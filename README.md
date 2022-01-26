# 4Hair Salon

<p align=center>The 4Hair Salon Performance Tracker</p>

This system grants user input and displays recommendations on what each salon should do to improve their average booking value. This provides visibility on each salon’s performance and be able to make top-level decisions from an objective point-of-view. 

![4hair-salon-logo-and-mockup](https://user-images.githubusercontent.com/81588887/133580235-1b66edf9-ef83-4954-92dc-60f27bbf4d93.png)

4Hair Salon App [link](https://fourhair-salon.herokuapp.com/)

## User Experience

### User Story

There are 6 salons under the 4Hair Salon franchise. One in London, Bristol, Manchester, Birmingham, Liverpool and Nottingham. Each salon has their own Sales Manager that monitors the salon’s performance, and these managers report into the National Director of Sales.

The National Director of Sales (NDoS) for 4Hair Salon, wants to have visibility on how each salon is performing and what they can do to improve performance. 

While the volume of sales is important, the NDoS wants to maximise the value each client brings to the salon. For example, if one client has a hair treatment that costs £20 and another that costs £50, the NDoS wants to maximise on each client spending £50 in the salon, thus increasing the booking/appointment value. 

One of 4Hair Salon’s business objectives is to maximise the average booking value (ABV) for each salon, by meeting the salons' target every week. This will not only maintain sales at a healthy level but encourage the clientele to spend more.

Each salon has different targets, as the cost of rent and other overhead bills range in each city. Therefore, some salons will need to work harder to stay afloat and the NDoS will need some guidance on what actions each salon should take on to meet their target.

### Summary

The NDoS would like to be able to -
1.	Input sales for each city
2.	Input completed bookings for each city
3.	Check if data inputted is correct and valid
4.	Receive recommendations based on data input
5.	Upload data inputted into a Google Sheet
6.	Have access to the Google Sheet

## Project Flowchart

The below flowchart shows the order in which actions are taken and how the program works.

![4hair-salon-flowchart-png](https://user-images.githubusercontent.com/81588887/133585502-5ac1d964-2922-41e1-954f-39c592b5a62f.png)

## Features

### Introductory Message and Sales Input

When the user runs the system, they will be greeted with an opening message and their first set of instructions. The NDoS will need to enter in the salons' sales figures for each city in a specific order, which need to be separated by a comma. No need for spaces or pound signs. An example of how the data should be entered is given.

![image](https://user-images.githubusercontent.com/81588887/133588088-c4962ecf-1f3e-4150-9cb7-08fa89ac4447.png)
![image](https://user-images.githubusercontent.com/81588887/133590157-1530b987-3ab4-4d08-8338-e0fb233d39fc.png)

### Completed Bookings Input

Once the NDoS has inputted the sales figures, they will be prompted to enter the completed bookings for each city, in the same order. This is so the system can calculate what the average booking value is for each city.

![image](https://user-images.githubusercontent.com/81588887/133588595-c8e7e54e-7f1f-48d1-87cf-6e2a1e623591.png)
![image](https://user-images.githubusercontent.com/81588887/133590208-16277512-13af-4150-a11a-7dfe0f2c38bd.png)

### Data Validation

If the data is valid, the NDoS will be notified with the below image. The data will only be classified as valid, if both the sales and completed booking inputs are 6 figures each, separated by commas.

![image](https://user-images.githubusercontent.com/81588887/133589477-57f68ea0-4d6c-4150-800d-6d5abff0ccf1.png)

### Confirming User Input Is Correct

Although the system informs the user that the data they inputted was valid, it doesn't necessarily mean the data is correct. At this point, the system gives the user a chance to check the data inputted for sales and completed bookings is correct before progressing. If the data is correct, the user will confirm by typing in "1". If not correct, the user will need to type in "2".

<img width="434" alt="data-is-valid" src="https://user-images.githubusercontent.com/81588887/151193697-f760744b-24ee-4821-85b9-180b0504a37a.png">

### System Updating Relevant Google Worksheets

Now that the NDoS confirmed the data is correct, the system will show statements that the calculations are happening in the background and that each relevant Google worksheet is being updated successfully.

![image](https://user-images.githubusercontent.com/81588887/133591140-422068db-11f5-4793-8e43-a1c7cc3bb8c7.png)

### Recommendations Based on Data Inputted

The system now tells the user what the current target is for each city, the current average booking value (ABV) is and what recommendations, if any, need to be taken to improve the salons performance. 

![image](https://user-images.githubusercontent.com/81588887/133591987-b2b715ee-20fe-4e02-9ee1-10d02f5dc000.png)

Recommendations are based on how far away the salon's average booking value is away from target.

<details>
 <summary>7 Recommendation Print Statements</summary>

If the city is more 90% away from target, they will receive this message: 
"This location is severely underperforming. Try offering more add-on services, such as:
 1. Trimming Services
 2. Hair/Root Colouring
 3. Highlights
 4. Balayage/Foilayage
 5. Blowout
 6. Bridal Hair
 7. 4Hair's Luxury Hair Care Kits"

If the city is more 70% away from target, they will receive this message: 
"Your average booking value for this location is dangerously low. Try upselling your clients with services that are in the £25-£40 range."

If the city is more 50% away from target, they will receive this message:
"This location is more than 50% under target. Encourage clients to trial the latest hairstyle trends that are £30+."

If the city is more 30% away from target, they will receive this message:
"This city's salon is currently falling behind. Aim to sell 4Hair's luxury hair care kits to each client to exceed targets."

If the city is more 5% away from target, they will receive this message:
"So close to target, but not quite there yet. Encourage clients to buy the hair oil serums and masks after every appointment."

If the city is more 1% away from target, they will receive this message:
"This salon is doing really well. Incentivise employees with 45% off £50+ treatments for themselves or family, only if they exceed target next week."

If the city is meeting target, they will receive this message:
"This salon is meeting target. However, aim to increase the salon's ABV to prevent falling behind."

And if the city is exceeding target, they will receive this message:
"Congratulations! This city is smashing target goals. Keep it up!"
</details>

### Reviewing 4Hair Salon Google Worksheet

Now the NDoS has reviewed the recommendations outputted from the system, they can review the latest data on the Google worksheet via a link. Heroku doesn't allow hyperlinks, so the user is instructed to copy the link. Which they can then open in a new tab.

![image](https://user-images.githubusercontent.com/81588887/133594840-810907da-5ccb-4887-a295-6549c1871ef0.png)

## 4Hair Salon Google Worksheet View

This worksheet is read-only for users who don't have the permissions to edit the file. Only the NDoS and senior management have access to edit the file. This is to limit the number of accidental changes made to the worksheet. 

### Sales Worksheet

The "Sales" worksheet displays historic data inputted and the most recent data the NDoS supplied.

![image](https://user-images.githubusercontent.com/81588887/133601117-5745cc2a-4880-49e8-99bc-c26016b7530f.png)

### Completed Bookings Worksheet

The "CompletedBookings" worksheet displays historic data inputted and the most recent data the NDoS supplied.

![image](https://user-images.githubusercontent.com/81588887/133601173-5d83bc0f-e463-4929-916e-a25666c14c9e.png)

### ABV Worksheet

The "ABV" worksheet displays the calculation between the total sales for each city divided by the number of completed bookings for each city. The final ABV figure is rounded down, so the data is easier to digest and understood clearly.

Additionally, the figures in each column are colour formatted based on whether they meet the city's target or not. The city's target is labelled in the column header. If the figure is below the city's target, it's highlighted in a pale orange, if it's meeting or above the city's target, then no highlighting is applied.

This allows the NDoS and other users to see which salons are consistently underperforming.

![image](https://user-images.githubusercontent.com/81588887/133601525-0aae546a-8b20-40b5-bf3b-7d669509a235.png)

## Future Features

1. Allow the user to add a new salon and append sales and completed bookings data to it
2. Allow the user to remove a salon from the list

## Testing

To ensure there were no bugs in the interface and that the system could handle incorrect user input. Many tests were conducted to cover all bases.

<details>
 <summary>View tests conducted</summary>

### Ensuring Data is Valid

To ensure the worksheet is updated with right number of figures, it is requested that the user inputs 6 figures for both sales and completed bookings. Even if the sales for that week were zero.

If the user does not enter in 6 figures for either input, the below error message will flag and ask the user to try again.
![invalid-data](https://user-images.githubusercontent.com/81588887/151200287-2a0e68a3-e37d-42cc-9cd0-d800a4e9c6cc.png)

If the user enters any data that is not 6 figures separated by a comma, this invalid message will appear.
 
This was tested on the following inputs
 * NDoS inputs a word, instead of a number (cat)
 ![word](https://user-images.githubusercontent.com/81588887/151200340-a6efc626-fbe9-4028-a83c-165464d6fc5d.png)
 * NDoS inputs a keyboard key (?)
 ![character-key](https://user-images.githubusercontent.com/81588887/151200377-51ad1e4e-b4f3-4fc9-a3c0-351a2e2eba0b.png)
 * NDoS presses the enter key
 ![enter](https://user-images.githubusercontent.com/81588887/151200415-cfca2dcc-4c21-4ab0-abbc-c4264be73e90.png)
 * NDoS does not use commas when inputting data
 ![commas](https://user-images.githubusercontent.com/81588887/151200547-bff2619e-de43-4231-888f-3b93bc8dc965.png)

### Confirming Data is Correct

To prevent the workflow from breaking, the system will keep asking the user to confirm the data is correct. This will be done by entering either 1 for yes or 2 for no. If the user inputs another number, letter, presses the enter key or any other key, the system will ask the same question until it gets a valid answer of either 1 or 2.

* NDoS inputs a number (3)
 ![three](https://user-images.githubusercontent.com/81588887/151201844-44121be8-2f27-455a-89cb-2fcecd965e6c.png)
* NDoS inputs a letter (k)
 ![k](https://user-images.githubusercontent.com/81588887/151201929-dfb189e9-83d3-4e0e-bb9a-2de7ce667c2a.png)
* NDoS presses the enter hey
 ![enter-key](https://user-images.githubusercontent.com/81588887/151201952-734fbc05-0447-4189-8ee8-81cf231ec8c8.png)
* NDoS presses a keyboard key (?)
 ![?](https://user-images.githubusercontent.com/81588887/151201975-00e5f918-cfe6-4c90-8a84-38d2fb72167a.png)

If the user is not confident that the data they inputted is correct, they can type in the number 2 and the system will start again, ignoring the previous data inputted.

![start-again](https://user-images.githubusercontent.com/81588887/151202024-65e06451-dd83-405b-9b35-35c4fcc168ef.png)

However, if the data is correct, they can type in 1 and the system will proceed with the remaining functions. 

Additionally, if the user enters the value "0" for sales and has bookings for that city, this could be due bookings/appointments that were 100% discounted. This happens when a salon is treating a celebrity or an influencer and wants to generate positive PR.

If it's the other way round and there is figure for sales but "0" completed bookings, this could be due to clients buying merchandise from the salon without having an appointment/confirmed booking. For example, buying the 4Hair Luxury Kits.
</details>

## Validator Testing

- Passed data through PEP8 and no errors were found
- Heroku works correctly as planned across Google Chrome, Safari, Microsoft Edge and Mozilla Firefox
- Tested the Heroku program on iPhone 11, Google Pixel 2, Motorola Edge and Huawei P9

For user experience purposes, it's best to run the program on a tablet, laptop or desktop, as on mobile it may be too small to read the instructions and recommendations.

## Project Bugs and Solutions

Bugs | Solutions
----------|----------
Double data upload - When the user confirmed the data they previously entered was incorrect, started the system again and then confirmed the new data was correct. The system would upload both sets of data (incorrect and correct) to the Google worksheets. | Moved the "return sales data, booking data" from the last line in the "weekly_data_input()" function and place it on line 43 in the while loop. This meant as soon as the data was confirmed to be correct, previous data inputs were ignored.
Integer User Error - When asking the user to confirm if their data was correct, the user had to type a number. If they typed a letter, a special character or pressed the enter key, the system would break, and the user would be exited from the program. | To handle different character/key inputs, I removed the "int" wrapping from the "user_confirm" string on line 40 and then wrapped the numbers 1 and 2 in quotations, so the program would accept these values as answers.
Sales Data Appearing Twice - When running the program initially, the sales data would appear on the "Sales" and "CompletedBookings" tab in the 4Hair Salon Google Worksheet, despite the user inputting separate completed bookings data. | Used the zip method for the sales and booking data on line 99.
Module Six Error in Heroku - After updating the requirements file and then deploying to Heroku, I was still shown a "Module six error". | After searching on StackOverflow, I found an answer that suggested adding `six == 1.10.0` to the top of the requirements.txt file. Once this was done and changes were committed, the program ran as intended on Heroku
Zero Division Error - When the user entered 0 for completed bookings for at least 1 city, the program would break, given that the calculation later on in the program asked for sales divided by bookings. | To handle this error, I used the following code: ![image](https://user-images.githubusercontent.com/81588887/138554667-64628b30-1daa-49d6-b9fd-fc25f9c41265.png) This allowed me to put a 0 in the Google worksheet and allow the program to continue running the code.

## Google API Setup

The value of using the Google API Sheets library is that it's built on HTTP and JSON, so any standard HTTP client can send requests to it and parse the responses. In other words, our project can feed data to the Google Sheet using an API and we can see the result of that data in a format suitable for Google Sheets. It's also not just used for Python, the Google API client libraies provide better language integration, improved security and support for making calls that require user authorisation. The client libraries are available in a number of programming languages. To get set up with a Google Sheet's API, you will need to select which language your project is for and then following the installation steps online.

The reason for using Google Sheets for this project is so that the NDoS and other permitted users could view past and current data inputted and be able to make insightful, data-driven decisions on what actions they should take for each salon. Using Google Sheets, meant that we could leverage formulas and highlight cells that were not equal to or greater than the city's target ABV. This added ability allows for instant clarity on what city is performing well or not, which the python program alone is not the best way to display such data. Using Google Sheets also allows the NDoS to share the file to the Regional Managers, in a read-only format, so they can understand how their salon is performing against other salons.

Link to the 4Hair Salon Google worksheet [here](https://docs.google.com/spreadsheets/d/1UmPvDmD13JLirGdsC2yTkNROgu0nCe9sanfPp3KKsbw/edit#gid=2144739599)

<details>
 <summary>Setting Up the Google API</summary>

  1. Create a Google account.
  2. Create a Google Sheet and name the file. Preferably matching your GitHub repository name.
  3. Then visit [Google Cloud Platform](https://console.cloud.google.com/)
  4. Make sure you select your personal Google account. This is to prevent other users from changing settings that could impact your final program.
  5. Next to the Google Cloud Platform burger menu, click "Select a project" and then select "New project".
  6. Then give your project a name. Preferably matching your GitHub repository and Google Sheets doc name. Then click "Create".
  7. Then click "Select project" again. But this time select the name of the project you just created.
  8. Now you're on your project dashboard, ensure the side menu/burger menu is open and select "API & Services" and then "Library".
  9. First search for "Google Drive" in the search bar. Click on the API at the top and click "Enable".
  10. Now you will need to create credentials to access the Google Sheets. Click "Create credentials".
  11. In the form, under "Which API are you using?", please select "Google Drive API".
  12. For "What data will you be accessing?", please select "Application Data".
  13. For the "Are you planning to use this API with Compute Engine, Kubernetes Engine, App Engine, or Cloud Functions?" question, please select "No, I'm not using them".
  14. Click "Next", then "Done".
  15. Now enter a Service account name. Preferably matching your Google Cloud project name if available.
  16. Then go to "Grant this service account access to project".
  17. In the Role dropdown box, select "Basic", then "Editor".
  18. Press "Continue".
  19. "Grant users access to this service `account`" can be left blank.
  20. Click "Done".
  21. On the next page, click on the service account that has just been created.
  22. Now click on the "Keys" tab.
  23. Click the "Add Key" dropdown button and select "Create New Key".
  24. Select "JSON" and then click "Create". This will trigger the .json file with your API credentials in it to download to your machine.
  25. Now, click on the main burger menu, select "API & Services" and select "Library".
  26. In the search bar, enter "Google Sheets" and select the "Google Sheets API" option and click "Enable".
</details>

<details>
 <summary>Link your Google API Credentials to Gitpod Workspace</summary>
 
  1. Drag and drop the .json file from your downloads folder into your Gitpod workspace.
  2. Rename the file to "creds.json"
  3. Now open the creds.json file. Locate the "client_email" line and copy the email address next to it, without the quotes.
  4. Then navigate to your Google Sheets file and open the "Share" button.
  5. Paste in the client email address and make sure "Editor" is selected, untick "Notify People" and then click "Share".
</details> 

Given that your `creds.json` file contains sensitive information. Make sure to add this file to your gitignore file, to prevent this data being committed or sent to GitHub.

To check that your `creds.json` file won't be committed, follow the below steps:

  1. In your terminal type `git add .` and press enter.
  2. Now type in `git status` and press enter.
  3. If the `creds.json` file is not listed in the staging area, you are safe to commit your changes.

## Deployment

<details>
 <summary>Heroku Deployment Steps</summary>
 
  1. Make sure all dependencies are listed in your requirements.txt file. To do this, type in your python terminal `pip3 freeze > requirements.txt`.
  2. Now all your requirements will be added to the requirements file.
  3. To prevent any problems with your Heroku program displaying correctly, add `six == 1.10.0` to the top of the requirements file.
  4. Commit this change.
  5. Go to the [Heroku](https://heroku.com/) website and navigate to the sign up button in the top right-hand corner.
  6. Next, click "New" in the top right-hand corner and select "Create new app".
  7. Then choose an app name. It must be unique.
  8. Then select "Europe" as your region.
  9. Click "Create app".
  10. Navigate to the "Settings" tab.
  11. Click on "Config Vars".
  12. For the first "KEY", input "CREDS".
  13. For "VALUE", input your entire creds.json file including the curly braces.
  14. Click "Add".
  15. For the second "KEY", input "PORT".
  16. For the second "PORT", input "8000".
  17. Click "Add".
  18. Scroll down to Buildpacks and select "Add buildpack".
  19. Select Python first and then add another buildpack and select Node JS. Python must be listed above Node JS for this to work.
  20. Scroll back to the top and select the "Deploy" tab.
  21. From Deployment method, select "GitHub".
  22. Now search for your GitHub repository name and select the correct repository.
  23. Now scroll down to Automatic deploys and choose the "main" branch. Therefore, any changes that have been pushed through to GitHub will update the Heroku app.
  24. Then scroll down to Manual deploy and click "Deploy Branch".
  25. When complete, click on "View", which will open a new tab and display your program.
</details>

Please note: Heroku is used to handle back-end languages such as Python. Hence why we need to deploy this work to Heroku in order to help manage and scale this app if need be.

## Technologies Used

- HTML5
- CSS3
- JavaScript
- Python3

## Credits

* Code
  * StackOverflow for the dictionary
  * W3Schools for zipping the sales and booking data
* Acknowledgements
  * My mentor Rahul for his ongoing support and feedback
  * The Code Institute’s Tutor Support
  * The Slack community
