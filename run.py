import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated by commas.
    The loop will repeatedly request data until it is valid.
    """
    while True: 
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n") # \n to put an extra line of space under the example data
        
        data_str = input("Enter your data here:") #print(f"The data you provided is {data_str}")
        
        sales_data = data_str.split(",")
        

#create a function to validate the data before allowing the rest of the program to continue
#If data is corrupted, it will give a message to our user explaining what's wrong
         
        if validate_data(sales_data):
            print("Data is valid")
            break

    return sales_data

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings connot be converted into int,
    or if there arn't exactly 6 values.
    """
    print(values)

    try:
        [int(value) for value in values] #for each individual value 
                                         #in the values list, 
                                         #convert that value into an integer.
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True


def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided.
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")
    
def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type
     - A positive number for surplus means unused stock
     - A negative number for surplus means stock sold out and tells us how many extra were needed
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    print(stock_row)    


def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    calculate_surplus_data(sales_data)



print ("Welcome to Steph_PP3 Data Automation")
main()



# Write your code to expect a terminal of 80 characters wide and 24 rows high
