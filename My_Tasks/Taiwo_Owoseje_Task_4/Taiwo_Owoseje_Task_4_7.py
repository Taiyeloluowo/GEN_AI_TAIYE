# Task 7: List Maniputalation
cityname = ["Jalingo", "Ibadan", "Abeokuta", "Ikeja", "Bobape"]
print(f"{cityname} are the cities on the itinerary, change Abeokuta to any other city of your choice" )
cityname_request = str(input("Enter a city of your choice: "))
cityname.remove("Abeokuta")
cityname.insert(2, cityname_request)
cityname.remove("Bobape")
cityname.insert(0, "Abuja")
print(cityname)