mod gui;
mod watcher;

use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        if let Err(e) = watcher::start_watching(tx) {
            eprintln!("Error starting screenshot watcher: {e}");
        }
    });

    for screenshot_path in rx {
        println!("New screenshot detected: {screenshot_path}");
        gui::show_dialog(screenshot_path);
    }
}
