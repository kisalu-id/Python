import sys


#validate a positive integer input
def prompt_positive_int(prompt, max_value=120):
    try:
        value = int(input(prompt))
        if value > 0 and (max_value is None or value <= max_value):
            return value
        #it's possible to perform if/else statements inside the placeholders using F-Strings
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
        name = input("Bitte geben Sie Ihren Vornamen ein: ").strip()
        surname = input("Bitte geben Sie Ihren Nachnamen ein: ").strip()
        age = prompt_positive_int("Wie alt sind Sie? ", 150)

        #write the output from user-given information
        print("\n\nIhre Persönliche Daten:")
        print(f"Name und Nachname: {name.capitalize()} {surname.capitalize()}")
        print(f"Wohnort: {residence.capitalize()}")
        print(f"Alter: {age} Jahre")

        age_format = "Ihr Alter in Binär: {:b}\nIhr Alter in Oktal: {:o}\nIhr Alter in Hexadezimal: {:x}"
        print(age_format.format(age, age, age))

        #instead of
        #print(f"Ihr Alter in Binär: {age:b}\nIhr Alter in Oktal: {age:o}\nIhr Alter in Hexadezimal: {age:x}")

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


def fibonacci(first, second):
    third = first + second
    try:
        txt_path = r"C:\Users\FolderName"
        file_name = "Fibonacci.txt"
        print(f"- {third}")
        third = first + second

        if third < 50:
            print(third)
            file_path = os.path.join(txt_path, file_name)

            if os.path.exists(file_path):
                with open(file_path, 'a') as f:
                    f.writelines(f"{third}\n")
            else:
                with open(file_path, 'w') as f:
                    f.writelines(f"{first}\n{second}\n{third}\n")

            fibonacci(second, third) #recursion

    except FileNotFoundError:
        print(f"Die Datei {file_path} wurde nicht gefunden.")
    except IOError as e:
        print(f"Ein Fehler trat beim Schreiben in die Datei auf: {e}")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")


def prime_nums(i, divisor, limit):
    if i > limit:
        return

    if i < 2: #is will not happen bc i pass "2" as a value for i, but just in case
        prime_nums(i + 1, 2, limit) 
        pass

    if i == divisor:
        print(i)
        try:
            txt_path = r"C:\Users\FolderName"
            file_name = "Prime numbers.txt"
            file_path = os.path.join(txt_path, file_name)

            if os.path.exists(file_path):
                with open(file_path, 'a') as f:
                    f.writelines(f"{i}\n")
            else:
                with open(file_path, 'w') as f:
                    f.writelines(f"Prime numbers:\n{i}\n")
        except FileNotFoundError:
            print(f"Die Datei {file_path} wurde nicht gefunden.")
        except IOError as e:
            print(f"Ein Fehler trat beim Schreiben in die Datei auf: {e}")
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")

        prime_nums(i + 1, 2, limit)

    elif i % divisor == 0:
        prime_nums(i + 1, 2, limit)

    else:
        prime_nums(i, divisor + 1, limit)



#main program
def main():
    while True:
        print("\n---Menü---")
        print("1. Programm 1: Erhebung von persönlichen Daten")
        print("2. Programm 2: Berechnung des Noten")
        print("3. Programm 3: Taschenrechner")
        print("4. Programm 4: Fibonacci")
        print("5. Programm 5: Prime Numbers")
        print("6. Beenden")

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
            print("Sie haben Programm 4 'Fibonacci' ausgewählt.")
            first, second = 0, 1
            print(first)
            print(second)
            fibonacci(first, second)
            
        elif user_input == '5':
            print("Sie haben Programm 5 'Prime Numbers' ausgewählt.")
            prime_nums(2, 2, 50)
            
        elif user_input == '6':
            print("Das Programm wird beendet.")
            sys.exit()
        else:
            print("Ungültige Auswahl. Bitte wählen Sie eine Option von 1 bis 4.")


if __name__ == "__main__":
    main()




# // (ganzzahlige Division): 1 // 2 ergibt 0 (ganzzahlig, Dezimalstellen werden abgeschnitten).
# / (echte Division): 1 / 2 ergibt 0.5 (Gleitkommazahl).

# ** (Exponentiation): 2 ** 3 ergibt 8 (2 hoch 3).
# * (Multiplikation): 2 * 3 ergibt 6 (2 mal 3).


# &=
# bitwise AND between x and 3, then assigns the result to x

# |=
# bitwise OR between x and 3, then assigns the result to x

# ^=
# bitwise XOR between x and 3, then assigns the result to x
# x = 5
# y = 6
# print(f"{x} = {x:b}")
# print(f"{y} = {y:b}\n")
# x ^= y
# print(f"{x} = {x:b}")
# Output:
# 5 = 101
# 6 = 110
# 3 = 11

# >>= (or also <<=)
# right bitwise shift on x by 3 positions, then assigns the result to x
# x = 12
# print(f"{x} = {x:b}")
# x >>= 1
# print(f"{x} = {x:b}")
# Output:
# 12 = 1100 
# 6 = 110

# := (Walrus operator)
# assigns a value to a variable as part of an expression
# Example:
# x = 10
# print(x)
# print(x := 3)
# Output:
# 10
# 3
