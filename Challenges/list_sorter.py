def list_sorter():
  list = []
  for i in range(1, 6):
    number_i = int(input(f"Type the number {i}: "))
    list.append(number_i)
  
  print(list)

  list.sort()

  print(list)

list_sorter()