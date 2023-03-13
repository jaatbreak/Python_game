import random
n=random.randint(1,5)
Number_of_Guesses = 1
print("---------Number of Guess Limit is only one  Time ------------------- ")
while (Number_of_Guesses<=2):
    Guess_Number=int(input("Enter the Guess No. :-"))
    if  Guess_Number<n:
        print("You enter the samll numer .Please Input is Greater ")
        break
    elif  Guess_Number>n:
        print("You Greater Number Please enter the Small no. :-")
        break
    else:
        print("!!!!!!!!!!!!!!----You Won---!!!!!!!!!!!!!!!!!!")
        print( Guess_Number,"===>The Number which you took to finish")
        break
        print(2 - Number_of_Guesses,"Number of Guess left")
        Number_of_Guesses+=1
    if Number_of_Guesses>2:
        print("game Over!!!!!")
        print("you System no was :-",Number_of_Guesses)
