valid = ["A", "B", "AB", "0"]
valid_2 = ["-", "+"]
answer1 = ""
answer2 = ""

print ("Bloodtype calculator")
print ("Please select bloodtype of mother")

bloodtype_m = input().upper()
while bloodtype_m not in valid:
    print ("Invalid input! Only A, B, AB or 0 allowed.")
    bloodtype_m = input().upper()

print ("Please select bloodtype of father")
bloodtype_f = input().upper()
while bloodtype_f not in valid:
    print ("Invalid input! Only A, B, AB or 0 allowed.")
    bloodtype_f = input().upper()

print ("Please select Rh-factor of mother")
rh_mom = input().strip()
while rh_mom not in valid_2:
    print ("Invalid input! Only - or + allowed.")
    rh_mom = input().strip()

print ("Please select Rh-factor")
rh_dad = input().strip()
while rh_dad not in valid_2:
    print ("Invalid input! Only - or + allowed.")
    rh_dad = input().strip()

if bloodtype_m == "A":
    if bloodtype_f == "A":
        answer1 = ("Your bloodtype is either A or 0")
    elif bloodtype_f == "B":
        answer1 = ("Your bloodtype is either A, B, AB or 0")
    elif bloodtype_f == "AB":
        answer1 = ("Your bloodtype is either A, B or AB")
    elif bloodtype_f == "0":
        answer1 = ("Your bloodtype is either A or 0")

elif bloodtype_m == "B":
    if bloodtype_f == "A":
        answer1 = ("Your bloodtype is either A, B, AB or 0")
    elif bloodtype_f == "B":
        answer1 = ("Your bloodtype is either B or 0")
    elif bloodtype_f == "AB":
        answer1 = ("Your bloodtype is A, B or AB")
    elif bloodtype_f == "0":
        answer1 = ("Your bloodtype is either B or 0")

elif bloodtype_m == "AB":
    if bloodtype_f== "A":
        answer1 = ("Your bloodtype is either A, B or AB")
    elif bloodtype_f == "B":
        answer1 = ("Your bloodtype is A, B or AB")
    elif bloodtype_f == "AB":
        answer1 = ("Your bloodtype is A, B or AB")
    elif bloodtype_f == "0":
        answer1 = ("Your bloodtype is either A or B")

elif bloodtype_m == "0":
    if bloodtype_f == "0":
        answer1 = ("Your bloodtype is 0")
    elif bloodtype_f == "A":
        answer1 = ("Your bloodtype is either A or 0")
    elif bloodtype_f == "B":
        answer1 = ("Your bloodtype is either B or 0")
    elif bloodtype_f == "AB":
        answer1 = ("Your bloodtype is either A or B")

if rh_mom == "-" and rh_dad == "-":
    answer2 = ("Your Rh-factor is negative")
else:
    answer2 = ("Your Rh-factor is positive")

print(answer1 + ". " +  answer2 + ".")
