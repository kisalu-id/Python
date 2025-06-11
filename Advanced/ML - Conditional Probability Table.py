import random


def read_data(path_to_csv):
    """
    Read training data from a CSV file and parse it into a list of tuples.

    :param path_to_csv: Path to the CSV file.
    :type path_to_csv: str
    :return: List of tuples (income, age, decision)
    :rtype: list[tuple[int, int, int]]
    """
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



def create_cpt(data):
    """
    Create the Conditional Probability Table (CPT) from the dataset.

    :param data: List of tuples (income, age, decision)
    :type data: list[tuple[int, int, int]]
    :return: Tuple containing CPT, marginal probabilities for income and age
    :rtype: tuple[dict, dict, dict]
    """
    cpt = {} 
    data_length = len(data)
    conditional_probabilities_dict = {} 
    income_count = {0: 0, 1: 0}
    age_count = {0: 0, 1: 0}
    
    #CPT will look like that
    #(1, 1): {0: 0.8, 1: 0.2},
    #(0, 1): {0: 0.9, 1: 0.1},
    
    #counting how many ppl have 0/1 age and 0/1 income
    #and how many chose An/Apple with X income and X age
    for icnome, age, decision in data:
        income_count[icnome] += 1
        age_count[age] += 1
        #    income_count = {0: 35, 1: 33}
        #    age_count = {0: 38, 1: 30}
        key_income_age = (icnome, age)
        
        if key_income_age not in conditional_probabilities_dict:
            conditional_probabilities_dict[key_income_age] = {0: 0, 1: 0}
        conditional_probabilities_dict[key_income_age][decision] += 1
        
    #sanity check
    total_counted = 0
    print("Number of people per group:")
    for key, decisions in conditional_probabilities_dict.items():
        checking_sum = sum(decisions.values())
        total_counted  += checking_sum
        print(f"  For key {key} we have {checking_sum} people")
        
    print(f"Total dataset size: {data_length} people\nTotal counted in groups: {total_counted} people")

    if total_counted == data_length:
        #count Marginal Probability
        print(f"\nIncome Distribution:\n  Low income  (0): {income_count.get(0, 0)} peoplen  High income  (1): {income_count.get(1, 0)} people")
        print(f"Age Distribution:\n  Old  (0): {age_count.get(0, 0)} people\n  Young (1): {age_count.get(1, 0)} people")
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
        print("Probability of Age:     ", probability_age)

        #CPT
        print("\nLegend:")
        print("  Income:   0 = low, 1 = high")
        print("  Age:      0 = old, 1 = young")
        print("  Decision: 0 = Android, 1 = Apple")
        #print(f"\nconditional_probabilities_dict:  {conditional_probabilities_dict}")

        cpt = {}
        for key_income_age, decision_counts in conditional_probabilities_dict.items():
            total_ppl_for_key = sum(decision_counts.values())
            probability_android = round(decision_counts.get(0, 0) / total_ppl_for_key, 2)
            probability_apple = round(decision_counts.get(1, 0) / total_ppl_for_key, 2)
        
            cpt[key_income_age] = {0: probability_android, 1: probability_apple}

        #print(f"cpt:                        {cpt}")
        return cpt, probability_income, probability_age

    else:
        print("total_counted != data_length  ... sad T_T ")
        return



def simple_prediction_with_forward_sampling(cpt, probability_income, probability_age):
    """
    Simulate a prediction using forward sampling from the CPT.
    Randomly selects income and age based on marginal probabilities, 
    and then predicts a decision using the CPT.

    :param cpt: Conditional Probability Table
    :type cpt: dict
    :param probability_income: Marginal probabilities for income
    :type probability_income: dict[int, float]
    :param probability_age: Marginal probabilities for age
    :type probability_age: dict[int, float]
    """
    #chosing between 0 and 1, wehights - there's a 41% chance to pick 0 for income
    income = random.choices([0, 1], weights=[
        probability_income[0], probability_income[1]
    ])[0]
    print(f"\nSampled income: {income} with weights:  {probability_income})")
    
    age = random.choices([0, 1], weights=[
        probability_age[0], probability_age[1]
    ])[0]
    print(f"Sampled age: {age} with weights:  {probability_age})")
    
    decision_probabilities = cpt.get((income, age), None)
    print(f"Decision probabilities for (income = {income}, age = {age}): {decision_probabilities}")
    
    if decision_probabilities is None:
        print("No CPT entry for sampled income/age.")
        return

    print("\nPrediction using forward sampling")
    predict_decision(cpt, income, age)



def predict_decision(cpt, income, age):
    """
    Predict the smartphone decision (Android/Apple) based on income and age.

    :param cpt: Conditional Probability Table
    :type cpt: dict
    :param income: Income level (0 = low, 1 = high)
    :type income: int
    :param age: Age group (0 = old, 1 = young)
    :type age: int
    """
    key = (income, age)
    print(f"Predicting decision for key: {key}")
    try:
        if key not in cpt:
            print("Invalid combination of income and age.")
            return
        decision_probabilities = cpt[key]
        
        if decision_probabilities[0] > decision_probabilities[1]:
            decision_str = "\"Android\""   #Android
        else:
            decision_str = "\"Apple\""   #Apple
        
        income_str = "\"high\"" if income == 1 else "\"low\""
        age_str = "\"young\"" if age == 1 else "\"old\""
        
        print(f"\nDecision for {income_str} income , age {age_str}:  {decision_str}")

    except Exception as e:
        print("Invalid input format. Please enter something like: 1,0")



def probability_age_given_decision(cpt, data, given_age, given_decision):
    """How likely is it that the user is (given_age, e.g.) young, given that they bought (given_decision, e.g.) Android?"""
    #P(age=1 | decision=0) = P(age=1, decision=0) / P(decision=0)
    #prpbability = people_of_given_age_who_bought_Andr / all people who bought Android



def main():
    path_to_csv = r"C:\...\Training_data.csv"
    data = read_data(path_to_csv)
    cpt, probability_income, probability_age = create_cpt(data)
    
    simple_prediction_with_forward_sampling(cpt, probability_income, probability_age)

    print("Input: Income (0=niedrig, 1=hoch), Age (0=alt, 1=jung)")
    input_str = input("Input data (format: income,age) e.g. 1,0:  ")
    income_str, age_str = input_str.strip().split(',')
    income = int(income_str)
    age = int(age_str)
    predict_decision(cpt, income, age)
    
    probability_age_given_decision(cpt, data, given_age = 0, given_decision = 0)



if __name__ == "__main__":
    main()
