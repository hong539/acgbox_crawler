#行程安排規劃的應用可以使用Python中的datetime模組和第三方的行事曆套件來實現。
# 以下是一個簡單的範例，可以根據指定的日期和時間創建事件，將其添加到行事曆中並列印出來。
import datetime
import calendar
import os
import sys
from ics import Calendar, Event

# 讀取行事曆檔案
def read_calendar_file():
    # 如果沒有行事曆檔案就創建一個新的
    if not os.path.exists("calendar.ics"):
        with open("calendar.ics", "w") as calendar_file:
            calendar_file.write("BEGIN:VCALENDAR\nEND:VCALENDAR\n")
    with open("calendar.ics", "r") as calendar_file:
        return Calendar(calendar_file.read())

# 將事件加入行事曆
def add_event_to_calendar(calendar, event):
    calendar.events.add(event)

# 將行事曆寫入檔案
def write_calendar_file(calendar):
    with open("calendar.ics", "w") as calendar_file:
        calendar_file.write(str(calendar))

# 創建事件並加入行事曆
def create_event():
    # 讀取行事曆
    calendar = read_calendar_file()

    # 輸入事件的標題、日期和時間
    event_title = input("Enter event title: ")
    event_date = input("Enter event date (YYYY-MM-DD): ")
    event_time = input("Enter event time (HH:MM:SS): ")

    # 創建事件
    event = Event()
    event.name = event_title
    event.begin = datetime.datetime.strptime(f"{event_date} {event_time}", "%Y-%m-%d %H:%M:%S")

    # 將事件加入行事曆
    add_event_to_calendar(calendar, event)

    # 將更新後的行事曆寫入檔案
    write_calendar_file(calendar)

# 列印當月的行事曆
def print_month_calendar():
    # 取得當月的年份和月份
    now = datetime.datetime.now()
    year = now.year
    month = now.month

    # 創建月曆
    month_calendar = calendar.monthcalendar(year, month)

    # 列印月曆
    print(calendar.month_name[month], year)
    print("Mo Tu We Th Fr Sa Su")
    for week in month_calendar:
        week_str = ""
        for day in week:
            if day == 0:
                week_str += "   "
            else:
                week_str += f" {day:2d}"
        print(week_str)

# 執行主程式
while True:
    # 顯示選單
    print("1. Create Event")
    print("2. View Calendar")
    print("3. Quit")

    # 輸入選擇
    choice = input("Enter choice: ")

    # 根據選擇執行不同的功能
    if choice == "1":
        create_event()
    elif choice == "2":
        print_month_calendar()
    elif choice == "3":
        sys.exit()
    else