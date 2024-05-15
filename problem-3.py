def check_number(num):
    if num < 0:
        return "negative"
    if num > 0:
        return "positive"
    else:
        return "zero"

print(check_number(100))