#1
# // (ganzzahlige Division): 1 // 2 ergibt 0 (ganzzahlig, Dezimalstellen werden abgeschnitten).
# / (echte Division): 1 / 2 ergibt 0.5 (Gleitkommazahl).

# ** (Exponentiation): 2 ** 3 ergibt 8 (2 hoch 3).
# * (Multiplikation): 2 * 3 ergibt 6 (2 mal 3).


#2
#prompt the user for the number of subjects they have and store it in the variable
num_subjects = int(input("Wie viele Fächer hast du? "))

# initialise the var as 0
sum = 0
average_last_10_years = 2.35
excellent_threshold = 2.0

# for the given amount of times add the grades to the sum variable
for i in range (num_subjects):
    sum += int(input(f"Gib die Note für Fach {i+1} ein: "))

current_average = sum/num_subjects

#calculate the average grade and print the result
print(f"Der Notendurchschnitt ist: {current_average:.2f}")

if current_average < average_last_10_years:
    print("Dein Notendurchschnitt ist besser als der Durchschnitt der letzten 10 Jahre.")
elif current_average > average_last_10_years:
    print("Dein Notendurchschnitt ist schlechter als der Durchschnitt der letzten 10 Jahre.")
else:
    print("Dein Notendurchschnitt ist gleich dem Durchschnitt der letzten 10 Jahre.")

#check if the user qualifies for direct, unlimited employment
if current_average < excellent_threshold:
    print("Mit diesem Notendurchschnitt hast du eine sehr gute Chance auf eine direkte, unbefristete Übernahme!")



#3
#query for the place of residence
residence = input("\nBitte geben Sie Ihren Wohnort ein: ").strip().upper()

#check if the place of residence is "Löhne"
if residence == "BERLIN":

    #additional inputs and processing
    #compares the processed input to the string "ja" - if it's matching, the expression evaluates to True; otherwise, False
    coding_star = input("Kennen Sie die Firma Coding Star? (Ja/Nein): ").strip().upper() == "JA" 
    college = input("Waren Sie im Spreebogenpark? (Ja/Nein): ").strip().upper() == "JA"

    #output the results
    print(f"\n---Ausgabe---\nWohnort: {residence}")
    print(f"Kennen Sie die Firma Coding Star? {'Ja' if coding_star else 'Nein'}")
    print(f"Waren Sie im Spreebogenpark? {'Ja' if college else 'Nein'}\n")
else:
    print("Keine weiteren Fragen.\n")
