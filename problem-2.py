def maximum(numone,numtwo,numthree):
  if numone < numtwo:
    return numtwo
  elif numone < numthree:
    return numthree
  elif numtwo < numone:
    return numone
  elif numtwo < numthree:
    return numthree
  else:
    return numthree

print(maximum(20, 10, 30))