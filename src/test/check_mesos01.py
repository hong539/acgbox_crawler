#要實作分散式行程安排規劃的應用，可以使用分散式任務調度框架，例如Apache Mesos、Kubernetes等。
#這些框架可以幫助你自動調度多個行程在多台機器上執行，以達到高效利用資源的目的。
import mesos.native
from mesos.interface import Scheduler

class TaskScheduler(Scheduler):
    def registered(self, driver, framework_id, master_info):
        print("Registered with framework ID %s" % framework_id.value)

    def resourceOffers(self, driver, offers):
        for offer in offers:
            print("Received offer %s" % offer.id.value)
            tasks = []
            task = mesos.native.TaskInfo(
                "task-1",
                "echo hello",
                mesos.native.Resources(cpus=1, mem=128),
            )
            tasks.append(task)
            driver.launchTasks(offer.id, tasks)

    def statusUpdate(self, driver, update):
        print("Received status update for task %s with state %s" % (update.task_id.value, mesos.native.TaskState.Name(update.state)))

if __name__ == "__main__":
    framework = mesos.native.FrameworkInfo(
        "MyFramework",
        user="",
    )
    scheduler = TaskScheduler()
    driver = mesos.native.MesosSchedulerDriver(
        scheduler,
        framework,
        "zk://localhost:2181/mesos",
    )
    status = 0 if driver.run() == mesos.native.DRIVER_STOPPED else 1
    driver.stop()
    sys.exit(status)

