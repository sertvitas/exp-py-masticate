temperature = 55
forecast = str("rain")

if temperature > 80:
    print("It's too hot")
    print("Stay indoors")
elif temperature < 60 and forecast == "rain":
    print("That rain makes for hypothermia weather...")
elif temperature < 60:
    print("Bit chilly")
    print("Stay in")
else:
    print("Take a hike :)")
print("Have a good one")
