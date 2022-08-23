# Cryptocurrency Wallet

#
################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
import pandas as pd
from pathlib import Path
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
################################################################################
# Step 1:
# Import Ethereum Transaction Functions into the Fintech Finder Application

from crypto_wallet import send_transaction, generate_account, get_balance

################################################################################

# Database of Algo Portfolios.
# A single Ether is currently valued at $1,500
master_data = pd.read_csv(
    Path("../data/master_data.csv")
)

people = master_data['Person Name'].tolist()

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

print(master_data)
print(data_2017)
print(data_2018)
print(data_2019)
print(data_2020)
print(data_2021)

def get_people():
    """Display the database of Fintech Finders candidate information."""
    for index, row in master_data.iterrows():
        st.image(row['Image'], width=500)
        st.markdown("**Name:** "+ row['Person Name'])
        st.markdown("**Investment strategies:** "+ row["Investment strategies"])
        metric_text = "**Strategy Profit:** <span style='color:Blue;font-weight:700'>"+ row["Strategy Profit"]+"</span>&nbsp;&nbsp;&nbsp;&nbsp;" +"**Annualised Return:**  <span style='color:Blue;font-weight:700'>"+ row["Annualised Return"] +"</span>&nbsp;&nbsp;&nbsp;&nbsp;" +"**Profit Factor:**  <span style='color:Blue;font-weight:700'>"+ str(row["Profit Factor"])+"</span>"
        st.markdown(metric_text, unsafe_allow_html=True)       
        st.markdown("**Ethereum Account Address:** "+  row["Ethereum Account Address"])
        st.markdown("**Price:** "+ str(row["Price"]))
        st.text("-------------------------------------------------------------- \n")

def get_people1():
    st.write(master_data)

################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# Algo Trading Portfolio")
st.markdown("## Buy A Trading Algorithm!")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

##########################################
# Step 1 - Part 4:
# Create a variable named `account`. Set this variable equal to a call on the
# `generate_account` function. This function will create the Fintech Finder
# customer’s (in this case, your) HD wallet and Ethereum account.

# @TODO:
#  Call the `generate_account` function and save it as the variable `account`
# YOUR CODE HERE
account = generate_account()

##########################################

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

##########################################
# Step 1 - Part 5:
# Define a new `st.sidebar.write` function that will display the balance of the
# customer’s account. Inside this function, call the `get_balance` function and
#  pass it your Ethereum `account.address`.

# @TODO
# Call `get_balance` function and pass it your account address
# Write the returned ether balance to the sidebar
# YOUR CODE HERE
ether = get_balance(w3, account.address)
st.sidebar.write(ether)

##########################################

# Create a select box to chose a FinTech Hire candidate
person = st.sidebar.selectbox('Select a Person', people)

# Create a input field to record the number of hours the candidate worked
hours = st.sidebar.number_input("Number of Months")

#st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

# Identify the FinTech Hire candidate
#candidate = candidate_database[person][0]

# Write the Fintech Finder candidate's name to the sidebar
#st.sidebar.write(candidate)

# Identify the FinTech Finder candidate's hourly rate
#hourly_rate = candidate_database[person][3]

# Write the inTech Finder candidate's hourly rate to the sidebar
#st.sidebar.write(hourly_rate)

# Identify the FinTech Finder candidate's Ethereum Address
#candidate_address = candidate_database[person][1]

# Write the inTech Finder candidate's Ethereum Address to the sidebar
#st.sidebar.write(candidate_address)

# Write the Fintech Finder candidate's name to the sidebar

#st.sidebar.markdown("## Total Wage in Ether")

################################################################################
# Step 2: Sign and Execute a Payment Transaction

#wage = candidate_database[person][3] * hours


#st.sidebar.write(wage)

##########################################
# Step 2 - Part 2:
# * Call the `send_transaction` function and pass it three parameters:
    # - Your Ethereum `account` information. (Remember that this `account`
    # instance was created when the `generate_account` function was called.)
    #  From the `account` instance, the application will be able to access the
    #  `account.address` information that is needed to populate the `from` data
    # attribute in the raw transaction.
    #- The `candidate_address` (which will be created and identified in the
    # sidebar when a customer selects a candidate). This will populate the `to`
    # data attribute in the raw transaction.
    # - The `wage` value. This will be passed to the `toWei` function to
    # determine the wei value of the payment in the raw transaction.

# * Save the transaction hash that the `send_transaction` function returns as a
# variable named `transaction_hash`, and have it display on the application’s
# web interface.


if st.sidebar.button("Send Transaction"):

    # @TODO
    # Call the `send_transaction` function and pass it 3 parameters:
    # Your `account`, the `candidate_address`, and the `wage` as parameters
    # Save the returned transaction hash as a variable named `transaction_hash`
    # YOUR CODE HERE
    transaction_hash = send_transaction(w3, account, candidate_address, wage)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes FinTech Finder candidates to the Streamlit page
get_people()

################################################################################
# Step 3: Inspect the Transaction

