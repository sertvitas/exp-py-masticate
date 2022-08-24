"""weather actions"""
TEMPERATURE = 55
FORECAST = str("rain")

if TEMPERATURE > 80:
    print("It's too hot")
    print("Stay indoors")
elif TEMPERATURE < 60 and FORECAST == "rain":
    print("That rain makes for hypothermia weather...")
elif TEMPERATURE < 60:
    print("Bit chilly")
    print("Stay in")
else:
    print("Take a hike :)")
print("Have a good one")
