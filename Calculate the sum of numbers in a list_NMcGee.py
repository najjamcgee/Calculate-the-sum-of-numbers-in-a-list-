"""
Name: Najja McGee
Date: June 27th, 2023
Course: CIS 111
Section: 03
Program Name: Calculate the sum of numbers in a list 

Algirithm:
1. create a count variable to keep track of the numbers
2. create a variale with a list
3. Prompt the user to enter a number
4. input those number into the variable list (element holder)
5. when prompted to quit press 0
6. then add all the numbers in the list
7. Display the sum of numbers in the list that were inputed.
"""
count = 0
my_list = []

while True:
  user_input = int(input("Enter a number or press 0 to quit: "))
  if user_input == 0:
    break
  my_list.append(user_input)
print(my_list)

for user_input2 in my_list:
  count += user_input2
print(count)
  