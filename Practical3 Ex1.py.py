name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
income = int(input("Enter Your Income: "))
caste = input("Enter Your Caste(OPEN,SC,ST,OBC,): ")

if age<25 and income<300000 and caste in["OPEN"]:
    print("You Are Eligible ")
else:
    print("You Are NOT Eligible ")