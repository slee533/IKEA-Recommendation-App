from os import path
import csv
import re

customer_data = {}

# CSV File
if not path.isfile('survey.csv'):
    with open('survey.csv', 'w') as fp:
        data = csv.writer(fp)
        data.writerow(['Email', 'Age', 'Budget', 'Selection'])


class Customer:
    def __init__(self, email, age, budget, selection):
        self.email = email
        self.age = age
        self.budget = budget
        self.selection = selection

    @staticmethod
    def validate_data(email, age, budget, selection):
        # Validate email format
        if not email:
            raise ValueError("Email cannot be empty. ")
        else:
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if re.fullmatch(regex, email):
                pass
            else:
                raise ValueError("Invalid email format. ")
        # Validate age
        if not age:
            raise ValueError("Age cannot be empty. ")
        elif not age.isdigit():
            raise ValueError("Age must be a integer.")
        elif int(age) < 13:
            raise ValueError("You must be older than 13 to get recommendations.")
        # Validate Budget
        if not budget:
            raise ValueError("Budget cannot be empty. ")
        else:
            try:
                budget_float = float(budget)
                if budget_float <= 0:
                    raise ValueError("Budget needs to be greater than $0.")
            except ValueError:
                raise ValueError("Budget must be a numeric value.")

        # Validate selections
        non_empty_selections = [s for s in selection if s.strip()]
        if not selection or len(non_empty_selections) != 2:
            raise ValueError("Select each option for every questions. ")

    # Save data
    def save_to_csv(self, filename='survey.csv'):
        with open(filename, 'a', newline='') as csvfile:
            fieldnames = ['Email', 'Age', 'Budget', 'Selection']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write customer data
            writer.writerow({'Email': self.email, 'Age': self.age, 'Budget': self.budget,
                             'Selection': ', '.join(self.selection)})
