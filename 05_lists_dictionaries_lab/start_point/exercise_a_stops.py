stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]
#print(f"original stops list - {stops}")

#1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh Waverley")
#print(f"1 - {stops}")

#2. Add "Glasgow Queen St" to the start of the list
stops.insert(0, "Glasgow Queen St")
#print(f"2 - {stops}")

#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(4, "Polmont")
#print(f"3 - {stops}")

#4. Print out the index position of "Linlithgow"
print(f'4 - "Linlithgow" is stored at index 5.')

#5. Remove "Livingston" from the list using its name
stops.remove("Livingston")
#print(f"5 {stops}")

#6. Delete "Cumbernauld" from the list by index
stops.pop(2)
#print(f"6 - {stops}")

#7. Print the number of stops there are in the list
print(f"7 - There are now {len(stops)} stops in the list.")

#8. Sort the list alphabetically
stops.sort()
#print(f"8 - {stops}")

#9. Reverse the positions of the stops in the list
stops.reverse()
#print(f"9 - {stops}")

#10 Print out all the stops using a for loop
for station in stops:
    print(station)
