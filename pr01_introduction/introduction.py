"""Taneli esimene programm :^)."""

name = input("Hello, my name is Python! Please type your name to continue our conversation.")

experience = input("Have you programmed before?.")

if experience == "Yes":
    print("Congratulations, " + name + "! It will be a little bit easier for you.")
elif experience == "No":
    print("Don`t worry, " + name + "! You will learn everything you need.")
else:
    print("Your input is incorrect!")
