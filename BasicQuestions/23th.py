#Find the count of digits in a number.
def Count_digit(number):
    return len(str(abs(number)))

number = int(input())

Digit_number = Count_digit(number)
print(f"The number of digits in {number} is {Digit_number} ")

# Approch 2 .

def count_digit(number):
    if number == 0:
        return 1
    number = abs(number)
    return len(str(number))

number = 4567821
digit = count_digit(number)

print(f"The number of digits in {number} is {digit}.")