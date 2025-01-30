#----------------------------------
#Exercise 1
# Which statement is a correct syntax to break out of a loop?
# break

#----------------------------------
#Exercise 2
# Print i as long as i is less than 6.
i = 1
while i < 6:
  print(i)
  i += 1
# while i < 6:

#----------------------------------
#Exercise 3
# Stop the loop if i is 3.
i = 1
while i < 6:
  if i == 3:    
    break
  i += 1
# break

#----------------------------------
#Exercise 4
# In the loop, when i is 3, jump directly to the next iteration.
i = 0
while i < 6:
  i += 1
  if i == 3:   
    continue
  print(i)
# continue

#----------------------------------
#Exercise 5
# Print a message once the condition is false.
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
# else:

#----------------------------------