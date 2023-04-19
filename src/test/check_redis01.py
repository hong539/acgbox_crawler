#使用Python语言编写的一个简单的Redis消息队列示例：
import redis

r = redis.Redis(host='localhost', port=6379)

# 生产者将消息推入列表中
r.lpush('myqueue', 'message1')
r.lpush('myqueue', 'message2')

# 消费者从列表中取出消息
while True:
    message = r.brpop('myqueue')
    print(message)
