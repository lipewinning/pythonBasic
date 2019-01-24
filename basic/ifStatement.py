is_male = True
is_tall = False

if is_male or is_tall:
    print('I am a man or tall')
elif is_male and not is_tall:
    print('I am a man')
else:
    print('I am neither male nor tall')


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print('the great one is ' + str(max_num(2,3,1)))


