import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
import math

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
    by city, in a specific order. Run a while loop until the data
    entered is valid and asks the user to confirm data is correct
    before proceeding with the rest of the program.
    """
    while True:
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

        if validate_data(sales_data, booking_data):
            print("Data is valid!\n")
            print("Please confirm the data you entered is correct?")
            while True:
                user_confirm = int(input("(1)Yes or (2)No \nType the number of your response: "))
                if user_confirm == 1:
                    print("\nThe system will proceed...\n")
                    break
                elif user_confirm == 2:
                    print("Start again")
                    break
                else:
                    print("Invalid choice. Options are 1 or 2 only.")
            break

    return sales_data, booking_data


def validate_data(value1, value2):
    """
    Inside the try statement, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values
    """
    try:
        [int(value) for value in value1]
        [int(value) for value in value2]
        if len(value1) != 6 or len(value2) != 6:
            raise ValueError(
                f"Exactly 6 values are required for both, you provided {len(value1)} and {len(value2)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided.
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")


def calculate_aov(sales_row):
    """
    Compare the sales and completed bookings for each city and
    calculate the average order value for each booking.
    """
    print("Calculating the average order value for each booking...\n")
    completed_bookings = SHEET.worksheet("CompletedBookings").get_all_values()
    booking_row = completed_bookings[-1]
    
    aov_data = []
    for sales, bookings in zip(sales_row, booking_row):
        aov = int(sales) / int(bookings)
        aov_data.append(aov)
    
    return aov_data


def update_aov_worksheet(aov):
    """
    Updates the AOV worksheet and appends a new row of data.
    """
    aov_results = SHEET.worksheet("AOV").append_row(aov)
    print("Your AOV per booking for each city has been updated successfully!")

    return aov_results


def main():
    """
    Here lies all the program functions
    """
    data = weekly_data_input()
    sales_data = data[0]
    update_worksheet(sales_data, "Sales")
    booking_data = data[1]
    update_worksheet(booking_data, "CompletedBookings")
    new_aov_data = calculate_aov(sales_data)
    update_aov_worksheet(new_aov_data)


main()