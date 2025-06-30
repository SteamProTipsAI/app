use notify::{Event, EventKind, RecursiveMode, Watcher};
use std::path::PathBuf;
use std::sync::mpsc::Sender;
use std::time::Duration;

pub fn start_watching(tx: Sender<String>) -> notify::Result<()> {
    let path = std::env::var("STEAM_SCREENSHOT_PATH")
        .unwrap_or_else(|_| String::from("C:\\Program Files (x86)\\Steam\\userdata"));

    println!("Observando screenshots em: {path}");

    let mut watcher = notify::recommended_watcher(move |res: Result<Event, notify::Error>| {
        if let Ok(event) = res {
            if matches!(event.kind, EventKind::Create(_)) {
                for path in event.paths {
                    if let Some(ext) = path.extension() {
                        if ext == "jpg" || ext == "png" {
                            println!("Screenshot detectada: {path:?}");
                            let _ = tx.send(path.to_string_lossy().to_string());
                        }
                    }
                }
            }
        }
    })?;

    watcher.watch(&PathBuf::from(path), RecursiveMode::Recursive)?;

    loop {
        std::thread::sleep(Duration::from_secs(10));
    }
}
