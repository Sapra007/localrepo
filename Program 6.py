#write a program to concert kilometers to miles
kilometers = float(input("enter distance in kilometers:"))

#conversion factor: 1 kilometer = 0.621371 miles
conversion_factor = 0.621371

miles =kilometers * conversion_factor

print(f"{kilometers} kilometers is equal to miles {miles} miles")