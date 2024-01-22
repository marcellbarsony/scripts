// Users
// https://crates.io/crates/users/0.11.0
// https://docs.rs/users/latest/users/
// WARNING: users is unmaintained
use users::get_current_username;


pub fn get_user() {
    let current_user = match get_current_username() {
        Some(uname) => println!("Running as user with name {:?}", uname),
        None        => println!("The current user does not exist!"),
    };
}
