# Xchange
[Video Pitch](https://youtu.be/AgSmypWLm68 "Xchange Video Pitch")

## 2019 Johns Hopkins University Business Plan Competition
- Computer Science Innovation and Entrepreneurship II

## Members
- Co-Founders: Andrew Rojas, Gabe Villasana, Reece Griffith, Ali Rachidi

## Tech Stack Diagram
![](images/diagram.png?raw=true)

## Math Model Factors for MVP
- Weather
  - Did it rain/snow during the operating hours?
  - Also the average temperature for the given day (in 10 degree intervals).
- Day of the Week
- Season
- Is Delivery Offered?
- Number of Employees Working
- Discounts or Sale
- Price (If it changes or fluctuates)
- Holidays or Events

## Model
After much deliberation, the team has decided to use a Long short-term Memory (LSTM) network which is a type of Recurrent Neural Network (RNN) architecture. LSTM's are great for predicting based on time-series data, which will suit our purpose well. More about this LSTM architecture can be found in this blog: http://colah.github.io/posts/2015-08-Understanding-LSTMs/

We will construct the LSTM network using the tensorflow library.

## MongoDB Instance
We setup a mongoDB cloud instance on AWS with 512 MB of available memory. This is a free M0 version for our prototyping. We are working to connect it with our application via a simple Python-Mongo driver. The admin account has been created to read and write to the database. The database will store information obtained from Square's transaction API and the ML model will fetch the data to update its parameters.

## FAQ
> Q:
