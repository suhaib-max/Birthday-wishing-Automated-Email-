import datetime
import pandas
import random
import smtplib

#reading csv
data = pandas.read_csv("birthdays.csv")
now = datetime.datetime.now()
#creating a tuple of today month and day
today = (now.month,now.day)

birthday_dict = {(data_row["month"],
                  data_row["day"]): data_row for index, data_row in data.iterrows()}
