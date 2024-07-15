#Finding the digit at a specific place in a number.
def Find_digit(number, position):
    num_str = str(number)
    if position < 1 or position > len(num_str):
        return False
    return int(num_str[position])

number = int(input())
position = int(input())

digit = Find_digit(number, position)

print(f"The digit at the position {position} is {digit} .")