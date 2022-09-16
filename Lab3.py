game=True

print("Welcome to the Flarsheim Guesser!")
print()
print(f"Please think of a number between and including 1 and 100.")
print()
while game:
    num=int(input("What is the remainder when your number is divided by 3?"))
    while num<=0:
        print("The value entered must be 0 or greater")
        num = int(input("What is the remainder when your number is divided by 3?"))
    while num>=3:
        print("The value entered must be less than 3")
        num = int(input("What is the remainder when your number is divided by 3?"))



    print()
    num2 = int(input("What is the remainder when your number is divided by 5?")) # 0 to 4
    while num2<=0:
        print("The value entered must be 0 or greater")
        num2= int(input("What is the remainder when your number is divided by 5?"))
    while num2>=4:
        print(f"The value entered must be less than 4")
        num2=int(input("what is the remainder when your number is divided by 5?"))

    print()
    num3=int(input("What is the remainder when your number is divided by 7?")) # 0 to 6
    while num3<=0:
        print("The value entered must be 0 or greater")
        num3=int(input("What is the remainder when your number is divided by 7?"))
    while num3>=6:
        print("The value entered must be less than 6")
        num3=int(input("What is remainder when your number is divided by 7?"))

    for i in range(1,101):
        if i%3==num and i%5==num2 and i%7==num3:
            print("Your number was ",i)

    print("How amazing is that?")
    play = input("Do you want to play again? Y to continue, N to quit ==> ")
    if play == "y" or play == "Y":
        game = True
    else:
        game = False





