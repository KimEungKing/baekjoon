while True:
  num_list = [] 
  sum = 0
  num = int(input())

  if num == -1:
    break

  else:
    for i in range(1,num):
      if num % i == 0:
        num_list.append(i)
        sum += i

    if sum == num:
      print(f"{sum} = ",end = '')  
      for a in num_list[:-1]:
        print(a,'+ ',end='')
      print(num_list[-1])

    else:
      print(f"{num} is NOT perfect.")

