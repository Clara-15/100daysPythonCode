#Nesting putting if inside if statement


print("Welcome to Bible Character Game")
bibleCharacter= input("Who is your favourite Bible character? ")

if bibleCharacter == "Esther":
    print("She was Mordecai's niece!")
    confirmation = input("Did you know that?")

    if confirmation == "Yes":
      print("Awesome! Esther was a brave and faithful woman")
    else:
       print("Now you know! ")

elif bibleCharacter =="David":
    print("He was a man after God's own heart!")
    confirmation = input("Did you know that?")

    if confirmation == "Yes":
      print("Awesome! David was a courageous and devoted leader.")
    else:
       print("Now you know! ")

elif bibleCharacter =="Moses":
    print("He led the Israelites out of Egypt!")
    confirmation = input("Did you know that?")

    if confirmation == "Yes":
      print("Awesome! Moses was a faithful and powerful prophet.")
    else:
       print("Now you know! ")
else:
   print(" 😞Try again!") 
 
