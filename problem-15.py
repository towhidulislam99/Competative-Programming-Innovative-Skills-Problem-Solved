def second_largest(numbers):
  if len(numbers) < 2:
    return "It has must be 2 Numbers"
  first_big = max(numbers[0], numbers[1])
  second_big = min(numbers[0], numbers[1])
  for i in numbers[2:]:
    if i > first_big:
      second_big = first_big
      first_big = i
    elif i > second_big and i != first_big:
      second_big = i
  return second_big

numbers = [10, 20, 4, 35, 99]
second_largest = second_largest(numbers)
print("Second largest element is:", second_largest)