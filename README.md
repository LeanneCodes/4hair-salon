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

### Introductory message and sales input

When the user runs the system, they will be greeted with an opening message and their first set of instructions. The NDoS will need to enter in the salons' sales figures for each city in a specific order, which need to be separated by a comma. No need for spaces or pound signs. An example of how the data should be entered is given.

![image](https://user-images.githubusercontent.com/81588887/133588088-c4962ecf-1f3e-4150-9cb7-08fa89ac4447.png)
![image](https://user-images.githubusercontent.com/81588887/133590157-1530b987-3ab4-4d08-8338-e0fb233d39fc.png)

### Completed bookings input

Once the NDoS has inputted the sales figures, they will be prompted to enter the completed bookings for each city, in the same order. This is done, so the system can calculate what the average booking value is for each city.

![image](https://user-images.githubusercontent.com/81588887/133588595-c8e7e54e-7f1f-48d1-87cf-6e2a1e623591.png)
![image](https://user-images.githubusercontent.com/81588887/133590208-16277512-13af-4150-a11a-7dfe0f2c38bd.png)

### Data valid

If the data is valid, the NDoS will be notified with the below image. The data will only be classified as valid, if both the sales and completed booking inputs are 6 figures each, separated by commas.

![image](https://user-images.githubusercontent.com/81588887/133589477-57f68ea0-4d6c-4150-800d-6d5abff0ccf1.png)

### Confirming user input is correct

Although the system informs the user that the data they inputted was correct, it doesn't necessarily mean the data is correct. This point in the system gives the user a chance to check the data for the sales and completed bookings is correct before progressing. If the data is correct, the user will confirming by typing in "1". If not correct, the user will need to type "2".

![image](https://user-images.githubusercontent.com/81588887/133590843-289c4d0b-b81a-4372-b99b-fe457d3745ee.png)

### System updating relevant Google worksheets

Now that the NDoS confirmed the data is correct, the system will show statements that the calculations are happening and that each relevant Google worksheet is being updated successfully.

![image](https://user-images.githubusercontent.com/81588887/133591140-422068db-11f5-4793-8e43-a1c7cc3bb8c7.png)

### Recommendations based on data inputted

The system now tells the user what the current target is for each city, what their current average booking value (ABV) is and what recommendations, if any, need to be taken to improve salon's performance. 

![image](https://user-images.githubusercontent.com/81588887/133591987-b2b715ee-20fe-4e02-9ee1-10d02f5dc000.png)

Recommendations are based on how far away the city's salon is away from their own target.

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

### Reviewing 4Hair Salon Google workbook

Now the NDoS has reviewed the recommendations outputted from the system, they can review the latest data they entered and the ABV on the Google workbook via a link. Heroku doesn't allow hyperlinks, so the user is instructed to copy the link. Which they can then open the link in a new tab.

![image](https://user-images.githubusercontent.com/81588887/133594840-810907da-5ccb-4887-a295-6549c1871ef0.png)

## 4Hair Salon Google Workbook View

This workbook is read-only for users who haven't been granted permisison to edit the file. Only the NDoS and senior management have access to edit the file. This is to limit the number of accidental changes made to the workbook.

### Sales Worksheet

The "Sales" worksheet displays historic data inputted and the most recent data the NDoS supplied.

![image](https://user-images.githubusercontent.com/81588887/133596558-4be3b54c-4053-4672-aa05-b0953d5793f6.png)

### Completed Bookings Worksheet

The "CompletedBookings" worksheet displays historic data inputted and the most recent data the NDoS supplied.

![image](https://user-images.githubusercontent.com/81588887/133596635-1ab0fea5-b7d3-4b63-9c09-051648c32dcc.png)

### ABV Worksheet

The "ABV" worksheet displays the calculation between the total sales for each city divided by the number of completed bookings for each city.

![image](https://user-images.githubusercontent.com/81588887/133596705-22e6700c-f4de-42ae-a65a-fbe17e46649b.png)

