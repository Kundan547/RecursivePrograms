def testing(test):
    if test < 1:
        return
    else:
        print(test, end=" ")
        testing(test -1)
        print(test, end=" ")
        return

test = int(input("Enter a number: "))
testing(test)