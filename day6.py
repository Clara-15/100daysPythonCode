#Elifs
#Elifs must go after the if and before the last else
print("My Login Sytem")
username=input(" Enter your username:")
password=input("Enter your passowrd:")

if username =="Ann" and password == "#j56ann":
    print("Habari yako", username, ",nakutaki siku njema yenye baraka na manufaa. Usisahau leo ni siku ya maombi kanisani." )
    
elif username == "Eunice" and password == "123456": 
    print("Good evening", username, ",you seem abit stressed, hope all went well at work.If you free this evening, please come by the house and share what's going on.. " )
   
elif username == "Kamau" and password == "AnythigYellow@210":
    print( "Hello", username, "What a beautiful house you have, it's a dream house for many.Have a great day.Don't forget to share your contractor's details!")
    
elif username =="Cheptoo" and password == "password":
    print("Good afternoon", username, ",what did are you doing at the back alone and everybody is outside having lunch?, Hope all is well! Enjoy your evening and greet you father for me!")
   

else:
    print("Wrong credentials! Please try again!")


