extern crate git2;

pub fn my_function() {
    println!("Hello world");
}

pub fn my_function2() {
    let url = "https://github.com/alexcrichton/git2-rs";
    let repo = match git2::Repository::clone(url, "/home/marci/Downloads2/git2") {
        Ok(repo) => repo,
        Err(e) => panic!("Failed to clone: {}", e),
    };
}
