def list_sorter():
  list = []
  number_1 = int(input("Type the first number: "))
  list.append(number_1)

  number_2 = int(input("Type the second number: "))
  list.append(number_2)

  number_3 = int(input("Type the third number: "))
  list.append(number_3)
  
  print(list)

  list.sort()

  print(list)

list_sorter()