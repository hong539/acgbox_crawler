import pandas as pd

check_table = pd.read_html("https://www.ubus.com.tw/Booking/FareInquiry")

print(check_table)