use gtk4::prelude::*;
use gtk4::{Application, ApplicationWindow, Button, Label, Box as GtkBox, Orientation};

pub fn show_dialog(image_path: String) {
    let app = Application::builder()
        .application_id("com.steamprotips.Gui")
        .build();

    app.connect_activate(move |app| {
        let vbox = GtkBox::new(Orientation::Vertical, 12);
        let label = Label::new(Some("Want some tips for this moment?"));
        let button = Button::with_label("Sure!");

        let img_path = image_path.clone();
        button.connect_clicked(move |_| {
            println!("User wants a tip for: {}", img_path);
        });

        vbox.append(&label);
        vbox.append(&button);

        let win = ApplicationWindow::builder()
            .application(app)
            .title("Steam Pro Tips AI")
            .child(&vbox)
            .default_width(300)
            .default_height(100)
            .build();

        win.show();
    });

    app.run();
}
