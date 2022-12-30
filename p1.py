elves = []
calories = []
elf = []

with open("calories.txt") as file:
    for line in file:
        calories_list = [line.strip() for line in file]
        
    for item in calories_list:
        if item != "":
            elf.append(int(item))
        if item == "":
            elves.append(elf)
            elf = []

for elf in elves:
    elf_cal = sum(elf)
    calories.append(elf_cal)
    
calories.sort()
top3 = calories[-1] + calories[-2] + calories[-3]
    
print(top3)