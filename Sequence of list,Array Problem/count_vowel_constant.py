def vowel_consonant(character):
  vowel = "aeiouAEIOU"
  vowel_count = 0
  constant_count = 0
  for i in character:
    if i.isalpha():
      if i in vowel:
        vowel_count += 1
      else:
        constant_count += 1
  return vowel_count,constant_count

character = input()
vowels, consonants = vowel_consonant(character)
print(f"Vowels: {vowels}, Consonants: {consonants}")