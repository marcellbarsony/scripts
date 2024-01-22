#[derive(Debug)]
struct Object {
    num: u8,
    string: String,
}

impl Object {
    fn new(name: String, num: u8) -> Object {
        Object { num, string: name }
    }

    fn set_num(&mut self, num: u8) {
        self.num = num;
    }
}

fn main() {
    std::fs::write("foo.txt", "Lorem ipsum").unwrap();
    let mut object1 = Object {
        num: 30,
        string: String::from("Heap"),
    };
    let mut object1 = Object {
        num: 30,
        string: String::from("Heap"),
    };
    object1.set_num(40);
    let object2 = Object::new(String::from("Valami"), 32);
    println!("Struct num: {}", object1.num);
    println!("Struct num: {:#?}", object1);
    println!("Struct string: {:#?}", object2);

    let error_codes: [i32; 3] = [200, 404, 500];

    // Access by slice
    let codes = &error_codes[1..2];

    println!("{:?}", codes);
}
