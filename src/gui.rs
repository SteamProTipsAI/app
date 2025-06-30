use notify_rust::Notification;

pub fn show_dialog(image_path: String) {
    let result = Notification::new()
        .summary("Steam Pro Tips AI")
        .body("Tap for a tip here...")
        .icon("dialog-question")
        .show();

    match result {
        Ok(_) => println!("Notification shown for: {image_path}"),
        Err(e) => eprintln!("Notification error: {}", e),
    }
}
