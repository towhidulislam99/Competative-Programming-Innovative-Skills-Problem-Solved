def upper_lower(character):
  if character.isupper():
    return "Uppercase"
  elif character.islower():
    return "Lowercase"
  else:
    return "Others"
print(upper_lower("L"))