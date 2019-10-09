string = input("")
starting_number = 1
original_number = 0

length_of_string = len(str(string))-1

while original_number <= length_of_string:
  if(original_number == length_of_string):
    final = string[original_number] * starting_number
    print(final + str(starting_number))
    break
  if(string[original_number] == string[original_number + 1]):
    original_number += 1
    starting_number += 1
  elif(string[original_number] != string[original_number + 1]):
    final = string[original_number] * starting_number
    print(final + str(starting_number), end = "" )
    original_number += 1
    starting_number = 1
    
