def list_avg(lst, multiplier = 1):

    if not type(multiplier) == int:
        print('Въведете валиден множител!')
        quit()

    sum = 0
    cnt = 0

    for i in lst:
        if type(i) == int or type(i) == float:
            sum += i * multiplier
            cnt += 1
        elif type(i) == str and i.isnumeric():
            sum += int(i) * multiplier
            cnt += 1
    
    if cnt == 0:
        print('Във въведения списък няма валидни числа!')
        quit()
    else:
        return(sum/cnt)
    
print(list_avg([2,'9','hi']))
print(list_avg(['hello','python']))