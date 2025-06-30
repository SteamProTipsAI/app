use notify::{Event, EventKind, RecursiveMode, Watcher};
use std::path::{Path, PathBuf};
use std::sync::mpsc::Sender;
use std::thread;
use std::time::Duration;
use std::fs;
use dirs_next;

pub fn start_watching(tx: Sender<String>) -> notify::Result<()> {
    let base_path = dirs_next::home_dir()
        .map(|home| home.join(".local/share/Steam/userdata"))
        .expect("Failed to locate home directory");

    println!("Watching for screenshots under: {}", base_path.display());

    let screenshot_dirs = find_screenshot_dirs(&base_path);

    if screenshot_dirs.is_empty() {
        println!("No screenshot directories found.");
    }

    let mut watcher = notify::recommended_watcher(move |res: Result<Event, notify::Error>| {
        if let Ok(event) = res {
            if matches!(event.kind, EventKind::Create(_)) {
                for path in event.paths {
                    if let Some(ext) = path.extension() {
                        if ext == "jpg" || ext == "png" {
                            println!("Screenshot detected: {path:?}");
                            let _ = tx.send(path.to_string_lossy().to_string());
                        }
                    }
                }
            }
        }
    })?;

    for dir in &screenshot_dirs {
        println!("Watching: {}", dir.display());
        watcher.watch(dir, RecursiveMode::NonRecursive)?;
    }

    loop {
        thread::sleep(Duration::from_secs(10));
    }
}

fn find_screenshot_dirs(base: &Path) -> Vec<PathBuf> {
    let mut result = Vec::new();

    if let Ok(user_dirs) = fs::read_dir(base) {
        for user_entry in user_dirs.flatten() {
            let user_path = user_entry.path();
            let remote_path = user_path.join("760/remote");

            if let Ok(game_dirs) = fs::read_dir(remote_path) {
                for game_entry in game_dirs.flatten() {
                    let screenshots_path = game_entry.path().join("screenshots");
                    if screenshots_path.is_dir() {
                        result.push(screenshots_path);
                    }
                }
            }
        }
    }

    result
}
