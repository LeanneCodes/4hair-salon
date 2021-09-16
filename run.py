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
SHEET = GSPREAD_CLIENT.open('4hair-salon')


def weekly_data_input():
    """
    This function asks the user for the end of week sales and bookings,
    by city, in a specific order. It runs a while loop until the data
    entered is valid and asks the user to confirm the data is correct
    before proceeding with the rest of the program.
    """
    while True:
        print("\nWelcome to the 4Hair Salon National Sales Tracking System!\n")
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
            print("\nData is valid!\n")
            print("Please confirm the data you entered is correct?")
            while True:
                user_confirm = (input("(1)Yes or (2)No \nType the number of your response: \n"))
                if user_confirm == "1":
                    print("\nThe system will proceed...\n")
                    return sales_data, booking_data
                elif user_confirm == "2":
                    print("\nSystem starting again...\n")
                    main()
                    break
                else:
                    print("\nInvalid choice. Options are 1 or 2 only.\n")
            break


def validate_data(value1, value2):
    """
    Inside the try statement, convert all string values into integers.
    Raises ValueError if strings cannot be converted into an int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(value) for value in value1]
        [int(value) for value in value2]
        if len(value1) != 6 or len(value2) != 6:
            raise ValueError(
                f"Exactly 6 values are required for both separated by commas.\nYou provided {len(value1)} and {len(value2)}"
            )
    except ValueError as e:
        print(f"\nInvalid data: {e}, please try again.\n")
        return False

    return True


def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet.
    Updates the relevant worksheet with the data provided.
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")


def calculate_abv(sales_row):
    """
    Compares the sales and completed bookings for each city and
    calculates the average booking value for each booking.
    """
    print("Calculating the average booking value for each city...\n")
    completed_bookings = SHEET.worksheet("CompletedBookings").get_all_values()
    booking_row = completed_bookings[-1]

    abv_data = []
    for sales, bookings in zip(sales_row, booking_row):
        abv = int(sales) / int(bookings)
        abv_data.append(abv)

    return abv_data


def update_abv_worksheet(abv):
    """
    Updates the abv worksheet and appends a new row of data.
    """
    abv_results = SHEET.worksheet("ABV").append_row(abv)
    print("Your average booking value for each city has been updated successfully!\n")

    return abv_results


def get_last_4_entries_abv():
    """
    This function looks at the last 4 average booking values per city.
    """
    abv = SHEET.worksheet("ABV")

    columns = []
    for ind in range(1, 7):
        column = abv.col_values(ind)
        columns.append(column[-4:])
    return columns


def abv_reccos(data):
    """
    Calculates the averages for last 4 average booking values for
    each city. Depending on the performance, recommendations
    are suggested to help improve performance.
    """
    print("Recommendations to improve average booking value per city are below, if any...\n")

    abv_value = []
    for column in data:
        float_column = [float(num) for num in column]
        average = sum(float_column) / len(float_column)
        abv_last_4 = round(average)
        abv_value.append(abv_last_4)

    abv_dict = {
     0: ["London", 70],
     1: ["Bristol", 30],
     2: ["Manchester", 55],
     3: ["Birmingham", 40],
     4: ["Liverpool", 35],
     5: ["Nottingham", 50]
    }

    for key, value in abv_dict.items():
        print(f"{value[0]}'s Regional ABV Target is {value[1]} and your latest ABV is currently at {abv_value[key]}.")
        if abv_value[key] < (0.1 * value[1]):
            print("This location is severely underperforming.\nTry offering more add-on services, such as:\n1. Trimming Services\n2. Hair/Root Colouring\n3. Highlights\n4. Balayage/Foilayage\n5. Blowout\n6. Bridal Hair\n7. 4Hair's Luxury Hair Care Kits\n")
        elif abv_value[key] < (0.3 * value[1]):
            print("Your average booking value for this location is dangerously low.\nTry upselling your clients with services that are in the £25-£40 range.\n")
        elif abv_value[key] < (0.5 * value[1]):
            print("This location is more than 50% under target.\nEncourage clients to trial the latest hairstyle trends that are £30+.\n")
        elif abv_value[key] < (0.7 * value[1]):
            print("This city's salon is currently falling behind.\nAim to sell 4Hair's luxury hair care kits to each client to exceed targets.\n")
        elif abv_value[key] < (0.95 * value[1]):
            print("So close to target, but not quite there yet.\nEncourage clients to buy the hair oil serums and masks after every appointment.\n")
        elif abv_value[key] <= (0.99 * value[1]):
            print("This salon is doing really well.\nIncentivise employees with 45% off £50+ treatments for themselves or family, only if they exceed target next week.\n")
        elif abv_value[key] > value[1]:
            print("Congratulations! This city is smashing target goals. Keep it up!\n")
        else:
            print("This salon is meeting target.\nHowever, aim to increase the salon's ABV to prevent falling behind.\n")

    print("To get access to the 4Hair Salon Google workbook, please copy this link here:\nhttps://bit.ly/4hair-salon")

    return abv_value


def main():
    """
    Here lies all the program functions
    """
    data = weekly_data_input()
    if data:
        sales_data = data[0]
        update_worksheet(sales_data, "Sales")
        booking_data = data[1]
        update_worksheet(booking_data, "CompletedBookings")
        new_abv_data = calculate_abv(sales_data)
        update_abv_worksheet(new_abv_data)
        abv_columns = get_last_4_entries_abv()
        abv_reccos(abv_columns)


main()
