extern crate git2;

pub mod submodule {
    use std::{fs, path::{Path, PathBuf}};

    pub fn clone(path: &Path, url: &str) {
        if path.exists() {
            println!("[i] Clone: Removing existing directory");
            fs::remove_dir_all(path)
                .expect("[-] Clone: Cannot remove directory");
        }

        match git2::Repository::clone(url, path) {
            Ok(repo) => {
                println!("[+] Clone: Cloned repository");
                repo
            }
            Err(e) => panic!("[-] Clone: Failed to clone: {}", e),
        };
    }

    pub fn copy(path: &Path) {
        let files: [&str; 2] = ["updates.sh", "user.js"];

        for entry in fs::read_dir(path).unwrap() {
            println!("{}", entry.unwrap().path().display());

            if entry.contains(&files) {
                println!("Found desired file: {}", files);
                // You can access the full path using entry.path()
            }
        }

    }

    pub fn function() {
        // TODO: copy `~/.config/firefox/preferences/user_overrides.js` to Firefox user profile
    }

    pub fn update() {
        // TODO: run `updater.sh`
    }

    pub fn get_firefox_profile() {
        // TODO: get firefox user profile (default-release)
    }
}
