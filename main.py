
for count in range(0, 101):
  if count % 3 == 0:
    if count % 5 == 0:
      print("fizzbuzz")
    else:
      print("fizz")
  if count % 5 == 0:
    if count % 3 == 0:
      print("fizzbuzz")
    else:
      print("buzz")

  if count % 3 !=0 and count % 5 != 0:
    print(count)




