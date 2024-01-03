use std::process::Command;

fn main() {
    mirrorlist_backup();
    mirrorlist_update();
}

fn mirrorlist_backup() {
    Command::new("sudo")
        .arg("cp")
        .arg("/etc/pacman.d/mirrorlist")
        .arg("/etc/pacman.d/mirrorlist.bak")
        .output()
        .expect("[-] Mirrorlist backup");

    println!("[+] Mirrorlist backup");
}

fn mirrorlist_update() {
    Command::new("sudo")
        .arg("reflector")
        .arg("--latest")
        .arg("25")
        .arg("--protocol")
        .arg("https")
        .arg("--connection-timeout")
        .arg("5")
        .arg("--sort")
        .arg("rate")
        .arg("--save")
        .arg("/etc/pacman.d/mirrorlist")
        .output()
        .expect("[-] Failed to update mirrorlist");

    println!("[+] Mirrorlist update");
}
