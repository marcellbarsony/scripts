// Users
// https://crates.io/crates/whoami
// https://docs.rs/whoami/latest/whoami/

pub mod whoami {
    pub fn get_username() -> String {
        return whoami::username()
    }
}
