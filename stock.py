
import yfinance as yf 
import streamlit as st
import pandas as pd




st.title('Stock Data')

getstock = st.text_input('Type in the stock name', 'GOOGL')

stock= yf.Ticker(getstock)

st.header('Historical price of ' + getstock)
old =stock.history(start='2010-01-01',  end='2021-01-01')
st.line_chart(old.Close)

st.header('Major holders of ' + getstock)
stock.major_holders

st.header('Balance sheet of ' + getstock)
stock.balance_sheet

st.header('Cashflow of ' + getstock)
stock.cashflow

st.header('Earnings of ' + getstock)
stock.earnings

st.header('Actions of ' + getstock)
stock.actions




