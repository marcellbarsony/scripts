use std::process::Command;

fn main() {
    qtile_reload();
}

// {{{ Screen
fn qtile () {


}
// }}}

// {{{ Qtile config
fn qtile_reload() {
    Command::new("qtile")
        .arg("cmd-obj")
        .arg("-o")
        .arg("cmd")
        .arg("-f")
        .arg("reload_config")
        .output()
        .expect("[-] Qtile: reload config");
    println!("[+] Qtile: reload config")
}
// }}}

