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
    # num = input()
    # print('Enter the times of guessing(1/3/5):')
    # num = input()
    # a = 0
    # x = 0
    # y = 0
#judge the condition
    start=input("The game begins!")
    match start:
        
        case "userA =='p' and userB == 's' and num == 1":
            # y+=1
            # a+=1
            # case "num == 1":
            print('computer wins')
            False
    # if userA =="p" and userB == "s":
    #     a+=1
        case "userA =='p' and userB == 's' and num == 3":
            a+=1
            y+=1
            if a<3:
                True
            if a==3 and x<y:
                print("computer wins")
                False
            if a==3 and x>y:
                print("userA wins")
                False
        case "userA =='p' and userB == 's' and num == 5":
            a+=1
            y+=1
            if a==5 and x<y:
                print("computer wins")
                False
            if a==5 and x>y:
                print("userA wins")
                False
       
        case "userA =='s' and userB == 'p' and num==1":
            print('userA wins')
            False
        case "userA =='s' and userB == 'p' and num==3":
            a+=1
            x+=1
            if a<3:
                True
            if a==3 and x<y:
                print("computer wins")
                False
            if a==3 and x>y:
                print("userA wins")
                False
        case "userA =='s' and userB == 'p' and num == 5":
            a+=1
            y+=1
            if a==5 and x<y:
                print("computer wins")
                False
            if a==5 and x>y:
                print("userA wins")
                False

        case "userA == 'p' and userB == 'r' and num == 1":
            print('userA wins')
            False
        case "userA =='p' and userB == 'r' and num == 3":
            a+=1
            x+=1
            if a<3:
                True
            if a==3 and x<y:
                print("computer wins")
            else:
                print("userA wins")
                False
        case "userA =='p' and userB == 'r' and num == 5":
            a+=1
            x+=1
            if a<5:
                True
            if a==5 and x<y:
                print("computer wins")
                False
            if a==5 and x>y:
                print("userA wins")
                False
        case "userA =='r' and userB == 'p' and num == 1":
            print("computer wins")
            False
        case "userA =='r' and userB == 'p' and num == 3":
            a+=1
            y+=1
            if a<3:
                True
            if a==3 and x<y:
                print("computer wins")
                False
            if a==3 and x>y:
                print("userA wins")
                False
        case "userA =='r' and userB == 'p' and num == 5":
            a+=1
            y+=1
            if a<5:
                True
            if a==5 and x<y:
                print("computer wins")
                False
            if a==5 and x>y:
                print("userA wins")
                False
        case "userA =='s' and userB == 'r' and num == 1":
            print("computer wins")
            False
        case "userA =='s' and userB == 'r' and num == 3":
            a+=1
            y+=1
            if a<3:
                True
            if a==3 and x<y:
                print("computer wins")
                False
            if a==3 and x>y:
                print("userA wins")
                False
        case "userA =='s' and userB == 'r' and num == 5":
            a+=1
            y+=1
            if a<5:
                True
            if a==5 and x<y:
                print("computer wins")
                False
            if a==5 and x>y:
                print("userA wins")
                False
        case "userA =='r' and userB == 's' and num == 1":
            print("userA wins")
            False
        case "userA =='r' and userB == 's' and num == 3":
            a+=1
            x+=1
            if a<3:
                True
            if a==3 and x<y:
                print("computer wins")
                False
            if a==3 and x>y:
                print("userA wins")
                False
        case "userA =='r' and userB == 's' and num == 5":
            a+=1
            x+=1
            if a<5:
                True
            if a==5 and x<y:
                print("computer wins")
                False
            if a==5 and x>y:
                print("userA wins")
                False
        case "userA == userB":
            print('draw: no one wins')
            True 

