use std::{env, fs, path::PathBuf};

fn main() {

    // Create file
    let file_path = make_file();

    // Discover file
    discover_files();

    // Generate encryption key
    // Encrypt files
}

fn make_file() -> PathBuf {
    println!("Creating file ... ");

    // Create file
    let cwd = env::current_dir().unwrap();
    let path = cwd.join("file.txt");
    fs::File::create(&path).unwrap();

    // Write to file
    let content: &str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.";
    fs::write(&path, content)
        .expect("Cannot write to file");

    cwd
}

fn discover_files() {
    println!("Discovering files ...");
}

