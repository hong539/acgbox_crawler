#使用Python语言编写的一个简单的Redis分布式锁示例
import redis
import time

r = redis.Redis(host='localhost', port=6379)

# 获取锁
def acquire_lock(lockname, acquire_timeout=10):
    start_time = time.time()
    while time.time() - start_time < acquire_timeout:
        if r.setnx(lockname, 'locked'):
            return True
        elif not r.ttl(lockname):
            r.expire(lockname, 10)
        time.sleep(0.1)
    return False

# 释放锁
def release_lock(lockname):
    r.delete(lockname)

# 使用锁
def do_something_with_lock():
    if acquire_lock('mylock'):
        print('Lock acquired!')
        time.sleep(5)
        release_lock('mylock')
        print('Lock released!')

do_something_with_lock()
