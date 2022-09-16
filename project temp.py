      #----------------------------------------------------------------------------
      # Created By  :       Timothy Tran
      # Created Date:       8/31/2022
      # Project Name:       Hello world
      # Project Purpose:    Print anything
      # Project Function:   
      # ---------------------------------------------------------------------------
      # Psuedocode:
      #import random
      # initilize y as a string "AHHHHHHHHH"
      # print Hello world, Type something
      # takes in input, and puts it under the variable "x"
"""# does an if, that states if you were to type anything that had a letter value less then AHHHHHHHHHH
      then it would print " low", if you were to type something that had a letter value more than AHHHHHHHH
      then it would print "high"
      """
      #prints Give two random numbers
      #asks for and input, and sets it as y
      #asks for and input, and sets it as X
      #does a random randint of 0-9999999999 and sets it as a variable named lotto
      #creates a new function called count, and sets it as 0
"""# does and for loop with the counting vari. being L, and counting from 1-10
      It also uses the count variable, and adds +1 to the current value it was at that time, 
      and does a print statement turing count into a string"""
      #prints out 3 spaces with \n
      #sets the count variable to 0
      #does the same thing as the other for loop, but with 1-100
      #does a print that prints lotto as a str.
      # ---------------------------------------------------------------------------
import random
y = "AHHHHHHHHHHHHH"
print("Hello world, Type something")
x = input("")

if (x < y):
      print("low")
if (x > y):
      print("high")

print("Give two random numbers")
y = input("")
x = input("")
lotto = random.randint(0,9999999999)
count = 0
for L in range(0,10):
      count = count + 1
      print(str(count))
print("\n\n\n")
count = 0
for L in range(0,100):
      count = count + 1
      print(int(count))
print(str(lotto))