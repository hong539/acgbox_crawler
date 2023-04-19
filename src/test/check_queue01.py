#Linux kernel 的 concurrency managed workqueue 是一種用於處理任務的框架，
#Python 雖然無法直接使用 Linux kernel 的框架，但可以使用 Python 中的佇列模組(queue module)模擬實現
import threading
import time
import queue

class ManagedWorkQueue:
    def __init__(self, num_threads):
        self.queue = queue.Queue()
        self.threads = []
        for i in range(num_threads):
            t = threading.Thread(target=self.worker)
            t.daemon = True
            t.start()
            self.threads.append(t)

    def worker(self):
        while True:
            try:
                task = self.queue.get(timeout=1)
            except queue.Empty:
                continue

            # Handle the task
            print("Processing task:", task)
            time.sleep(1)

            self.queue.task_done()

    def add_task(self, task):
        self.queue.put(task)

    def wait_completion(self):
        self.queue.join()