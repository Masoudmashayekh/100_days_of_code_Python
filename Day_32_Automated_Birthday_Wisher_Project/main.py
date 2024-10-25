# #################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib

PLACEHOLDER = "[NAME]"
my_email = "AAAAAAAAA@gmail.com"
password = "AAAAAAAAAA"

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
print(data)
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
day = now.day
month = now.month
if not data[data.month == month].empty and not data[data.day == day].empty:
    filter_row = data[(data["month"] == month) & (data["day"] == day)]
    print(filter_row)
    name = filter_row["name"].to_string(index=False)
    email = filter_row["email"].to_string(index=False)

    # 3. If step 2 is true, pick a random letter from letter templates and replace the
    # [NAME] with the person's actual name from birthdays.csv
    random_letter = f"letter_{random.randint(1, 3)}"
    with open(f"letter_templates/{random_letter}.txt") as letter_file:
        letter_content = letter_file.read()
        ready_to_send = letter_content.replace(PLACEHOLDER, name)
        print(ready_to_send)
    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=email,
                            msg=f"Subject: Happy Birthday {name}\n\n {ready_to_send}")
else:
    print("There is no Birthday!")
