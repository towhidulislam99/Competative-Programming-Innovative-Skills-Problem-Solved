def max_min(numbers):
    if not numbers:
        return None
    maximum = numbers[0]
    minimum = numbers[0]
    
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
            
    return maximum, minimum

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
max_num, min_num = max_min(numbers)
print(f"Maximum: {max_num}, Minimum: {min_num}")