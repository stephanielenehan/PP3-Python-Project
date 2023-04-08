import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]



CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('steph_pp3')

# sales = SHEET.worksheet('sales')
# data = sales.get_all_values()
# print(data)
# per the walkthrough video delete these lines of code we used to check our API was working

# our first function : to collect the sales data from the user 

def get_sales_data():
    """
    Get sales figures input from the user
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n") # \n to put an extra line of space under the example data

    data_str = input("Enter your data here:")
    #print(f"The data you provided is {data_str}")

    sales_data = data_str.split(",")
    validate_data(sales_data)

#create a function to validate the data before allowing the rest of the program to continue
#If data is corrupted, it will gove a useful message to our user explaining what's wrong

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings connot be converted into int,
    or if there arn't exactly 6 values.
    """
    print(values)

    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
    

get_sales_data()
# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
