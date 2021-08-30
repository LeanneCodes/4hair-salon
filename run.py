import gspread
from google.oauth2.service_account import Credentials
import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('4hair-salon')


def weekly_data_input():
    """
    This function asks the user for the weekly sales and bookings,
    by city, in a specific order.
    """
    print("Welcome to the 4Hair Salon Regional Sales Tracking System!\n")
    print("Please enter your weekly sales figures for each city in the order below:")
    print("London, Bristol, Manchester, Birmingham, Liverpool and Nottingham\n")
    print("Data should be 6 numbers, separated by commas")
    print("For example: 1000,250,3456,780,90,0\n")
    sales_string = input("Enter your numbers here: \n")
    print("\nNow enter your completed bookings by city")
    booking_string = input("Enter your numbers here: \n")

    sales_data = sales_string.split(",")
    booking_data = booking_string.split(",")

    validate_data(sales_data,booking_data)
    

def validate_data(value1,value2):
    """
    Inside the try statement, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values
    """
    try:
        if len(value1) != 6 or len(value2) != 6:
            raise ValueError(
                f"Exactly 6 values are required for both, you provided {len(value1)} and {len(value2)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True
    

weekly_data_input()