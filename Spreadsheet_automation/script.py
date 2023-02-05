'''
    ## Spreadsheet Automation Functionalities:
    - First upload two datasets
    - The script will we compare the two datasets
    - The output will be a pie chart
    ## Spreadsheet Automation Instructions:
    ### Step 1:
    Open Termnial
    ### Step 2:
    Locate to the directory where python file is located
    ### Step 3:
    Run the command: python script.py/python3 script.py
    ### Step 4:
    Sit back and Relax. Let the Script do the Job.
'''
# importing libraries
import pandas as pd
import plotly.express as px


# storing the dataset
data1 = input("Enter first dataset")
data2 = input("Enter second dataset")


# reading the data
data_read_1 = pd.read_excel(data1)
data_read_2 = pd.read_excel(data2)


# print(df_prices, df_home_1)


refrence = input("What is the basis of merging?")
data_total = data_read_2.merge(data_read_1, on=refrence)


# print(df_total)
criteria_1 = input("Enter criteria 1")
criteria_2 = input("Enter criteria 2")

fig = px.pie(data_total[[criteria_1, criteria_2]],
             values=criteria_2, names=criteria_1)

fig.show()
