// 使用Redis作為分布式鎖
use redis::{Client, Commands};
use std::thread::sleep;
use std::time::Duration;

fn acquire_lock(conn: &redis::Connection, lock_name: &str, timeout: u64) -> bool {
    let expiration = timeout + 1;
    let lock = redis::RedisResult::Ok(conn.set_nx(lock_name, 1)?);
    if lock.is_err() {
        return false;
    }
    let _: () = redis::RedisResult::Ok(conn.expire(lock_name, expiration)?);
    true
}

fn release_lock(conn: &redis::Connection, lock_name: &str) -> bool {
    let lock = redis::RedisResult::Ok(conn.del(lock_name)?);
    if lock.is_err() {
        return false;
    }
    true
}

fn main() {
    let client = Client::open("redis://127.0.0.1/").unwrap();
    let conn = client.get_connection().unwrap();
    let lock_name = "my_lock";
    let timeout = 5;

    // 取得分布式鎖
    while !acquire_lock(&conn, lock_name, timeout) {
        sleep(Duration::from_millis(100));
    }

    // 在獲取到分布式鎖的情況下，進行需要鎖定的操作
    println!("Locked!");

    // 釋放分布式鎖
    release_lock(&conn, lock_name);
    println!("Unlocked!");
}