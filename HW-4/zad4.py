def input_nums(n):
    nums = []
    if not type(n) == int:
        return list()
    else:
        for i in range(n):
            x = input('Въведете число: ')
            if type(x) == int:
                nums.append(x)
            elif type(x) == str and x.isnumeric():
                nums.append(int(x))
    return nums

# print(input_nums(4))

# ----------------------------------------------------

def sum_list(lst):
    sum = 0
    for i in lst:
        if type(i) == int or type(i) == float:
            sum += i
        elif type(i) == str and i.isnumeric():
            sum += int(i)
    return sum

# print(sum_list([1,'4','g',4.2]))
# print(sum_list(['aaa','ff']))

# ---------------------------------------------------------

def max_of_two(a,b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        if a > b:
            return a
        if a < b:
            return b
        if a == b:
            return a
    elif (type(a) != int or type(a) != float) and (type(b) == int or type(b) == float):
        return b
    elif (type(b) != int or type(b) != float) and (type(a) == int or type(a) == float):
        return a
    else:
        return

# print(max_of_two(5.3, 'gg'))

# --------------------------------------------------------

# print(max_of_two(sum_list(input_nums(4)), sum_list(input_nums(3))))

print(max_of_two(sum_list([4, "AA@", 3.12, "1"]), '9.2'))