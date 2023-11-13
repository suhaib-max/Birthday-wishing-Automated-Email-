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
if today in birthday_dict:      #it check key only in method
    with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt", "r") as letter:
        changed = letter.read()
    # Get the data_row for today's birthday
    data_row = birthday_dict[today]

    # Replace [NAME] with the actual name
    modified_letter = changed.replace("[NAME]",data_row["name"])

    email = "sshuhaib274@gmail.com"
    password = "wolbqcyegqklzxgj"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=data_row['email'],
                            msg=f"Subject:Birthday_wish\n\n{modified_letter}")
