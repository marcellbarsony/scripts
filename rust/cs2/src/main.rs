use std::process::Command;

fn main() {
    compositor();
    vpn();
    screens();
    qtile_reload();
}

// {{{ Compositor
fn compositor() {
    Command::new("pkill")
        .arg("picom")
        .output()
        .expect("[-] Compositor: disabled");
    println!("[+] Compositor: disabled")
}
// }}}

// {{{ VPN
fn vpn() {
    let wg_interface = vec!["wg0", "wg1", "wg2", "wg3", "wg4", "wg5", "wg6", "wg7", "wg8", "wg9"];

    for interface in wg_interface {
        Command::new("nmcli")
            .arg("connection")
            .arg("down")
            .arg(interface)
            .output()
            .expect("[-] VPN: disabled");
    }
    println!("[+] VPN: disabled");
}
// }}}

// {{{ Screens
fn screens() {
    // https://github.com/ValveSoftware/csgo-osx-linux/issues/3262
    // https://www.reddit.com/r/linux_gaming/comments/17nulbp/comment/k7ufdmo/

    // TODO: Check for monitors (xrandr)

    let screens = vec!["DP-1", "DP-2", "DP-3", "DP-4", "DP-5", "DP-6", "DP-7", "DP-8"];

    for screen in screens {
        Command::new("xrandr")
            .arg("--output")
            .arg(screen)
            .arg("--off")
            .output()
            .expect("failed to execute nmcli");
        println!("[+] Screen: {} disabled", screen);
    }

    Command::new("xrandr")
        .arg("--output")
        .arg("DP-9")
        .arg("--mode")
        .arg("1280x960")
        .arg("--rate")
        .arg("60")
        .arg("--pos")
        .arg("0x0")
        .arg("--rotate")
        .arg("normal")
        .output()
        .expect("[-] Set screen: DP-9");
    println!("[+] Set screen: DP-9");
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
