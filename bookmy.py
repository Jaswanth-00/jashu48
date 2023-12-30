print('welcom to bookmy show')
name=input('enter you are name:-')
seats=int(input('select no.of seats:'))
seat=int(input('select 1->diamond \n,2->gold,3->silver'  ))
if seats==1:
       amount=seats*200
elif(seats==2):
    amount=seats*150
elif seats==3:
        amount=seats*100
print(f'hi {name} you booked {seats} seats and total is :{amount} ')








