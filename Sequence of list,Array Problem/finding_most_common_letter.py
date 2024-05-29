def most_common_letter(word):
    letter = word.lower()
    freq = {}

    for i in letter:
        if i.isalpha():
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
      
    return freq

word = input()
freq1 = most_common_letter(word)
char = max(freq1, key=freq1.get) 
value = freq1[char] 
print(f"Most Common Letter: '{char}' value is: {value}")
print(f"Frequency: {freq1}")
