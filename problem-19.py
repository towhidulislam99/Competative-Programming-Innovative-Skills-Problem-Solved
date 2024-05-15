def count_frequenct_element(numbers):
  freq_numbers = {}

  for i in numbers:
    if i in freq_numbers:
      freq_numbers[i] += 1
    else:
      freq_numbers[i] = 1
  return freq_numbers

numbers = [1, 1, 2, 3, 3, 5, 5, 6, 3, 4, 7, 8]
frequencies = count_frequenct_element(numbers)

for key, value in frequencies.items():
    print(f"Element {key} occurs {value} times")