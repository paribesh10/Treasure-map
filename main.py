row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

first_number = int(position[0])
second_number = int(position[1])

map[second_number - 1][first_number - 1] = "📦"

print(f"{row1}\n{row2}\n{row3}")





