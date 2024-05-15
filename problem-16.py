def odd_even_count(numbers):
    count_even = 0
    count_odd = 0
    
    for i in numbers:
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    
    return count_even, count_odd

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_count, odd_count = odd_even_count(numbers)
print(f"Number of even elements: {even_count}")
print(f"Number of odd elements: {odd_count}")