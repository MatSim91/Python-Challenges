# Simple program that received five input numbers from the user
# and sort then in crescent order in a list

def list_sorter():
  list = []
  for i in range(1, 6):
    number_i = int(input(f"Type the number {i}: "))
    list.append(number_i)
  
  print(list)

  list.sort()

  print(list)

list_sorter()