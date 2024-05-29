def count_frequenct_element(word):
    letter = word.lower()
    freq_word = {}

    for i in letter:
        if i.isalpha(): 
            if i in freq_word:
                freq_word[i] += 1
            else:
                freq_word[i] = 1
    
    return freq_word

word = input()
frequencies = count_frequenct_element(word)

for char, count in frequencies.items():
    print(f"{char} -- {count}")


# words = input()
# letter = words.lower()
# fre = {}
# for i in set(letter):
#   fre[i] = letter.count(i)
# print(fre)
