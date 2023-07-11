#user input:p,s,r
#computer randomly input
import random
print('Enter the times of guessing(1/3/5):')
num = input()
a = 0
x = 0
y = 0
while True:
    print('Enter p/s/r:')
    userA = input()
    option = ['p','s','r']
    userB = random.choice(option)
    # print('Enter the times of guessing(1/3/5):')
    # num = input()
    # a = 0
    # x = 0
    # y = 0
#judge the condition
    if userA =="p" and userB == "s":
        a+=1
        if num == 1:
            print('userB wins')
            False
        else:
            y+=1
            if num == 3 and a<3:
                True
            if num == 5 and a<5:
                True
            else:
                if y>x:
                    print('computer wins')
                if y<x:
                    print('userA wins')
                False
    if userA =="s" and userB == "p":
        a+=1
        if num == 1:
            print('userA wins')
            False
        else:
            x+=1
            if num == 3 and a<3:
                True
            if num == 5 and a<5:
                True
            else:
                if y>x:
                    print('computer wins')
                if y<x:
                    print('userA wins')
                False

    if userA =="p" and userB == "r":
        a+=1
        if num == 1:
            print('userA wins')
            False
        else:
            x+=1
            if num == 3 and a<3:
                True
            if num == 5 and a<5:
                True
            else:
                if y>x:
                    print('computer wins')
                if y<x:
                    print('userA wins')
                False
    if userA =="r" and userB == "p":
        a+=1
        if num == 1:
            print('userB wins')
            False
        else:
            y+=1
            if num == 3 and a<3:
                True
            if num == 5 and a<5:
                True
            else:
                if y>x:
                    print('computer wins')
                if y<x:
                    print('userA wins')
                False

    if userA =="s" and userB == "r":
        a+=1
        if num == 1:
            print('userB wins')
            False
        else:
            y+=1
            if num == 3 and a<3:
                True
            if num == 5 and a<5:
                True
            else:
                if y>x:
                    print('computer wins')
                if y<x:
                    print('userA wins')
                False

    if userA =="r" and userB == "s":
        a+=1
        if num == 1:
            print('userA wins')
            False
        else:
            x+=1
            if num == 3 and a<3:
                True
            if num == 5 and a<5:
                True
            else:
                if y>x:
                    print('computer wins')
                if y<x:
                    print('userA wins')
                False

    if userA == userB:
        print('draw: no one wins')
        True 

