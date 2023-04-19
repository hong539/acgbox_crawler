//使用 C 程式語言示範如何在 Redis 中使用分布式鎖的程式碼範例：
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <hiredis.h>

int main(int argc, char **argv) {
    const char *redis_host = "localhost";
    int redis_port = 6379;

    // 建立 Redis 連接
    redisContext *redis_conn = redisConnect(redis_host, redis_port);
    if (redis_conn == NULL || redis_conn->err) {
        printf("Failed to connect to Redis: %s\n", redis_conn->errstr);
        exit(EXIT_FAILURE);
    }

    // 設置分布式鎖
    const char *lock_key = "my_lock";
    const char *lock_val = "lock_val";
    const int lock_timeout = 10000; // 鎖定超時時間，單位：毫秒
    redisReply *reply = (redisReply *)redisCommand(redis_conn, "SET %s %s NX PX %d", lock_key, lock_val, lock_timeout);
    if (reply == NULL) {
        printf("Failed to set lock: %s\n", redis_conn->errstr);
        exit(EXIT_FAILURE);
    }
    if (strcmp(reply->str, "OK") != 0) {
        printf("Failed to acquire lock\n");
        exit(EXIT_FAILURE);
    }
    freeReplyObject(reply);

    // 模擬使用分布式鎖
    printf("Lock acquired, sleeping for 5 seconds\n");
    sleep(5);

    // 釋放分布式鎖
    reply = (redisReply *)redisCommand(redis_conn, "DEL %s", lock_key);
    if (reply == NULL) {
        printf("Failed to release lock: %s\n", redis_conn->errstr);
        exit(EXIT_FAILURE);
    }
    if (reply->integer != 1)
