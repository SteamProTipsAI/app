use notify_rust::Notification;

pub fn show_dialog(image_path: String) {
    let result = Notification::new()
        .summary("Steam Pro Tips AI")
        .body("Want a tip for this moment?")
        .icon("dialog-question")
        .action("yes", "Sure!")
        .action("no", "No thanks")
        .show()
        .and_then(|handle| handle.wait_for_action());

    match result {
        Ok("yes") => {
            println!("User accepted tip for: {image_path}");
            // Call AI logic here
        }
        Ok("no") => {
            println!("User declined tip for: {image_path}");
        }
        Ok(_) => {}
        Err(e) => {
            eprintln!("Notification error: {}", e);
        }
    }
}
