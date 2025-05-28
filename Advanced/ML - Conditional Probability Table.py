def main():
    path_to_csv = r"C:\...\Trainingsdaten.csv"
    data = read_data(path_to_csv)
    cpt = create_cpt(data)
    
    print("\n...")
    

def create_cpt(data):
    cpt = {} 
    data_length = len(data)
    conditional_probabilities_dict = {} 
    
    #CSV:
    #Income: 1 = high, 0 = low
    #Age: 1 = young, 0 = old
    #Decision: 1 = Apple, 0 = Android
    
    income_count = {0: 0, 1: 0}
    age_count = {0: 0, 1: 0}
    
    #Bedingte Wahrscheinlichkeitstabelle will look like that
    #(1, 1): {1: 0.2, 0: 0.8},
    #(0, 1): {1: 0.1, 0: 0.9},
    
    #counting how many ppl have 0/1 age and 0/1 income
    #and how many chose An/Apple with X income and X age
    for icnome, age, decision in data:
        income_count[icnome] += 1
        age_count[age] += 1
        #we will get z.B.;
        #    income_count = {0: 35, 1: 33}
        #    age_count = {0: 38, 1: 30}
        key_income_age = (icnome, age)
        if key_income_age not in conditional_probabilities_dict:
            conditional_probabilities_dict[key_income_age] = {0: 0, 1: 0}
        conditional_probabilities_dict[key_income_age][decision] += 1
        
    #sanity check
    total_counted  = 0
    for key, decisions in conditional_probabilities_dict.items():
        checking_sum = sum(decisions.values())
        total_counted  += checking_sum
        print(f"For key {key} we have {checking_sum} ppl")
        
    print(f"data_length == {data_length}")
    print(f"total_counted  ==  {total_counted }")
    
    if total_counted == data_length:
        #count Marginal Probability
        
        print(f"\nIncome counts:\n  High (1): {income_count.get(1, 0)}\n  Low  (0): {income_count.get(0, 0)}")
        print(f"Age counts:\n  Young (1): {age_count.get(1, 0)}\n  Old  (0): {age_count.get(0, 0)}")
        #    income_count = {0: 35, 1: 33}
        #    age_count = {0: 38, 1: 30}
        probability_income = {
            0: round(income_count.get(0, 0) / total_counted, 2), 
            1: round(income_count.get(1, 0) / total_counted, 2)
        }

        probability_age = {
            0: round(age_count.get(0, 0) / total_counted, 2),
            1: round(age_count.get(1, 0) / total_counted, 2)
        }
        print("\nProbability of Income:  ", probability_income)
        print("Probability of Age:  ", probability_age)

        #CPT
        print("Income: 1 = high, 0 = low")
        print("Age: 1 = young, 0 = old")
        print("Decision: 1 = Apple, 0 = Android")
        print(f"conditional_probabilities_dict:  {conditional_probabilities_dict}")

        cpt = {}
        for key_income_age, decision_counts in conditional_probabilities_dict.items():
            total_ppl_for_key = sum(decision_counts.values())
            p_android = decision_counts.get(0, 0) / total_ppl_for_key
            p_apple = decision_counts.get(0, 0) / total_ppl_for_key
        
        
        
    else:
        print(" T_T ")
        return 
    
    return cpt

def read_data(path_to_csv):
    try:
        with open(path_to_csv, 'r', encoding='utf-8') as file:
            next(file)  #skip header
            return [tuple(map(int, line.strip().split(';'))) for line in file]
    except FileNotFoundError:
        print(f"Error: File not found: {path_to_csv}")
        return []
    except ValueError:
        print(f"Error: Could not convert one or more values to integers in {path_to_csv}")
        return []

if __name__ == "__main__":
    main()
