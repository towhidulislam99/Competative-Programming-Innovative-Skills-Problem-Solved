def list_odd_even(data):
    count_even = 0
    count_odd = 0
    for num in data:
        if num % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return count_even, count_odd

data = input()
data = list(map(int, data.split()))

even_count, odd_count = list_odd_even(data)
print(f"Even numbers count: {even_count}, Odd numbers count: {odd_count}")2 