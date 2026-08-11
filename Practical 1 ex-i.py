name = input("Enter Your Name: ")

sub1 = float(input("Enter marks of Sub 1: "))
sub2 = float(input("Enter marks of Sub 2: "))
sub3 = float(input("Enter marks of Sub 3: "))
total = sub1+sub2+sub3
per = (total/300) * 100

print("----------ScoreCard----------\n")
print("Marks Of Sub 1: ", sub1)
print("Marks Of Sub 2: ", sub2)
print("Marks Of Sub 3: ", sub3)
print("Total Marks: ", total)
print("Percentage: ", per)