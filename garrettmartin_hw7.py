def fizzbuzz(idx=99):
    val = idx
    list = []

    for x in range(1,101):
        if (x % 3 == 0 and x % 5 == 0):
            list.append("FizzBuzz")
        elif (x % 3 == 0):
            list.append("Fizz")
        elif (x % 5 == 0):
            list.append("Buzz")
        else:
            list.append(str(x))

    if idx != 99:
        return(list[idx])
    else:
        return(print(*list))

def leapyear(x):
    pass
