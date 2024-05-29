def frequency_of_words_different_lengths(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        length = len(word)
        if length in freq:
            freq[length] += 1
        else:
            freq[length] = 1

    return freq

sentence = input()
length_freq = frequency_of_words_different_lengths(sentence)
for length, count in length_freq.items():
    print(f"{length}-letter words: {count}")