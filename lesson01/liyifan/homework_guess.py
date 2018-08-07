import random
final = 0
n = random.randint(0,100)

for a in range(1,7):
    guess = int(input("Enter your guess number :"))
    if guess > n:
        print("\033[35mYour number is higher!\033[0m")
    elif guess < n:
        print("\033[35mYour number is lower!\033[0m")
    else:
        print("\033[36mYou are right ,my bro!\033[0m")
        final = 1
        break
if final == 0:
    print("""
    **************************

    Sorry,you have no chances now...""")
    print("    The right number is {}.".format(n))
    print("""
    **************************""")
