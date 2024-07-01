#ifStatement and Else
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# a =500
# b = 50
# if b>a:
#  print("b is greater than a")
# else:
#  print("b is not greater than a")


# name=input("What's your name?")
# age=int(input("How old are you?"))
# if age >= 18:
#  print( name, "You're eligible to vote!")
# else:
#  print( name, "You're not eligible to vote!")


print("\033[35mWelcome to the 'Who am I?' game!")
print("Try to guess the Bible character based on the clues given.\033[0m")

print("I built an ark to survive the great flood.")
answer = input("Who am I? ")
if answer == "noah":
     print("Correct! I am Noah.")
else:
   print("Incorrect. Let's try another one.")

print("I led the Israelites out of Egypt and received the Ten Commandments.")
answer = input("Who am I? ")
if answer == "moses":
    print("Correct! I am Moses.")
else:
    print("Incorrect. Let's try another one.")

print("I was thrown into a lions' den for praying to God.")
answer = input("Who am I? ")
if answer == "daniel":
    print("Correct! I am Daniel.")
else:
    print("Incorrect. Let's try another one.")

print(" I was swallowed by a big fish because I tried to run away from God.")
answer = input("Who am I? ")
if answer == "jonah":
    print("Correct! I am Jonah.")
else:
    print("Incorrect. Let's try another one.")

print(" I am known as the 'beloved disciple' and wrote the fourth Gospel.")
answer = input("Who am I? ")
if answer == "john":
    print("Correct! I am John. \033[35mThanks for playing!\033[0m")
else:
    print("Incorrect. \033[35mThanks for playing!\033[0m")

