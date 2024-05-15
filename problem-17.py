def count_negative_element(numbers):
  count_all = 0

  for i in numbers:
    if i < 0:
      count_all += 1
  return count_all

numbers = [1,-1,2,-2,3,-3,4,]
count_all = count_negative_element(numbers)
print(f"Number of Negative Element: {count_all}")