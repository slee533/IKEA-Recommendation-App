from ClassFile import Customer

def test_valid_data():
    print('Test Case 1: Valid data')
    email = "example@example.com"
    age = "20"
    budget = "1000"
    selection = ["Option1", "Option2"]
    customer = Customer(email, age, budget, selection)
    assert customer.email == email
    assert customer.age == age
    assert customer.budget == budget
    assert customer.selection == selection

def test_invalid_email():
    print('Test Case 2: Invalid email')
    email = "invalid_email"
    age = "20"
    budget = "1000"
    selection = ["Option1", "Option2"]
    try:
        Customer(email, age, budget, selection)
    except ValueError as e:
        assert str(e) == "Invalid email format. "

def test_invalid_age():
    print('Test Case 3: Invalid age')
    email = "example@example.com"
    age = "abc"  # Invalid age (not a number)
    budget = "1000"
    selection = ["Option1", "Option2"]
    try:
        Customer(email, age, budget, selection)
    except ValueError as e:
        assert str(e) == "Age must be a numeric value."

def test_invalid_budget():
    print('Test Case 4: Invalid budget')
    email = "example@example.com"
    age = "20"
    budget = "invalid_budget"  # Invalid budget (not a number)
    selection = ["Option1", "Option2"]
    try:
        Customer(email, age, budget, selection)
    except ValueError as e:
        assert str(e) == "Budget must be a numeric value."

def test_invalid_selection():
    print('Test Case 5: Invalid selection')
    email = "example@example.com"
    age = "20"
    budget = "1000"
    selection = ["Option1"]  # Invalid selection (not enough options)
    try:
        Customer(email, age, budget, selection)
    except ValueError as e:
        assert str(e) == "Select each option for every questions. "

