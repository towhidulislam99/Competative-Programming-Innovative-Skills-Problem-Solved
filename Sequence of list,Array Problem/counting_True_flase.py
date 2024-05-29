def count_boolean_values(data):
    count_true = 0
    count_false = 0
    for value in data:
        if value:
            count_true += 1
        else:
            count_false += 1
    return count_true, count_false

data_str = input()
data = [value.lower() == 'true' for value in data_str.split()]

true_count, false_count = count_boolean_values(data)
print(f"True occurrences: {true_count}, False occurrences: {false_count}")