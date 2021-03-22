usertime = int(input("what hour is it? (0-23)"))

if usertime <= 5:
    print("Its early. You should be sleeping!")
elif usertime <= 7:
    print("Wake up, brew that coffe, get that mile run in, and get that breakfast...")
elif usertime <=9:
    print("Time to go to work.")
elif usertime <=12:
    print()
else:
        print("You didn't type an acceptable value! (0-23)")
