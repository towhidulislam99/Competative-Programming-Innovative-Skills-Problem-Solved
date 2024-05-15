def alpha_digit_specha(character):
  if character.isalpha():
    return "Alphabet"
  elif character in "0123456789":
    return "Number"
  else:
    return "Special character"

print(alpha_digit_specha("*"))