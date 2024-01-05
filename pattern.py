                                                    # 1.

# rows=int(input())
# col=int(input())
# for i in range(rows):
#     for j in range(col):
#         print('+',end=' ')
#     print()

                                                        # 2.

# rows=int(input('row'))
# col=int(input('col'))
# for i in range(rows):
#     for j in range(col):
#         if i==0 or i==rows-1:
#             print('+',end=' ')
#         else:
#             if j == 0 or j==col-1:
#                 print('+',end=' ')
#             else:
#                 print(' ',end=' ') 
#     print()

                                                            # 3.

# rows=int(input('row'))
# col=int(input('col'))
# for i in range(rows):
#     for j in range(col):
#         if i==0 or i==rows-1 :
#             print('+',end=' ')
#         else:
#             # if j == 0 or j==col-1 or j==i: or
#             if j == 0 or j==col-1 or j==i or rows-i-1==j:
#                 print('+',end=' ')
#             else:
#                 print(' ',end=' ') 
#     print()

                                                            # 4.

# rows=int(input('row'))
# col=int(input('col'))
# for i in range(rows):
#     for j in range(col):
#         if j==0 or j==col-1 :
#             print(' ',end=' ')
#         else:
#             if j == i or rows-i-1==j :
#                 print(' ',end=' ')
#             else:
#                 print('*',end=' ') 
#     print()

                                                        # 5.

rows=int(input('row'))
for i in range(1,rows+1):
    
    print('*'*i)    

                                            # 6.

# row=int(input('row'))

# for i in range(1,row+1):
    
#     print('  '*(row-i),'* '*i,)    


# row=int(input('row'))

# for i in range(1,row+1):
#     print(' '*(row-i),'* '*i)
    
                                                        # 7.

# row=int(input('row'))
# out='''
# '''
# for i in range(1,row+1):
#     out=out+(' '*(row-i)+'* '*i)
#     out=out+'\n'
    
# for i in range(0,row):
#     out=out+(' '*(row-i)+'*'*(i*2+1))
#     out=out+'\n'
# #with open('part1.txt','w') as file:
#     #file.write(out)
# name=input('enter name of file:-')    # to remane the txt file
# with open(f'{name}.txt','w')as file:
#     file.write(out)            




























