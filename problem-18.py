def unique_elements(numbers):
    unique_list = []

    for i in numbers:
        if i not in unique_list:
            unique_list.append(i)
    
    for i in unique_list:
        print(i)

numbers = [1, 1, 2, 3, 3, 5, 5, 6, 3, 4, 7, 8]
unique_elements(numbers)