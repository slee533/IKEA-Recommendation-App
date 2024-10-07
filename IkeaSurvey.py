from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import csv

from ClassFile import Customer
from Recommendations import recommendations

ikea_yellow = "#FBDA0C"
ikea_blue = "#0057AD"
customer_list = []


# Function to handle submission of survey
def submit_survey():
    email = email_entry.get()
    age = age_entry.get()
    budget = budget_entry.get()
    selections = [var.get() for var in vars_list]

    # Validating inputs
    try:
        Customer.validate_data(email, age, budget, selections)
    except ValueError as error:
        result_label.config(text=str(error))
        return

    # Checking if email already exists in the data file
    with open('survey.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Email'] == email:
                result_label.config(text="Email already exists. ")
                return

    # Save data to csv file
    customer_data = Customer(email, age, budget, selections)
    customer_list.append(customer_data)
    customer_data.save_to_csv()
    #Printing recommendation
    recommendation = get_recommendation()
    result_label.config(text=f"Survey saved for {email}. ")
    result()


# Function to get recommendation based on user's selections
def get_recommendation():
    try:
        budget = float(budget_entry.get())
    except ValueError:
        return "Invalid budget input. Please enter a numeric value."

    budget_range = f">${150}" if budget < 150 else f"$150+"
    #getting recommendations
    selections = [budget_range]
    selections.extend([var.get() for var in vars_list])
    return recommendations.get(tuple(selections), "No recommendation found")


# Update budget/selection by existing email
def update_selection():
    with open('survey.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        customer_data = list(reader)
        search_email = email_entry.get().strip()
        budget = budget_entry.get()
        new_selections = [var.get() for var in vars_list]

        found = False
        for customer in customer_data:
            if 'Email' in customer and customer['Email'] == search_email:
                try:
                    Customer.validate_data(search_email, customer['Age'], budget, new_selections)
                except ValueError as error:
                    result_label.config(text=str(error))
                    return

                customer['Budget'] = budget
                customer['Selection'] = ', '.join(new_selections)
                found = True
                break
    if found:
        # Save the updated data back to the CSV file
        with open('survey.csv', 'w', newline='') as csvfile:
            fieldnames = customer_data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for customer in customer_data:
                writer.writerow(customer)
        result_label.config(text="Budget/Selections updated. ")

        result()

    if not found:
        result_label.config(text="Email not found. Re-enter email or submit a new survey.")


def result():
    # Create a pop-up window for printing recommendation
    pop_up_win = Tk()
    pop_up_win.title("Your recommendation ")
    pop_up_win.geometry('350x120')
    pop_up_win.columnconfigure(0, weight=1)
    pop_up_win.config(bg='floralwhite')

    # Recommendation: Result of the survey
    recommendation_label = Label(pop_up_win, text=get_recommendation(),fg=ikea_blue, bg="floralwhite", wraplength=250)
    recommendation_label.pack()

    # Ok button for closing
    ok_button = Button(pop_up_win, text="Ok", command=lambda: close(pop_up_win))
    ok_button.pack(pady=15)


def close(window):
    window.destroy()


# Main Window
win = Tk()
win.title('IKEA: Table Personal Recommendation')
win.geometry('550x685')
win.columnconfigure(0, weight=1)
win.config(bg='floralwhite')

# Resizing image to fit the Canvas
logo = Image.open('ikea.png')
new_width = 200
new_height = 90
img = logo.resize((new_width, new_height), Image.LANCZOS)
img.save('ikea.png')
logo = ImageTk.PhotoImage(img)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.pack()


# Title labels
greeting_label = Label(win, text="Hej, we'll do the work for you!",
                       font=("Comic Sans MS", 13), fg=ikea_yellow, bg=ikea_blue)
greeting_label.pack()
instruction_label = Label(win, text="Answer these questions to get your personal recommendation for table/desk.",
                          font=("Comic Sans MS", 11), fg=ikea_yellow, bg=ikea_blue)
instruction_label.pack()

# Frame for email, age, comment, and budget
frame1 = Frame(win)
frame1.pack(anchor='w', padx=8, pady=13)
frame2 = Frame(win)
frame2.pack(anchor='w', padx=8, pady=6)
frame_comment = Frame(win)
frame_comment.pack(anchor='w', padx=8, pady=6)
frame3 = Frame(win)
frame3.pack(anchor='w', padx=8, pady=6)

# Email label
email_label = Label(frame1, text="Enter your email: ", fg=ikea_blue)
email_label.pack(side='left', pady=4)
email_entry = Entry(frame1, width=27)
email_entry.pack(side='left')

# Age label
age_label = Label(frame2, text="Enter your age: ", fg=ikea_blue)
age_label.pack(side='left', pady=4)
age_entry = Entry(frame2, width=28)
age_entry.pack(side='left')

# Comment label
comment_label = Label(frame_comment, text="* Enter and select the best options that fit your idea.", fg=ikea_blue, bg="floralwhite")
comment_label.config(font=("Comic Sans MS", 8, "underline"))
comment_label.pack(anchor='w')

# Budget label
budget_label = Label(frame3, text="What's your budget?  $", fg=ikea_blue)
budget_label.pack(side='left', pady=4)
budget_entry = Entry(frame3, width=22)
budget_entry.pack(side='left')


# RadioButton
questions = {
    "Q1: What is the mood/vibe you are looking for? ": ["Office", "Outdoor", "Colorful", "Earthy", "for Kids"],
    "Q2: Do you need a matching chair with the table/desk? ": ["Yes", "No"]}

# Create variables to store user selections
vars_list = []
for question, options in questions.items():
    label = Label(win, text=question, fg=ikea_blue, bg="floralwhite", font=("Comic Sans MS", 11))
    label.pack(anchor=W, padx=8, pady=9)
    var = StringVar(win)
    for option in options:
        style = ttk.Style(win)
        style.configure('TRadiobutton', background='floralwhite',
                        foreground=ikea_blue, font=("Comic Sans MS", 10))
        radio_button = ttk.Radiobutton(win, text=option, variable=var, value=option)
        radio_button.pack(anchor=W, padx=20)
    vars_list.append(var)


# Frame for finishing buttons
frame4 = Frame(win, background='floralwhite')
frame4.pack(pady=15)
# Update button
update_button = Button(frame4, text="Update", command=update_selection, background=ikea_blue, fg=ikea_yellow)
update_button.pack(side='left')
# Submit button
submit_button = Button(frame4, text="SUBMIT", command=submit_survey, background=ikea_blue, fg=ikea_yellow)
submit_button.pack(side='left', padx=40)
# Exit button
exit_button = Button(frame4, text='Exit', command=lambda: close(win))
exit_button.pack(side='left')


# Label to display recommendation
result_label = Label(win, text="", font=("Comic Sans MS", 11), bg="floralwhite", fg='firebrick')
result_label.pack()

win.mainloop()