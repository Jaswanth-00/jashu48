# Def:-decoratorm is a function which adds aditional information to a function 



# def add():
#    a=int(input('enter a:-'))
#    b=int(input('enter b:-'))
#    print(a+b)

# def cal(func):
#     def inner():
#         print('operation started')
#         func()
#         print('operation done')
#     return inner

# add=cal(add)
# add()

import time
def timer(func):
    def inner():
        start = time.time()
        func()
        end= time.time()
        print(f'Time taken to answer question:- {end-start} secs ')

    return inner

@timer
def question1():
    print('who is the prime minister of India :- ')
    response = input('enter your response :- ')

@timer
def question2():
    print('who is the  chief minister of Andra pradesh :- ')
    response = input('enter your response :- ')

question1()
question2()





































































