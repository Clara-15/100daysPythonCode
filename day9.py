#Casting
# int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
# float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
# str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

# myScore= int(input("What did you score in CyberSecurity?"))
# if myScore >= 80:
#   print("Distinction!")
# elif myScore >=70:
#   print("Credit!")

# elif myScore >=50:
#   print("Pass")

# else:
#   print("Fail!")

#float example
# myPi =float(input("What is Pi to 3dp?"))
# if myPi == 3.142:
#     print("Correct! 👏 ")

# else:
#     print("Try again! 😞 ") 

#Practice
print("Generation Identifier")

myYear = int(input("Which year were you born? "))
    
if 1883 <= myYear <= 1900:
        print('Hah! Lost Generation')
elif 1901 <= myYear <= 1927:
        print('Hah! The Greatest Generation')
elif 1928 <= myYear <= 1945:
        print('Wow! Silent Generation')
elif 1946 <= myYear <= 1964:
        print('Haiya! Baby Boomers')
elif 1965 <= myYear <= 1980:
        print('Hurray! Generation X')
elif 1981 <= myYear <= 1996:
        print('Mmmh! Millennials')
elif 1997 <= myYear <= 2012:
        print('Oh! Generation Z')
        
elif 2012 <=myYear <= 2024:
        print('Great! Generation Alpha')
else:
        print("Please enter a valid year.")