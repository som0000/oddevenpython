# program to identify the even/odd state of given number
def isEven(number):
    if number % 2== 0:
        print("the entered number is even")
    else:
        print("the entered number is odd")


number=int(input("enter number: "))
isEven(number)
