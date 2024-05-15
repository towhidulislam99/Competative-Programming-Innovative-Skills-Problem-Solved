def check_divisible(num):
  if num % 5 == 0 and num % 11 == 0:
    return "This Number is Divisible by 5 and 11"
  else:
    return "Not Divisible"

print(check_divisible(100))