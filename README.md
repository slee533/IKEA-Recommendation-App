# Sunhyung Lee (slee533@asu.edu)
# IKEA Table/Desk Personal Recommendation Survey


This Python project aims to assist users in finding the perfect table or desk based on their preferences. This README file provides detailed information about the project structure, functionality, and how to run it.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [To Run the Program](#to-run-the-program)
6. [Usage](#usage)
7. [Functionality Description](#functionality-description)
8. [CSV File Structure](#csv-file-structure)
9. [Customer Class](#customer-class)
10. [Auto Testing](#auto-testing)

## Introduction
This project utilizes Python's Tkinter library for building the graphical user interface (GUI) and provides personalized table recommendations based on user input. Users are required to answer a set of questions regarding their preferences, such as budget, mood/vibe, and the need for a matching chair.

## Features
- User-friendly GUI developed using Tkinter.
- Validates user inputs for email, age, budget, and selections.
- Provides personalized table recommendations.
- Allows users to update their selections.
- Saves user data to a CSV file for future reference.


## Installation
1. Install the required dependencies using pip:
    ```
    pip install tkinter pillow
    ```
2. Ensure you have Python 3.x installed on your system.

## To run the program
Click the green triangle run icon in the top-right corner of the PyCharm window.
or
```shell
$ python3 IkeaSurvey.py
```

## Usage
1. The GUI window will open, prompting users to answer a series of questions.
2. Fill in your email, age, budget, and select the options that best match your preferences.
3. Click on the "SUBMIT" button to receive a personalized table recommendation.
4. If you need to update your budget/selections, click on the "Update" button and follow the instructions.
5. Exit the application by clicking on the "Exit" button.

## Functionality
1. **Submission of Survey:** Users can submit a survey by providing their email, age, budget, and selecting options that best match their preferences, such as mood/vibe and the need for a matching chair. Upon submission, the data is validated and saved to a CSV file.
2. **Personalized Recommendations:** Based on the user's inputs, including budget and selections, the system generates personalized table recommendations. It utilizes a recommendation algorithm to match user preferences with suitable table options.
3. **Data Validation:** The project ensures that user inputs are properly validated. It checks for valid email formats, numeric age inputs, positive budget values, and ensures that all selection options are chosen.
4. **Update Budget/Selections:** Users have the option to update their budget and selections by entering their email and modifying their preferences. The system updates the user's data in the CSV file accordingly.
5. **GUI Interface:** The graphical user interface provides a user-friendly experience, guiding users through the survey process with clear instructions and interactive elements.
6. **Feedback and Error Handling:** The system provides feedback to users throughout the survey process, informing them of any errors in their inputs and displaying the recommendation once the survey is successfully submitted.
7. **Persistence of Data:** User data is stored in a CSV file, allowing for future reference and analysis. This ensures that users can access their recommendations and update their selections as needed.
8. **Exit Option:** Users can easily exit the application by clicking on the "Exit" button, providing a seamless user experience.

These functionalities collectively enhance the user experience and provide a valuable tool for users seeking personalized recommendations for tables or desks from IKEA.

## CSV File Structure
The project utilizes a CSV file named `survey.csv` to store user data records. Each record in the CSV file consists of the following fields:

- **Email:** The email address provided by the user during the survey submission.
- **Age:** The age of the user provided during the survey submission.
- **Budget:** The budget specified by the user for purchasing a table or desk.
- **Selection:** The selections made by the user during the survey, indicating their preferences for mood/vibe and the need for a matching chair.

Here is an example of how the data records are structured in the `survey.csv` file:

Email,Age,Budget,Selection
ex1@gmail.com,24,123,"Colorful, Yes"


# Class
## Customer Class
The `Customer` class in the `ClassFile.py` module is responsible for managing customer data and performing validation checks on user inputs. This README provides a detailed description of the class, its variables, and methods.

### Variables
- `email`: Stores the email address of the customer.
- `age`: Stores the age of the customer.
- `budget`: Stores the budget specified by the customer.
- `selection`: Stores the selections made by the customer during the survey.

### Methods
#### `__init__(self, email, age, budget, selection)`
- **Description:** Initializes a new instance of the `Customer` class with the provided email, age, budget, and selection.
- **Parameters:**
  - `email`: Email address of the customer.
  - `age`: Age of the customer.
  - `budget`: Budget specified by the customer.
  - `selection`: Selections made by the customer during the survey.

#### `validate_data(email, age, budget, selection) [staticmethod]`
- **Description:** Validates the provided email, age, budget, and selection inputs.
- **Parameters:**
  - `email`: Email address to be validated.
  - `age`: Age value to be validated.
  - `budget`: Budget value to be validated.
  - `selection`: Selections to be validated.
- **Raises:**
  - `ValueError`: If any of the inputs fail validation checks.


#### `save_to_csv(self, filename='survey.csv')`
- **Description:** Saves the customer data to a CSV file.
- **Parameters:**
  - `filename`: Name of the CSV file to which data is saved. Default is 'survey.csv'.


## Auto testing
Run the following command to test the test_accounts.py. There are 6 test cases.
```shell
pytest -v test_class.py
```