use std::path::Path;

mod arken;
mod utils;
// use arken::*;
// use utils::*;

fn main() {
    let url: &str = "https://github.com/arkenfox/user.js/";

    let user: String = utils::whoami::get_username();
    let user: &String = &user;

    let path: String = format!("/home/{}/tmp/arkenfox", user);
    let path: &Path = Path::new(&path);

    // arken::submodule::clone(path, url);
    arken::submodule::copy(path);
}
