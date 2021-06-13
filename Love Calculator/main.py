print("-" * 50)
print("\t Welcome to the Love Calculator!")
print("-" * 50)
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

name1.count('t')
name1.count("r")
name1.count("u")
name1.count("e")

FirstNameTrue = name1.count('t') + name1.count("r") + name1.count("u") + name1.count("e")

name2.count("t")
name2.count("r")
name2.count("u")
name2.count("e")

SecondNameTrue = name2.count('t') + name2.count("r") + name2.count("u") + name2.count("e")

TrueTotal = FirstNameTrue + SecondNameTrue

name1.count("l")
name1.count("o")
name1.count("v")
name1.count("e")

FirstNameLove = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")

name2.count("l")
name2.count("o")
name2.count("v")
name2.count("e")

SecondNameLove = name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")
LoveTotal = FirstNameLove + SecondNameLove

Convert = str(TrueTotal) + str(LoveTotal)
Score = int(Convert)

print(f"Your score is: {Score}")

if Score < 10 or Score > 90:
    print(f"Your score is {Score}, you go together like coke and mentos.")
elif Score >= 40 or Score >= 50:
    print(f"Your score is {Score}, you are alright together.")
else:
    print(f"Youre score is: {Score}")
