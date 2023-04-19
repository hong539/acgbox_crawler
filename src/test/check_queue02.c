#include <linux/init.h>
#include <linux/module.h>
#include <linux/workqueue.h>
#include <linux/slab.h>

MODULE_LICENSE("Dual BSD/GPL");

// 創建一個 workqueue
static struct workqueue_struct *example_wq;

// 定義一個 workqueue 工作
struct work_data {
    struct work_struct work;
    int data;
};

// workqueue 回調函數
static void example_work_func(struct work_struct *work)
{
    struct work_data *wd = container_of(work, struct work_data, work);
    printk(KERN_ALERT "example workqueue: %d\n", wd->data);
    kfree(wd);
}

// 初始化模組
static int __init example_init(void)
{
    int i;
    struct work_data *wd;

    // 創建 workqueue
    example_wq = create_workqueue("example_wq");

    // 創建 10 個 work 並加入到 workqueue 中
    for (i = 0; i < 10; i++) {
        wd = kmalloc(sizeof(*wd), GFP_KERNEL);
        if (!wd)
            return -ENOMEM;
        wd->data = i;
        INIT_WORK(&wd->work, example_work_func);
        queue_work(example_wq, &wd->work);
    }

    printk(KERN_ALERT "example workqueue initialized\n");
    return 0;
}

// 卸載模組
static void __exit example_exit(void)
{
    // 清空 workqueue 中的所有 work
    flush_workqueue(example_wq);

    // 銷毀 workqueue
    destroy_workqueue(example_wq);

    printk(KERN_ALERT "example workqueue uninitialized\n");
}

module_init(example_init);
module_exit(example_exit);