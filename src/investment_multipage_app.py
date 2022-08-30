import streamlit as st
from streamlit_multipage import MultiPage
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
import pandas as pd
from pathlib import Path
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# Import Ethereum Transaction Functions into the investment Application

from crypto_wallet import send_transaction, generate_account, get_balance


# Database of Algo Portfolios.
# Master data consists of 5 year Metrics
master_data = pd.read_csv(
    Path("../data/master_data.csv")
)

# list of seller names
people = master_data['Person Name'].tolist()

# Yearly data consists of a year Metrics of last 5 years
data_2017 = pd.read_csv(
    Path("../data/2017.csv")       
)

data_2018 = pd.read_csv(
    Path("../data/2018.csv")       
)

data_2019 = pd.read_csv(
    Path("../data/2019.csv")       
)

data_2020 = pd.read_csv(
    Path("../data/2020.csv")       
)

data_2021 = pd.read_csv(
    Path("../data/2021.csv")       
)

year = ["2017", "2018", "2019", "2020", "2021"]

# Streamlit Sidebar Code - Start
# Making the sidebar wider as first step
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 380px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 380px;
        margin-left: -380px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown("#### My Account Address")


#  Call the `generate_account` function and save it as the variable `account`
account = generate_account()

##########################################

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)


##########################################
# Define a new `st.sidebar.write` function that will display the balance of the
# customer’s account. Inside this function, call the `get_balance` function and
#  pass it your Ethereum `account.address`.

# Call `get_balance` function and pass it your account address
# Write the returned ether balance to the sidebar
# YOUR CODE HERE
ether = get_balance(w3, account.address)
st.sidebar.write("Ether Balance: <span style='color:Green;font-weight:700'>" + str(ether)+"</span>", unsafe_allow_html=True)
st.sidebar.text("------------------------------------ \n\n")


def home_page(st, **state):
    namespace = "main"
    variables = state[namespace] if namespace in state else {}

    # title
    st.markdown("# 1Stop Investing Shop")
    st.markdown("##### Project 3 by Marc, Jigar, Padma & Roy")
    st.text("-------------------------------------------------------------- \n")

    for index, row in master_data.iterrows():
        st.image( row['Image'], width=500)
        st.markdown("**"+ str(index+1) + ". Name:** "+ row['Person Name'])
        st.markdown("**Investment strategies:** "+ row["Investment strategies"])
        metric_text = "**Strategy Profit:** <span style='color:Green;font-weight:700'>"+ row["Strategy Profit"]+"</span>&nbsp;&nbsp;&nbsp;&nbsp;" +"**Annualised Return:**  <span style='color:Green;font-weight:700'>"+ row["Annualised Return"] +"</span>&nbsp;&nbsp;&nbsp;&nbsp;" +"**Profit Factor:**  <span style='color:Green;font-weight:700'>"+ str(row["Profit Factor"])+"</span>"
        st.markdown(metric_text, unsafe_allow_html=True)       
        st.markdown("**Ethereum Account Address:** "+  row["Ethereum Account Address"])
        st.markdown("**Price:** <span style='color:Green;font-weight:700'>"+ str(row["Price"]) +"</span> Ether", unsafe_allow_html=True)
        st.markdown("**Subscription:** "+ row["Subscription"] , unsafe_allow_html=True)
        st.text("-------------------------------------------------------------- \n")


def buy_page(st, **state):
    namespace = "result"
    variables = state[namespace] if namespace in state else {}
    
    # Streamlit application headings
    st.markdown("# 1Stop Investing Shop")
    st.text("-------------------------------------------------------------- \n")
    st.markdown("#### Backtest")
    #st.text("-------------------------------------------------------------- \n")

    #Create a select box to chose a developer profile
    person = st.selectbox('Select a Developer', people)

    backtest_person = master_data.loc[master_data['Person Name'] == person]
    backtest_person_address = backtest_person["Ethereum Account Address"].values[0]
    backtest_person_rate = backtest_person["Price"].values[0]
    st.markdown("**Investment strategies 5 Yrs:** " + backtest_person["Investment strategies"].values[0])
    #st.markdown(backtest_person["Investment strategies"].values[0])
    st.markdown("**Strategy Profit:** <span style='color:Green;font-weight:700'>"+ backtest_person["Strategy Profit"].values[0]+"</span>", unsafe_allow_html=True)       
    st.markdown("**Annualised Return:**  <span style='color:Green;font-weight:700'>"+ backtest_person["Annualised Return"].values[0]+"</span>"  , unsafe_allow_html=True)       
    st.markdown("**Profit Factor:**  <span style='color:Green;font-weight:700'>"+ str(backtest_person["Profit Factor"].values[0])+"</span>", unsafe_allow_html=True)       
    st.markdown("**Ethereum Account Address:** "+ backtest_person_address )
    st.markdown("**Price:** <span style='color:Green;font-weight:700'>"+ str(backtest_person_rate) +"</span> Ether", unsafe_allow_html=True)
    st.markdown("**Subscription:** "+ backtest_person["Subscription"].values[0] , unsafe_allow_html=True)
    st.markdown("-------------------------------")

    # Create a selectbox to chose a backtest period
    backtest_year = st.selectbox("Select Backtest Period", year)

    # Identify the backtest data for the developer
    backtest_data = pd.DataFrame()

    if backtest_year == "2017":
        backtest_data = data_2017.loc[data_2017['Person Name'] == person]
    elif backtest_year == "2018":
        backtest_data = data_2018.loc[data_2018['Person Name'] == person]
    elif backtest_year == "2019":
        backtest_data = data_2019.loc[data_2019['Person Name'] == person]
    elif backtest_year == "2020":
        backtest_data = data_2020.loc[data_2020['Person Name'] == person]
    elif backtest_year == "2021":
        backtest_data = data_2021.loc[data_2021['Person Name'] == person]

    if(len(backtest_data)> 0):
        backtest_metric = "**Strategy Profit:** <span style='color:Green;font-weight:700'>"+ backtest_data["Strategy Profit"].values[0]+"</span>&nbsp;&nbsp;&nbsp;&nbsp;" +"**Annualised Return:**  <span style='color:Green;font-weight:700'>"+ backtest_data["Annualised Return"].values[0] +"</span>&nbsp;&nbsp;&nbsp;&nbsp;" +"**Profit Factor:**  <span style='color:Green;font-weight:700'>"+ str(backtest_data["Profit Factor"].values[0])+"</span>"
        # Write the bactest metric in sidebar
        st.markdown(backtest_metric, unsafe_allow_html=True)
        st.image(backtest_data['Image'].values[0], width=600) 
    

    if st.button("Purchase Strategy"):

        # Call the `send_transaction` function and pass it 3 parameters:
        # Your `account`, the `candidate_address`, and the `rate` as parameters
        # Save the returned transaction hash as a variable named `transaction_hash`
        # YOUR CODE HERE
        transaction_hash = send_transaction(w3, account, backtest_person_address, backtest_person_rate)

        # Markdown for the transaction hash
        st.markdown("#### Validated Transaction Hash")

        # Write the returned transaction hash to the screen
        st.write(transaction_hash)

        # Celebrate your successful payment
        st.balloons()

def footer(st):
    st.text("-------------------------------------------------------------- \n")
    st.write("Developed by by Marc, Jigar, Padma & Roy")



app = MultiPage()
app.st = st

app.add_app("Home Page", home_page)
app.add_app("Buy Page", buy_page)
app.navbar_style = "VerticalButton"
app.footer = footer

app.run()