mod gui;
mod watcher;

use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        if let Err(e) = watcher::start_watching(tx) {
            eprintln!("Erro ao iniciar watcher: {e}");
        }
    });

    for screenshot_path in rx {
        println!("Nova screenshot detectada: {screenshot_path}");
        gui::show_dialog(screenshot_path);
    }
}
