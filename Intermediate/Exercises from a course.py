import sys


#validate a positive integer input
def prompt_positive_int(prompt, max_value=120):
    try:
        value = int(input(prompt))
        if value > 0 and (max_value is None or value <= max_value):
            return value
        print(f"Bitte geben Sie eine gültige Zahl größer als 0{' und kleiner als ' + str(max_value) if max_value else ''}.")
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")


#prompt the user for their personal info and save it in the variables
def get_pesonal_data():
    print("\n---Persönliche Daten---")
    # #query for the place of residence
    residence = input("Bitte geben Sie Ihren Wohnort ein: ").strip().upper()
    #check if the place of residence is "Berlin"
    if residence == "BERLIN":
        name = input("Bitte geben Sie Ihren Vornamen ein: ").strip().upper()
        surname = input("Bitte geben Sie Ihren Nachnamen ein: ").strip().upper()
        age = prompt_positive_int("Wie alt sind Sie? ", 150)

        #write the output from user-given information
        print("\n\nIhre Persönliche Daten:")
        print(f"Name und Nachname: {name} {surname}")
        print(f"Alter: {age} Jahre")
        print(f"Wohnort: {residence}")
    else:
        print("Nur Personen aus Berlin können teilnehmen.")
        

#prompt the user for the number of subjects they have and store it in the variable
def grade_point_average():
    print("\n---Notendurchschnitt---")
    num_subjects = int(input("\nWie viele Fächer hast du? "))

    #initialise the var as 0
    sum = 0
    average_last_10_years = 2.35
    excellent_threshold = 2.0

    #for the given amount of times add the grades to the sum variable
    for i in range (num_subjects):
        try:
            sum += int(input(f"Gib die Note für Fach {i+1} ein: "))
        except ValueError:  
            print("Ungültige Eingabe. Bitte geben Sie eine gültige Note ein.")
            return
        
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


#define reliable chars for calculator()
def safe_evaluation(expr):
    allowed_characters = "0123456789+-*/.()**"
    if all(char in allowed_characters for char in expr):
        try:
            #check the expr
            result = eval(expr)
            return result
        except ZeroDivisionError:
            return "Fehler: Division durch Null ist nicht erlaubt."
        except Exception as e:
            return f"Fehler bei der Auswertung: {e}"
    else:
        return "Ungültige Eingabe. Bitte nur Zahlen und erlaubte Operatoren verwenden."


def calculator():
    print("\n---Taschenrechner---")
    print("Geben Sie einen mathematischen Ausdruck ein (z. B. 2 + 3, 5**2)\noder 'Beenden', um das Programm zu schließen.")
    expr = input("Eingabe: ").strip()

    if expr.strip().lower() == 'beenden':
        print("Das Programm wird beendet.")
        sys.exit()  #exit the program
    else:
        try:
            #safely evaluate the expression
            result = safe_evaluation(expr)
            print(f"Ergebnis: {result}")
        except ZeroDivisionError:
            print("Fehler: Division durch Null ist nicht erlaubt.")
        except Exception as e:
            print(f"Fehler bei der Auswertung: {e}")


#main program
def main():
    while True:
        print("\n---Menü---")
        print("1. Programm 1: Erhebung von persönlichen Daten")
        print("2. Programm 2: Berechnung des Noten")
        print("3. Programm 3: Taschenrechner")
        print("4. Beenden")

        #user-defined input
        user_input = input("Bitte wählen Sie eine Option (1-4): ")

        if user_input == '1':
            print("Sie haben Programm 1 'Erhebung von persönlichen Daten' ausgewählt.")
            get_pesonal_data()

        elif user_input == '2':
            print("Sie haben Programm 2 'Berechnung des Noten' ausgewählt.")
            grade_point_average()

        elif user_input == '3':
            print("Sie haben Programm 3 'Taschenrechner' ausgewählt.")
            calculator()

        elif user_input == '4':
            print("Das Programm wird beendet.")
            sys.exit()
        else:
            print("Ungültige Auswahl. Bitte wählen Sie eine Option von 1 bis 4.")


if __name__ == "__main__":
    main()
