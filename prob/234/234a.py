def func(val):
  return val * val + 2 * val + 3 

num = int(input())
print(func(func(func(num) + num) + func(func(num))))