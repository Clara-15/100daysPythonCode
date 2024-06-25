#input commands shows the text on the screen but, won't do anything else untill the user has typed something in and pressed enter.
#variable is a container that stores data
#variable names can't have spaces in the e.g i_love_tulip_flowers or iLoveTulipFlowers
#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)

# we use = sign to assign a variable

myName =input("What's your name?")
favFood =input("What's your favourite food?")
favMusic=input("What's your favourite music?")
location=input("Where do you live?")
 
print()
print("So, you're")
print(myName)
print("You seem hungry for")
print(favFood)
print("You can order via Glovo app and they wil deliver at your doorstep in")
print(location)
print("While waiting, you can be listening to")
print(favMusic)
print("🙂" )
