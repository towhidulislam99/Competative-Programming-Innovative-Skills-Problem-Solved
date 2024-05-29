def particular_digit_count(list_A, target):
    count = 0
    for i in range(len(list_A)):
        if list_A[i] == target:
            count += 1
    return count  

list_A = input()  
target = input()  

number = particular_digit_count(list_A, target)
print(f"Number: {list_A}, Target Number: {target}, occurs {number} times")
