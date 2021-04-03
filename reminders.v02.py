imort datetime

now.hour = int(input("what hour is it? (0-23)"))

now = datetime.now()
print(now.year, now.motnh, now.day, now.hour, now.minute, now.second)
if now.hour <= 5:
    print("Its early. You should be sleeping!")
elif now.hour <= 7:
    print("Wake up, brew that coffe, get that mile run in, and get that breakfast...")
elif now.hour <= 9:
    print("Time to go to work.")
elif now.hour <= 12:
    print()
else:
        print("You didn't type an acceptable value! (0-23)")
