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


def weekly_sales_input():
    """
    This function asks the user for the weekly sales
    per product, in a specific order.
    """
    print("Please enter your weekly sales figures for each product in the order below:")
    print("Shampoo, Conditioner, Styling Gel, Hair Oil, Mousse, Combs, Brushes and Hair Accessories\n")
    print("If you had no sales for that product in the week, please type 0\n")
    print("Data should be 8 numbers, separated by commas")
    print("For example: 8,11,3,16,0,29,7,4\n")

    data_string = input("Enter your numbers here: \n")
    print(f"The data provided is {data_string}")

weekly_sales_input()