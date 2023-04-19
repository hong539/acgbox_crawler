#行程安排規劃是一個複雜的問題，需要考慮許多因素，例如每個任務的時間和優先級、資源分配、限制和約束條件等。
#以下是一個簡單的範例，展示如何使用Python來安排一個簡單的行程：
from datetime import datetime, timedelta

# 定義一個任務類別
class Task:
    def __init__(self, name, duration, priority):
        self.name = name
        self.duration = duration
        self.priority = priority

# 創建一些任務
task1 = Task("任務1", timedelta(minutes=30), 1)
task2 = Task("任務2", timedelta(minutes=45), 2)
task3 = Task("任務3", timedelta(minutes=60), 3)
task4 = Task("任務4", timedelta(minutes=15), 1)
task5 = Task("任務5", timedelta(minutes=90), 2)

# 將所有任務放入一個清單
tasks = [task1, task2, task3, task4, task5]

# 將任務按優先級排序
tasks.sort(key=lambda x: x.priority)

# 定義一個起始時間
start_time = datetime.now()

# 計算每個任務的結束時間
for task in tasks:
    end_time = start_time + task.duration
    print(f"{task.name} 從 {start_time} 到 {end_time}")
    start_time = end_time