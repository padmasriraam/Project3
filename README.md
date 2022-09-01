# 1Stop Investing Shop !!

![image](https://user-images.githubusercontent.com/101629518/187576431-0b91def2-9a23-44b9-a69f-2f77ab9e3b27.png)

## Problem Statement
People want to invest in the wide variety of options available but developing strategies is the challenge! There are limited options available but restricted to types and size of investment. Below are some of the challenges using some of the more traditional investing approaches:

* **Too Defensive** - Indexed funds are easier option for investing but are too defensive in terms of returns
* **Too Expensive** - Joining a fund / investment manager for better returns but returns would be offset with the administration and management fees.
* **Too Hard** - Self learning and investing in the market data is time consuming and needs extensive learning for better returns but returns would be offset with the administration and management fees.

All the challenges listed above are obstacles for potential investors to overcome, and provide an opportunity for additional investing approaches that can demonstrate higher returns, more personal choice and exposure to a community of investment experts.

## Value Proposition

We address these challenges buy offering investors access to an online marketplace, where the algo-trading developers can sell their algorithm and IP, so the investors (buyers) can "test-drive" and back-test different algorithms based on their risk profile and buy the one that meets their appetite. Benefits include:

* Key insights, algorithm information, metrics and customer ratings are made available to customers to make an informed decision before purchasing access to an algorithm.
* Easy, instantaneous, cross-country and less expensive transactions, the payment from investors to sellers is executed through a blockchain platform. 
* Affordable entry point accessing reliable, consistent and innovative algorithms from a community of algorithmic investement developers

Basically 1Stop Investing shop! 

*The algorithms and back testing functionality is not part of this project due to the time constraints*.

The project was analysed in August 2022 by :
-   Padma Ram
-   Roy Booker
-   Jigar Lotia
-   Marc Julies


## How it works

![image](https://user-images.githubusercontent.com/101629518/187581492-5cbc6b88-2047-413c-b806-e07bac43ce80.png)

The 1Stop Investing Shop offering provides benefits for both sellers of investment algorithms as well as the buyers. The high-level process is for both buyer and seller is as follows:

* **Algo-trading developers lists their algorithm** - Algo-trading developer builds a trading algorithm that aims to profit, but rather than using it for themselves, they list it on the marketplace for others to also buy and thus making money for themselves
* **Investors reviews different algorithm and historical returns** -Investors uses the marketplace to look at different algorithms listed and reviews the returns as claimed
* **Investors does their own back testing** - Rather than relying on the claimed returns, investors can run their own backtesting in the app using their chosen period and see the results
* **Investors shortlist the algorithm** - After comparing the few algorithm, the investors narrows down on the algorithm they prefer based on the backtesting results they have reviewed.
* **Buy instantly through blockchain** - Investors can buy the algorithm instantantly and to provide speed, accuracy and less fees, the transaction is executed through blockchain!

## Technologies Leveraged

The technologies used are critical in ensuring the solution offered is positioned at a price point that opens up door to investing to a wider audience. The technologies provided a solution that is intuitve, efficient and cost effective. Key to our solution is the ability to support crypto transactions and future development around smart contracts managing the agreements between buyer and seller.

Below are the technologies we used:

* **Streamlit & streamlit_multipage** - teamlit based app for the UX and interaction
* **Algo-trading developers lists their algorithm** - Steamlit based app for the UX and interaction
* **Blockchain & Cryptowallet Library** - Blockchain based cryptowallet library to generate account, get balance and execute transactions.
* **Ganache and Metamask for testing transactions** - Ganache was used a virtual blockchain for testing and Metamask as a wallet to confirm the transactions.
* **BIP44 and Web3** - IP44 and Web3 library to handle Ethereum based wallet transactions
* **Backtest Zone** - (https://www.backtestzone.com/) Backtest Zone app was used to generate the backtesting data that is used within the Streamlit App

![image](https://user-images.githubusercontent.com/101629518/187583416-99362eef-44fe-49c2-a500-b057f03d1590.png)


##  Data Preparation

![image](https://user-images.githubusercontent.com/101629518/187586768-2c5daea3-7cd3-41f1-a36f-7d11b3556a72.png)


The data preparation to support the minimum viable demonstration of the 1Stop Investing Shop. The steps are as follows:

* **High level concept creation** - Teamlit based app for the UX and interaction
* **Portfolio Creation** - BacktestZone was used to examine the types of portfolios that where available to be back tested and 4 portfolios where nominated for each of the team members
* **Back testing** - A simple moving average was used to compare the performance of the portfolios between 2017 and 2021 . Strategy Profit %, Annualized return % and Profit Factor
* **Yearly investigation** - This analysis then was done over single years to look further into how each portfolio reacted to the volatile market conditions experienced recently with the Covid pandemic. 
* **Data visualization** - Graphs on strategy equity curves were viewed on back_test_zone and modified to suit the date ranges.

## Streamlit App
This [streamlitapp](src/investment_multipage_app.py) provides the following features:

* Import of the Ethereum transaction function into the 1Stop Investing Shop streamlit application. 
* Five years worth of metric data generated from Backtest Zone is sourced from the [data folder](data/).
* Creation of the list of sellers used in the minimum viable application demonstration
* Configuration of the user interface - sidebar
* Displaying Ethereum balances
* Selection of backtesting data
* Selecting a product
* Displaying developer profile 
* Implementing the purchasing transaction

### Landing Page

![image](https://user-images.githubusercontent.com/101629518/187657832-975a7d3d-c1f7-418d-aa15-e8f4603f9451.png)

**Functionality:**

* Left hand panel displaying the Ethereum account balances, with navigation options
* The main page displaying the Algo developer profile, associated metrics, pricing and update features

### Backtest Page

![image](https://user-images.githubusercontent.com/101629518/187659013-cf7b18e2-96c5-4099-83e0-39eb2a86b28e.png)

**Functionality:**

* Selection of a developer and associated product
* Selection of period to support backtesting
* Display of backtesting results

### Metamask

![image](https://user-images.githubusercontent.com/101629518/187658542-41bafbc2-477f-4caa-a95f-bb0ce7c57a4f.png)

### Garnache

![image](https://user-images.githubusercontent.com/101629518/187658852-7ea70144-f457-4441-a605-de2aa993eba6.png)



## Challenges

The limited development time was a factor we had to consider when defining the scope of the minimum viable product. The main challenges encountered whilst developing the 1Stop Investing shop minimum viable product. 

* **Streamlit - Multipage concept** - Team had to investigate the multipage concept of Streamlit which is released only in June '22.
* **Data Preparation** - The data had to be prepared to "simulate" the backtesting step within the Streamlit App.
* **Local Ganache Addresses** - For the demo, we had to setup Metamask and had to update addresses locally for each member

## Future State 

![image](https://user-images.githubusercontent.com/101629518/187588931-672f845e-fe46-462b-94e2-167b05b35dd4.png)


We see potential in the 1Stop Investing Shop solution and in order to extend the solution further we see the backlog of development items as key producing a fully operational offering:

* **Backtesting Automation** - Currently the backtesting function is simulated and can be automated
* **Alpaca API Integration** - Connect to Alplaca API to fetch the historical data requried for backtesting
* **Seller Feature** - Build the seller part of the app where they can lists and manage their algorithms for selling and check orders and transactions..
* **Customer Insights** - Ability to proivide the ratings and feedback to seller which will build over the period of time and help other investors
* **Automated AWS Deployment** - On successful completion of transaction of investor buying the algorithm, as a next step it could deploy on the AWS as a bot with the algorithm logic so investors can start making money without needing to go technical on how to deploy and run the algorithm


## Slide Deck Link
[Slide Deck](document/Project%202-%20Presentation%20(Fintech%20Bootcamp).pdf)

## Resources
- [backtestzone.com](https://www.backtestzone.com) for back testing results
