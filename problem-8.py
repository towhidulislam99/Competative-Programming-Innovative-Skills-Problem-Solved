def vowel_consonant(character):
    if character in "aeiouAEIOU":
        return "Vowel"
    elif character.isalpha():
        return "Consonant"
    else:
        return "Not Vowel Not Constant"
print(vowel_consonant("@"))