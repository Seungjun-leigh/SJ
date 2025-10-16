import random as rd
print("***GAMBLING SIMULATOR***")
kidney=int(2)
sell=int(0)
notBroke=bool(True)
money=int(5000)
bet=int(0)
while notBroke==True:
    sell-=1
    if type(money)==float:
        money=round(money)
    if money<=0:
        print("You went bankrupt")
        break
    elif money>=1000000:
        print("Ur rich")
        break
    print("Enter your bet. money:",money)
    if(rd.random()<0.2):
        print("Tip: Type \"all\" to bet all your money at once.")
    bet=input()
    if bet=="all":
        bet=money
    else:
        bet=int(bet)
    while bet>money:
        print("Ur too broke to bet this much.")
        bet=int(input())
    if rd.random()<0.5:
        bet/=2
        money-=bet
        print("You lost")
    else:
        money-=bet
        bet*=2
        money+=bet
        print("You won")
    if money<2000 and sell<=0:
        sell+=3
        print("Hi! You look broke. Do you want to sell your kidney for money? 1. Yes 2. No")
        choice1=int(input())
        if choice1==1:
            kidney-=1
            if kidney==0:
                print("You died because you sold both kidneys. The compiler is astonished by your stupidity.")
                break
            else:
                money+=100000
                print("You sold your kidney for 100000.")
        elif choice1==2:
            print("You didn't sell your kidney. Probably you'll have to sell it later.")
        else:
            print("You act as if you didn't understand. The stranger gets bored and searches for another victim.")
