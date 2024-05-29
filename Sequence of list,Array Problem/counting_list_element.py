def count_frequency(data):
    freq_dict = {}
    for item in data:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict

data_str = input()
data = data_str.split()
frequency = count_frequency(data)
print(frequency)