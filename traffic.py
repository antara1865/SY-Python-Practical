print("*****TRAFFIC SIGNAL RULE*****")
Signal= input("Enter The Signal Color : ")

if Signal == "red":
    print("Action : STOP ")

elif Signal == "yellow":
    print("Action : Wait")

elif Signal == "greeen":
    print("Action : GO")

else :
    print("Invalid Signal")