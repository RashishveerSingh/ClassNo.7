#activity 1 exam elgilibility check

medic_cause = input("enter your medical cause, Y or N:")
atten = int(input("enter the attendance of your students:"))

if medic_cause == 'Y':
    print("you are allowed")
else:
    if atten >= 75:
        print("you are allowed")
    else:
        print("you are NOT allowed")