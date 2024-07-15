import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px

st.title('Stock Dashboard')

# Use st.session_state to store dates
if 'start_date' not in st.session_state:
  st.session_state['start_date'] = None
if 'end_date' not in st.session_state:
  st.session_state['end_date'] = None


ticker = st.sidebar.text_input('Ticker')
start_date = st.sidebar.date_input('Start Date', value=st.session_state['start_date'])
end_date = st.sidebar.date_input('End Date', value=st.session_state['end_date'])


# Download data with error handling
try:
  data = yf.download(ticker, start=start_date, end=end_date)
except (ConnectionError, ValueError):
  st.error(f"Error downloading data for {ticker}.")
  data = pd.DataFrame()  # Create an empty DataFrame to handle no data case

# Check if data is downloaded successfully
if not data.empty:
  fig = px.line(data, x=data.index, y='Adj Close', title=ticker)
  st.plotly_chart(fig)
else:
  st.warning("No data downloaded. Please check the ticker symbol or date range.")



pricing_data, fundamental_data, news = st.tabs(["Pricing Data", "Fundamental Data", "Top 10 News"])

with pricing_data:
  st.header('Price Movements')
  data2 = data
  data2['% Change'] = data['Adj Close'] / data['Adj Close'].shift(1) - 1
  data2.dropna(inplace= True)
  st.write(data2)
  annual_return = data2['% Change'].mean()*252*100
  st.write('Annual Return is ',annual_return,'%')
  stdev = np.std(data2['% Change'])*np.sqrt(252)
  st.write('Standard Deviation is ',stdev*100,'%')
  st.write('Risk Adj. Return is ',annual_return/(stdev*100))


from alpha_vantage.fundamentaldata import FundamentalData
with fundamental_data:
 key = 'LVMEXB9LJW1TB1SY'
 fd = FundamentalData(key, output_format='pandas')

 st.subheader('Balance Sheet')
 balance_sheet = fd.get_balance_sheet_annual(ticker)[0]
 bs = balance_sheet.T[2:]
 bs.columns = list(balance_sheet.T.iloc[0])
 st.write(bs)
 st.subheader('Income Statement')
 income_statement = fd.get_income_statement_annual(ticker)[0]
 is1 = income_statement.T[2:]
 is1.columns = list(income_statement.T.iloc[0])
 st.write(is1)
 st.subheader('Cash Flow Statement')
 cash_flow = fd.get_cash_flow_annual(ticker)[0]
 cf = cash_flow.T[2:]
 cf.columns = list(cash_flow.T.iloc[0])
 st.write(cf)

from stocknews import StockNews

with news:  # Assuming this is a context manager for news access
    st.header(f'News of {ticker}')
    sn = StockNews(ticker, save_news=False)
    df_news = sn.read_rss()

    for i in range(10):
        st.subheader(f'News {i+1}')
        st.write(df_news.loc[i, 'published'])  # Using .loc for clarity
        st.write(df_news.loc[i, 'title'])
        st.write(df_news.loc[i, 'summary'])

        # Check if 'sentiment_title' exists before accessing
        if 'sentiment_title' in df_news.columns:
            title_statement = df_news.loc[i, 'sentiment_title']
            st.write(f'Title Statement: {title_statement}')
        else:
            st.write('Title Sentiment Not Available')  # Handle missing column

        # Check if 'statement_summary' exists before accessing 
        if 'statement_summary' in df_news.columns:
            news_statement = df_news.loc[i, 'statement_summary']
            st.write(f'News Statement: {news_statement}')
        else:
            st.write('News Summary Not Available')  # Handle missing column




