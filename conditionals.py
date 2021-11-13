temperature = int(input("Enter a number between 0 and 120: "))

# if water's temp is less than 4, it's frozen
if (temperature <= 4):
    # water is frozen
    print("water is a solid")
elif (temperature < 100):
    # water should be a liquid
    print("water is a liquid")
else:
    print("water is a vapor")