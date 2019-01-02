import random
def games():
    user=0
    me=0
    while(True):
        n1=int(input("How many rounds do you want the match to be?"))
        for i in range(0,n1):
            usr_choice=input("Choose one: rock,paper or scissors")
            n3=random.randint(1,4)
            if n3==1:
                my_choice='rock'
            elif n3==2:
                my_choice='paper'
            else:
                my_choice='scissors'
            print("My selection is: ",my_choice)
            print("Your selection is: ",usr_choice)
            if my_choice==usr_choice:
                print("It's a draw!")
            elif my_choice=='rock':
                if usr_choice=='paper':
                    print("You won the round!")
                    user=user+1
                else:
                    print("I won the round!")
                    me=me+1
            elif my_choice=='paper':
                if usr_choice=='rock':
                    print("I won the round!")
                    me=me+1
                else:
                    print("You won the round!")
                    user=user+1
            else:
                if usr_choice=='rock':
                    print("You won the round!")
                    user=user+1
                else:
                    print("I won the round!")
                    me=me+1
        if user>me:
            print("You won the match!")
        else:
            print("I won the match!")
        n4=input("Do you want to play one more game?- yes or no")
        n4=n4.lower()
        if n4=='no':
            break
games()