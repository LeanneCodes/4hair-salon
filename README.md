# 4Hair Salon

<p align=center>The 4Hair Salon Performance Tracker</p>

This system allows user input and displays recommendations on what each salon should do to improve their average booking value from one system. This provides visibility on each salon’s performance and be able to make top-level decisions from an objective point-of-view. 

![4hair-salon-logo-and-mockup](https://user-images.githubusercontent.com/81588887/133580235-1b66edf9-ef83-4954-92dc-60f27bbf4d93.png)

4Hair Salon App [link](https://fourhair-salon.herokuapp.com/)

## User Experience

### User Story

There are now 6 salons under the 4Hair Salon franchise. One in London, Bristol, Manchester, Birmingham, Liverpool and Nottingham. Each have their own Sales Manager monitoring the salon’s performance. 

A high-ranking employee with the title, National Director of Sales (NDoS) for 4Hair Salon, wants to have visibility on how each salon is performing and what they can do to improve performance. 

While the volume of sales is important, the NDoS wants to maximise the value each client brings to the salon. For example, if one client has a hair treatment that costs £20 and another that costs £50, the NDoS wants to maximise on each client spending £50 in the salon, thus increasing the booking/appointment value. 

One of 4Hair Salon’s business objectives is to maximise the average booking value (ABV) for each salon, by meeting the salon’s target every week. This will not only maintain sales at a healthy level but encourage the clientele to spend more.

Each salon has different targets, as the cost of rent and other overhead bills range in each city. Therefore, some salons will need to work harder to stay afloat and the NDoS will need some guidance on what actions each salon should take on to meet their target.

### Summary

As a user, I would like to be able to -
1.	Input sales for each city
2.	Input completed bookings for each city
3.	Check if data inputted is correct and valid
4.	Receive recommendations based on data input
5.	Upload data inputted into a Google Workbook
6.	Have access to the Google Workbook

## Project Flowchart

The below flowchart shows the order in which actions are taken and how it works.

![4hair-salon-flowchart-png](https://user-images.githubusercontent.com/81588887/133585502-5ac1d964-2922-41e1-954f-39c592b5a62f.png)

## Features

### Introductory Message and Sales Input

When the user runs the system, they will be greeted with an opening message and their first set of instructions. The NDoS will need to enter in the salons' sales figures for each city in a specific order, which need to be separated by a comma. No need for spaces or pound signs. An example of how the data should be entered is given.

![image](https://user-images.githubusercontent.com/81588887/133588088-c4962ecf-1f3e-4150-9cb7-08fa89ac4447.png)
![image](https://user-images.githubusercontent.com/81588887/133590157-1530b987-3ab4-4d08-8338-e0fb233d39fc.png)

### Completed Bookings Input

Once the NDoS has inputted the sales figures, they will be prompted to enter the completed bookings for each city, in the same order. This is done, so the system can calculate what the average booking value is for each city.

![image](https://user-images.githubusercontent.com/81588887/133588595-c8e7e54e-7f1f-48d1-87cf-6e2a1e623591.png)
![image](https://user-images.githubusercontent.com/81588887/133590208-16277512-13af-4150-a11a-7dfe0f2c38bd.png)

### Data Validation

If the data is valid, the NDoS will be notified with the below image. The data will only be classified as valid, if both the sales and completed booking inputs are 6 figures each, separated by commas.

![image](https://user-images.githubusercontent.com/81588887/133589477-57f68ea0-4d6c-4150-800d-6d5abff0ccf1.png)

### Confirming User Input Is Correct

Although the system informs the user that the data they inputted was correct, it doesn't necessarily mean the data is correct. This point in the system gives the user a chance to check the data for the sales and completed bookings is correct before progressing. If the data is correct, the user will confirming by typing in "1". If not correct, the user will need to type "2".

![image](https://user-images.githubusercontent.com/81588887/133590843-289c4d0b-b81a-4372-b99b-fe457d3745ee.png)

### System Updating Relevant Google Worksheets

Now that the NDoS confirmed the data is correct, the system will show statements that the calculations are happening and that each relevant Google worksheet is being updated successfully.

![image](https://user-images.githubusercontent.com/81588887/133591140-422068db-11f5-4793-8e43-a1c7cc3bb8c7.png)

### Recommendations Based on Data Inputted

The system now tells the user what the current target is for each city, what their current average booking value (ABV) is and what recommendations, if any, need to be taken to improve salon's performance. 

![image](https://user-images.githubusercontent.com/81588887/133591987-b2b715ee-20fe-4e02-9ee1-10d02f5dc000.png)

Recommendations are based on how far away the city's salon is away from their own target.

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

### Reviewing 4Hair Salon Google Workbook

Now the NDoS has reviewed the recommendations outputted from the system, they can review the latest data they entered and the ABV on the Google workbook via a link. Heroku doesn't allow hyperlinks, so the user is instructed to copy the link. Which they can then open the link in a new tab.

![image](https://user-images.githubusercontent.com/81588887/133594840-810907da-5ccb-4887-a295-6549c1871ef0.png)

## 4Hair Salon Google Workbook View

This workbook is read-only for users who haven't been granted permisison to edit the file. Only the NDoS and senior management have access to edit the file. This is to limit the number of accidental changes made to the workbook.

### Sales Worksheet

The "Sales" worksheet displays historic data inputted and the most recent data the NDoS supplied.

![image](https://user-images.githubusercontent.com/81588887/133601117-5745cc2a-4880-49e8-99bc-c26016b7530f.png)

### Completed Bookings Worksheet

The "CompletedBookings" worksheet displays historic data inputted and the most recent data the NDoS supplied.

![image](https://user-images.githubusercontent.com/81588887/133601173-5d83bc0f-e463-4929-916e-a25666c14c9e.png)

### ABV Worksheet

The "ABV" worksheet displays the calculation between the total sales for each city divided by the number of completed bookings for each city. The final ABV figure is rounded down, so the data is easier to digest and understand clearly.

Additionally, the figures in each column are formatted based on whether they meet the city's target or not. The city's target is labelled in the column header. If the figure is below the city's target, it's highlighted in a pale orange, if it's meeting or above the city's target, then no highlighting is applied.

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

To ensure the workbook is updated with right number of figures, it is requested that the user inputs 6 figures for both sales and completed bookings. Even if the sales for that week is zero.

If the user does not enter in 6 figures for either input, the below error message will flag and ask the user to try again.

![image](https://user-images.githubusercontent.com/81588887/133613385-25ab149d-e8f8-42a3-bf7d-46534b6d8ecf.png)

If the user enters any data that is not a number, the system will call this out.

![image](https://user-images.githubusercontent.com/81588887/133613655-14131e87-8049-4145-82f9-07b3b8bdd358.png) User enters "cat" in the sales input
![image](https://user-images.githubusercontent.com/81588887/133613721-1bc102a4-6395-4d45-a650-8949de2973e4.png) User enters "dog" in the booking input
![image](https://user-images.githubusercontent.com/81588887/133613918-cc4fef71-7ce1-42bc-a5c7-ab325a6b7cdf.png) User presses the enter key in the sales input
![image](https://user-images.githubusercontent.com/81588887/133614776-969953ae-26ee-4f46-9b76-c20d5e43abd3.png) The user does not use commas when inputting data

### Confirming Data is Correct

To prevent the workflow from breaking, the system will keep asking the user to confirm the data is correct, by entering either 1 for yes or 2 for no. If the user inputs another number, letter, presses enter or any other key, the system will ask the same question until it gets a valid answer of either 1 or 2.

![image](https://user-images.githubusercontent.com/81588887/133612180-fc1d858e-5973-4a6d-befd-50b6004be80e.png)
User inputs the value of 3

![image](https://user-images.githubusercontent.com/81588887/133612268-c46f6660-24a5-460f-80ec-4393cb954140.png)
User then inputs the letter k

![image](https://user-images.githubusercontent.com/81588887/133612420-d96d77d0-e5a1-4eac-8897-25c74987ad93.png)
The user presses the enter key

If the user is not confident that the data they inputted is correct, they inputted the number 2 and the system starts again, ignoring the previous data inputted.

![image](https://user-images.githubusercontent.com/81588887/133612733-fe6dc000-51f2-4805-834a-4683b43dd02f.png)

However, if the data is correct, they can type in 1 and the system will proceed with the remaining functions. 

Additionally, if the the user enters the value "0" for sales and has bookings for that city, this could be due bookings/appointments that were 100% discounted. This happens when a salon is treating a celebrity or an influencer and wants to generate positive PR.

If it's the other way round and there is figure for sales but 0 completed bookings, this could be due to clients buying merchandise from the salon without having an appointment/confirmed booking. For example, buying the 4Hair Luxury Kits.
</details>

## Validator Testing

- Passed data through PEP8 and no errors were found
- Heroku works correctly as planned across Google Chrome, Safari, Microsoft Edge and Mozilla Firefox
- Tested the Heroku program on iPhone 11, Google Pixel 2, Motorola Edge and Huawei P9

For user experience purposes, it's best to run the program on a tablet, laptop or desktop, as on mobile it may be too small to read the instructions and recommendations.

## Deployment

<details>
 <summary>GitHub Deployment Steps</summary>
 
1. In the GitHub repository, navigate to the Settings tab
2. Scroll down to GitHub pages and click "Check it out here!"
3. Under "Source" ensure you select "main"
4. Once the main branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.
</details>
 
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
  13. For "VALUE", input your entire cred.json file including the curly braces.
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
  * StackOverflow for the dictonary
  * W3Schools for zipping the sales and booking data
* Acknowledgements
  * My mentor Rahul for his ongoing support and feedback
  * The Code Institute’s Tutor Support
  * The Slack community
