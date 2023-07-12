#user input:p,s,r
#computer randomly input
import random
print('Enter the times of guessing(1/3/5):')
num = input()
a = 0
x = 0
y = 0
# game = True
while True:
    print('Enter p/s/r:')
    user = input()
    option = ['p','s','r']
    computer = random.choice(option)
    # num = input()
    # print('Enter the times of guessing(1/3/5):')
    # num = input()
    # a = 0
    # x = 0
    # y = 0

#judge the condition
    arr = [user,computer]
    # start=input("The game begins!")
    match arr:
        
        # case "userA =='p' and userB == 's' and num == 1":
        case ["p","s"]|["r","p"]|["s","r"]:
            if num == 1:
                        # y+=1
            # a+=1
            # case "num == 1":
                print('computer wins')
                break
            if num == 3 and a<2:
                a+=1
                y+=1
                True
            if num == 5 and a<4:
                a+=1
                y+=1
                True
            else:
                # a+=1
                y+=1
                if x<y:
                    print('computer wins')
                    break
                if x>y:
                    print('user wins')
                    break
        case ["s","p"]|["p","r"]|["r","s"]:
            if num == 1:
                        # y+=1
            # a+=1
            # case "num == 1":
                print('user wins')
                break
            if num == 3 and a<2:
                a+=1
                x+=1
                True
            if num == 5 and a<4:
                a+=1
                x+=1
                True
            else:
                # a+=1
                x+=1
                if x<y:
                    print('computer wins')
                    break
                if x>y:
                    print('user wins')
                    break
                        # y+=1
            # a+=1
            # # case "num == 1":
            #     print('computer wins')
            #     False
            # if num == 3 and a<3:
            #     a+=1
            #     y+=1
            #     True
            # if num == 5 and a<5:
            #     a+=1
            #     y+=1
            #     True
            # else:
            #     # a+=1
            #     y+=1
            #     if x<y:
            #         print('computer wins')
            #         False
            #     if x<y:
            #         print('user wins')
            #         False
    # if userA =="p" and userB == "s":
    #     a+=1
        case ["s","s"]|["r","r"]|["p","p"]:
            print("no one wins")
            True
            # case "userA =='' and userB == 's' and num == 3":
        #     a+=1
        #     y+=1
        #     if a<3:
        #         True
        #     if a==3 and x<y:
        #         print("computer wins")
        #         False
        #     if a==3 and x>y:
        #         print("userA wins")
        #         False
        # case "userA =='p' and userB == 's' and num == 5":
        #     a+=1
        #     y+=1
        #     if a==5 and x<y:
        #         print("computer wins")
        #         False
        #     if a==5 and x>y:
        #         print("userA wins")
        #         False
       
        # case "userA =='s' and userB == 'p' and num==1":
        #     print('userA wins')
        #     False
        # case "userA =='s' and userB == 'p' and num==3":
        #     a+=1
        #     x+=1
        #     if a<3:
        #         True
        #     if a==3 and x<y:
        #         print("computer wins")
        #         False
        #     if a==3 and x>y:
        #         print("userA wins")
        #         False
        # case "userA =='s' and userB == 'p' and num == 5":
        #     a+=1
        #     y+=1
        #     if a==5 and x<y:
        #         print("computer wins")
        #         False
        #     if a==5 and x>y:
        #         print("userA wins")
        #         False

        # case "userA == 'p' and userB == 'r' and num == 1":
        #     print('userA wins')
        #     False
        # case "userA =='p' and userB == 'r' and num == 3":
        #     a+=1
        #     x+=1
        #     if a<3:
        #         True
        #     if a==3 and x<y:
        #         print("computer wins")
        #     else:
        #         print("userA wins")
        #         False
        # case "userA =='p' and userB == 'r' and num == 5":
        #     a+=1
        #     x+=1
        #     if a<5:
        #         True
        #     if a==5 and x<y:
        #         print("computer wins")
        #         False
        #     if a==5 and x>y:
        #         print("userA wins")
        #         False
        # case "userA =='r' and userB == 'p' and num == 1":
        #     print("computer wins")
        #     False
        # case "userA =='r' and userB == 'p' and num == 3":
        #     a+=1
        #     y+=1
        #     if a<3:
        #         True
        #     if a==3 and x<y:
        #         print("computer wins")
        #         False
        #     if a==3 and x>y:
        #         print("userA wins")
        #         False
        # case "userA =='r' and userB == 'p' and num == 5":
        #     a+=1
        #     y+=1
        #     if a<5:
        #         True
        #     if a==5 and x<y:
        #         print("computer wins")
        #         False
        #     if a==5 and x>y:
        #         print("userA wins")
        #         False
        # case "userA =='s' and userB == 'r' and num == 1":
        #     print("computer wins")
        #     False
        # case "userA =='s' and userB == 'r' and num == 3":
        #     a+=1
        #     y+=1
        #     if a<3:
        #         True
        #     if a==3 and x<y:
        #         print("computer wins")
        #         False
        #     if a==3 and x>y:
        #         print("userA wins")
        #         False
        # case "userA =='s' and userB == 'r' and num == 5":
        #     a+=1
        #     y+=1
        #     if a<5:
        #         True
        #     if a==5 and x<y:
        #         print("computer wins")
        #         False
        #     if a==5 and x>y:
        #         print("userA wins")
        #         False
        # case "userA =='r' and userB == 's' and num == 1":
        #     print("userA wins")
        #     False
        # case "userA =='r' and userB == 's' and num == 3":
        #     a+=1
        #     x+=1
        #     if a<3:
        #         True
        #     if a==3 and x<y:
        #         print("computer wins")
        #         False
        #     if a==3 and x>y:
        #         print("userA wins")
        #         False
        # case "userA =='r' and userB == 's' and num == 5":
        #     a+=1
        #     x+=1
        #     if a<5:
        #         True
        #     if a==5 and x<y:
        #         print("computer wins")
        #         False
        #     if a==5 and x>y:
        #         print("userA wins")
        #         False
        # case "userA == userB":
        #     print('draw: no one wins')
        #     True 

