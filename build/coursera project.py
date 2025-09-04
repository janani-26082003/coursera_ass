import yfinance as yf
import pandas as pd

# Download Tesla (TSLA) stock data
tesla_data = yf.download('TSLA', period="1y")  # Fetch past 1 year of data

# Reset the index so Date becomes a column
tesla_data.reset_index(inplace=True)

# Save the data to a CSV file
tesla_data.to_csv("tesla_stock_data.csv", index=False)

# Display the first five rows
print(tesla_data.head())


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL for Tesla's revenue data on MacroTrends
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"

# Send a request to fetch the webpage
headers = {"User-Agent": "Mozilla/5.0"}  # Some websites block bots without a user-agent
response = requests.get(url, headers=headers)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all tables
tables = soup.find_all("table")

# Locate the correct table containing "Tesla Quarterly Revenue"
revenue_table = None
for table in tables:
    if "Tesla Quarterly Revenue" in table.text:
        revenue_table = table
        break

# Ensure the table is found
if revenue_table:
    # Extract table rows
    rows = revenue_table.find_all("tr")

    # Parse data into a list
    data = []
    for row in rows[1:]:  # Skip the header row
        cols = row.find_all("td")
        cols = [col.text.strip() for col in cols]
        if len(cols) == 2:  # Ensure two columns: Date & Revenue
            data.append(cols)

    # Create a DataFrame
    tesla_revenue = pd.DataFrame(data, columns=["Date", "Revenue"])

    # Clean Revenue column (remove non-numeric characters)
    tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(r"[^\d.]", "", regex=True)
    tesla_revenue["Revenue"] = pd.to_numeric(tesla_revenue["Revenue"], errors='coerce')

    # Display the last five rows
    print(tesla_revenue.tail())

else:
    print("Error: Revenue table not found. The website structure may have changed.")

import yfinance as yf
import pandas as pd

# Download GameStop (GME) stock data
gme_data = yf.download('GME', period="1y")  # Fetch past 1 year of data

# Reset the index so Date becomes a column
gme_data.reset_index(inplace=True)

# Save to a CSV file
gme_data.to_csv("gme_stock_data.csv", index=False)

# Display the first five rows
print(gme_data.head())

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"

# Send a request to fetch the webpage
headers = {"User-Agent": "Mozilla/5.0"}  # Some websites block bots without a user-agent
response = requests.get(url, headers=headers)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all tables
tables = soup.find_all("table")

# Locate the correct table containing "GameStop Quarterly Revenue"
revenue_table = None
for table in tables:
    if "GameStop Quarterly Revenue" in table.text:
        revenue_table = table
        break
   
    import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"

# Send a request to fetch the webpage
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find the correct table by searching for 'GameStop Quarterly Revenue'
tables = soup.find_all("table")

revenue_table = None
for table in tables:
    if "GameStop Quarterly Revenue" in table.text:
        revenue_table = table
        break

# Ensure we found the table
if revenue_table:
    # Extract table rows
    rows = revenue_table.find_all("tr")

    # Parse data into a list
    data = []
    for row in rows[1:]:  # Skipping the header row
        cols = row.find_all("td")
        cols = [col.text.strip() for col in cols]
        if len(cols) == 2:  # Ensure two columns: Date & Revenue
            data.append(cols)

    # Create a DataFrame
    gme_revenue = pd.DataFrame(data, columns=["Date", "Revenue"])

    # Convert Revenue to numeric (removing non-numeric characters)
    gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace(r"[^\d.]", "", regex=True)
    gme_revenue["Revenue"] = pd.to_numeric(gme_revenue["Revenue"], errors='coerce')

    # Display the last five rows
    print(gme_revenue.tail())

else:
    print("Revenue table not found. The website might have changed its structure.")
    
    
#DATA VISUALIZATION

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Function to plot stock graph
def make_graph(stock_data, title):
    plt.figure(figsize=(12,6))
    plt.plot(stock_data["Date"], stock_data["Close"], label="Closing Price", color="red")
    plt.xlabel("Date")
    plt.ylabel("Stock Price (USD)")
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.show()

# Download GameStop (GME) stock data
gme_data = yf.download('GME')

# Reset index to ensure Date is a column
gme_data.reset_index(inplace=True)

# Plot GME stock graph
make_graph(gme_data, "GameStop (GME) Stock Price Over Time")
import yfinance as yf
import matplotlib.pyplot as plt

# Function to plot stock graph
def make_graph(ticker, title):
    # Download stock data for the past year
    stock_data = yf.download(ticker, period="1y")
    
    # Reset index to ensure Date is a column
    stock_data.reset_index(inplace=True)

    # Plot stock prices
    plt.figure(figsize=(12,6))
    plt.plot(stock_data["Date"], stock_data["Close"], label="Closing Price", color="blue")
    plt.xlabel("Date")
    plt.ylabel("Stock Price (USD)")
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)  # Rotate x-axis labels for readability
    plt.show()

# Call the function for Tesla stock (TSLA)
make_graph("TSLA", "Tesla Stock Price Over the Past Year")
