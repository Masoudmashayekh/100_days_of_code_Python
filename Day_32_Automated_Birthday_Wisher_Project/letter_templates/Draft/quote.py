# # import smtplib
# #
# # my_email = "aaaaaa@gmail.com"
# # password = "AAAAAAAAAA"
# #
# # with smtplib.SMTP("smtp.gmail.com", 587) as connection:
# #     connection.starttls()
# #     connection.login(user=my_email, password=password)
# #     msg = ("Subject: Email from Masoud's Python Code\n\nDear Masoud,\n \nI hope this email finds you "
# #            "well.\nPlease keep going...\n \nBest regards\nYour friend Masoud")
# #     connection.sendmail(from_addr=my_email, to_addrs="masoudmashayekh4944@gmail.com", msg=msg)
#
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# which_day = now.weekday()
# print(now)
# print(year)
# print(month)
# print(day)
# print(which_day)
#
# day_of_birth = dt.datetime(year=1992, month=9, day=6,hour= 21,)
# print(day_of_birth)
import smtplib
import datetime as dt
import random

my_email = "aaaaaa@gmail.com"
password = "AAAAAAAAAA"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs="masoudmashayekh4944@gmail.com",
                            msg=f"Subject: weekly quote\n\n {quote}")
