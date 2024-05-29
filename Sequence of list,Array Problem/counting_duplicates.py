def most_common_letter(word):
    letter = word.lower()
    freq = {}

    for i in letter:
        if i.isalpha():
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

    duplicates = [(char, count) for char, count in freq.items() if count > 1]
    return duplicates

word = input()
freq1 = most_common_letter(word)
for char, count in freq1:
    print(f"{char}: {count}")