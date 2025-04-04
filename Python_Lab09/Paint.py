#Imports
import pygame
import math

def main():
    #Initialzing 
    pygame.init()

    #Screen 
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint")

    #Main Variables
    clock = pygame.time.Clock()
    radius = 15
    mode = 'blue'
    draw_mode = False
    eraser_mode = False
    shape_mode = None
    drawing = False

    drawings = []
    start_pos = None

    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

                #Color selection
                if event.key == pygame.K_r:
                    mode = 'red'
                    eraser_mode = False
                elif event.key == pygame.K_g:
                    mode = 'green'
                    eraser_mode = False
                elif event.key == pygame.K_b:
                    mode = 'blue'
                    eraser_mode = False

                #Radius control
                if event.key == pygame.K_UP:
                    radius = min(200, radius + 1)
                elif event.key == pygame.K_DOWN:
                    radius = max(1, radius - 1)

                #Mode selection
                if event.key == pygame.K_1: #Line mode
                    draw_mode = True
                    eraser_mode = False
                    shape_mode = None
                if event.key == pygame.K_2: #Eraser mode
                    eraser_mode = True
                    draw_mode = True
                    shape_mode = None
                if event.key == pygame.K_3: #Circle mode
                    shape_mode = 'circle'
                    draw_mode = False
                    eraser_mode = False
                if event.key == pygame.K_4: #Rectangle mode
                    shape_mode = 'rectangle'
                    draw_mode = False
                    eraser_mode = False
                if event.key == pygame.K_5: #Square mode
                    shape_mode = 'square'
                    draw_mode = False
                    eraser_mode = False
                if event.key == pygame.K_6: #Right triangle mode
                    shape_mode = 'right_triangle'
                    draw_mode = False
                    eraser_mode = False
                if event.key == pygame.K_7: #Equilateral triangle mode
                    shape_mode = 'equilateral_triangle'
                    draw_mode = False
                    eraser_mode = False
                if event.key == pygame.K_8: #Rhombus mode
                    shape_mode = 'rhombus'
                    draw_mode = False
                    eraser_mode = False

            #Mouse events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #Left mouse button
                    if draw_mode: #Start drawing
                        drawing = True
                        drawings.append({'type': 'line', 'color': (0, 0, 0) if eraser_mode else mode, 'radius': radius, 'points': []})
                    elif shape_mode: #Save the starting mouse position
                        start_pos = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: #Left mouse button
                    drawing = False #Stop drawing
                    if shape_mode and start_pos: #Save the ending mouse position
                        end_pos = event.pos
                        drawings.append({'type': 'shape', 'shape': shape_mode, 'color': mode, 'start': start_pos, 'end': end_pos, 'radius': radius})
                        start_pos = None

            if event.type == pygame.MOUSEMOTION and drawing:
                #Draw lines
                last_point = drawings[-1]['points'][-1] if drawings[-1]['points'] else None
                new_point = event.pos
                if last_point:
                    drawLineBetween(screen, last_point, new_point, radius, mode)
                drawings[-1]['points'].append(new_point)

        #Clear screen before redrawing
        screen.fill((0, 0, 0))

        #Draw in the correct order
        for item in drawings:
            if item['type'] == 'shape':
                drawShape(screen, item)
            elif item['type'] == 'line':
                for i in range(len(item['points']) - 1):
                    drawLineBetween(screen, item['points'][i], item['points'][i + 1], item['radius'], item['color'])

        pygame.display.flip()
        clock.tick(60)

#Draw line between two points
def drawLineBetween(screen, start, end, width, color_mode):
    color = (0, 0, 255) if color_mode == 'blue' else (255, 0, 0) if color_mode == 'red' else (0, 255, 0) if color_mode == 'green' else (0, 0, 0)

    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))

    if distance == 0:
        pygame.draw.circle(screen, color, start, width)
        return

    for i in range(distance):
        progress = i / distance
        x = int(start[0] * (1 - progress) + end[0] * progress)
        y = int(start[1] * (1 - progress) + end[1] * progress)
        pygame.draw.circle(screen, color, (x, y), width)

#Draw shapes
def drawShape(screen, shape):
    color = (0, 0, 255) if shape['color'] == 'blue' else (255, 0, 0) if shape['color'] == 'red' else (0, 255, 0) if shape['color'] == 'green' else (0, 0, 0)

    start = shape['start']
    end = shape['end']
    width = shape['radius'] * 2

    if shape['shape'] == 'circle':
        center = ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2)
        radius = max(abs(end[0] - start[0]), abs(end[1] - start[1])) // 2
        pygame.draw.circle(screen, color, center, radius, width)

    elif shape['shape'] == 'rectangle':
        x1, y1 = start
        x2, y2 = end
        top_left = (min(x1, x2), min(y1, y2))
        width_rect = abs(x2 - x1)
        height_rect = abs(y2 - y1)
        rect = pygame.Rect(top_left, (width_rect, height_rect))
        pygame.draw.rect(screen, color, rect, width)

    elif shape['shape'] == 'square':
        x1, y1 = start
        x2, y2 = end
        side = min(abs(x2 - x1), abs(y2 - y1))
        top_left_x = x1 if x2 >= x1 else x1 - side
        top_left_y = y1 if y2 >= y1 else y1 - side
        rect = pygame.Rect(top_left_x, top_left_y, side, side)
        pygame.draw.rect(screen, color, rect, width)

    elif shape['shape'] == 'right_triangle':
        points = [start, (start[0], end[1]), end]
        pygame.draw.polygon(screen, color, points, width)

    elif shape['shape'] == 'equilateral_triangle':
        x1, y1 = start
        x2, y2 = end
        base = x2 - x1
        height = abs(base * math.sqrt(3) / 2)
        if y2 < y1:
            height = -height
        point1 = (x1, y2)
        point2 = (x2, y2)
        point3 = ((x1 + x2) // 2, y2 - height)
        pygame.draw.polygon(screen, color, [point1, point2, point3], width)

    elif shape['shape'] == 'rhombus':
        x1, y1 = start
        x2, y2 = end
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2
        dx = abs(x2 - x1) // 2
        dy = abs(y2 - y1) // 2
        points = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]
        pygame.draw.polygon(screen, color, points, width)

main()