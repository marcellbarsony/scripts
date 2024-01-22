extern crate git2;

pub mod submodule {
    use std::{fs, path::Path};

    pub fn clone() {
        let url: &str = "https://github.com/arkenfox/user.js/";
        let dst: &Path = Path::new("/home/marci/Downloads/arkenfox"); // TODO: get_current_username

        if dst.exists() {
            println!("[i] Directory exists");
            println!("[i] Removing directory");
            fs::remove_dir_all(dst)
                .expect("[-] Cannot remove directory");
        }

        let _repo = match git2::Repository::clone(url, dst) {
            Ok(repo) => repo,
            Err(e) => panic!("[-] Failed to clone: {}", e),
        };
    }

    pub fn copy() {
        // Create a vector
        let mut destination_paths: Vec<_> = Vec::new();

        let files: &[&str; 2] = &["updates.sh", "user.js"];
        let src: &Path = Path::new("/home/marci/Downloads/arkenfox"); // TODO: get_current_username
        let dst: &Path = Path::new("/home/marci/"); // TODO: get_current_username & get Firefox user profile

        for file in files {
            let src_path = src.join(Path::new(file));
            let dst_path = dst.join(Path::new(file));
            println!("{:?}", src_path);
            println!("{:?}", dst_path);
            if src_path.exists() {
                destination_paths.push(dst_path);
            }
        }

        for dst_path in destination_paths {
            if !destination_path.exists() {
                let result = fs::copy(source_path, destination_path);

                if result.is_ok() {
                    println!("File copied successfully: {}", destination_path.as_path().display());
                } else {
                    println!("Error copying file: {}", destination_path.as_path().display());
                }
            } else {
                println!("File already exists: {}", destination_path.as_path().display());
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
