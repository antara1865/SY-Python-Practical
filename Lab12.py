coordinates_mumbai = (18.5204, 73.8567)      
coordinates_pune= (19.0760, 72.8777)     

print("Mumbai Location :", coordinates_mumbai)
print("Pune Location :", coordinates_pune)

print("\nLatitude of Mumbai:", coordinates_mumbai[0])
print("Longitude of Mumbai:", coordinates_mumbai[1])

print("\nMumbai coordinates using slicing:", coordinates_mumbai[:])
print("Latitude using slicing:", coordinates_mumbai[:1])
print("Longitude using slicing:", coordinates_mumbai[1:])

latitude, longitude = coordinates_mumbai

print("\nAfter tuple unpacking:")
print("Latitude:", latitude)
print("Longitude:", longitude)

combined_coordinates = coordinates_mumbai + coordinates_pune
print("\nCombined coordinates:", combined_coordinates)

print("\nIs 18.5204 present in Location 1?", 18.5204 in coordinates_mumbai)

print("Count of 18.5204:", coordinates_mumbai.count(18.5204))

print("Index of 73.8567:", coordinates_mumbai.index(73.8567))

print("\nTuples are immutable.")
coordinates_mumbai[0] = 20.0000