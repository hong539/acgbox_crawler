// 使用Redis作為消息隊列
use redis::{Client, Commands};

fn main() {
    let client = Client::open("redis://127.0.0.1/").unwrap();
    let con = client.get_connection().unwrap();

    // 發佈消息到隊列中
    let _: () = con.lpush("my_queue", "message1").unwrap();
    let _: () = con.lpush("my_queue", "message2").unwrap();

    // 從隊列中讀取消息
    loop {
        let msg: Option<String> = con.brpop("my_queue", 0).unwrap();
        match msg {
            Some(value) => println!("Got message: {}", value),
            None => break,
        }
    }
}