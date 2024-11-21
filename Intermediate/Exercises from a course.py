# // (ganzzahlige Division): 1 // 2 ergibt 0 (ganzzahlig, Dezimalstellen werden abgeschnitten).
# / (echte Division): 1 / 2 ergibt 0.5 (Gleitkommazahl).

# ** (Exponentiation): 2 ** 3 ergibt 8 (2 hoch 3).
# * (Multiplikation): 2 * 3 ergibt 6 (2 mal 3).



# prompt the user for the number of subjects they have and store it in the variable
num_subjects = int(input("Wie viele Fächer hast du? "))
# initialise the var as 0
sum = 0

# for the given amount of times add the grades to the sum variable
for i in range (num_subjects):
    sum += int(input(f"Gib die Note für Fach {i+1} ein: "))

# calculate the average grade and print the result
print(f"Der Notendurchschnitt ist: {sum/num_subjects:.2f}")
