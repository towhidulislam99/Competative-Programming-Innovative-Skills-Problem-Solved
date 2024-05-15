def leap_year(year):
  if year % 400 == 0 and year % 100 == 0:
    return "Year is leap Year"
  elif year % 4 == 0 and year % 100 != 0:
    return "Year is Leap Year"
  else:
    return "Year is Not Leap Year"
  
print(leap_year(2004))