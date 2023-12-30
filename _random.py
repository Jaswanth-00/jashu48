import random
num=random.randint (50,1000)
while True:
    a=int(input('enter a number:-'))
    if a==num:
        print('u successfully gussed a number')
        break
    elif a<num:
        print('enter  greater number')
    elif a>num:
        print('enter lesser number')
        