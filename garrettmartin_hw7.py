def fizzbuzz(idx=99):
    val = idx
    list = []

    for x in range(1,101):
        if (x % 3 == 0):
            list.append("Fizz")
        else:
            list.append(str(x))

    if idx != 99:
        return(list[idx])
    else:
        return(print(*list))
