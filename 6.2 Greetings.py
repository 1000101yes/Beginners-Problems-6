time = 0
name = input("What is your name").lower()
what = int(input("What time of day is it for you?"))
print(name)
if what in range(0, 12):
    print("Acceptable morning!")
elif what in range(13, 17):
    print("Best time of day and you spend it in school")
elif what in range(18, 23):
    print("Unacceptable morning")
else:
    print("erm what the sigma")
