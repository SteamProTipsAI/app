# steamprotipsai/adapters/screenshot_watcher.py

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from steamprotipsai.core.ports import ScreenshotWatcher
from pathlib import Path
import time
import threading


class RealScreenshotWatcher(ScreenshotWatcher):
    def __init__(self, watch_dir: Path = Path.home() / "Pictures" / "Steam"):
        self.watch_dir = watch_dir

    def watch(self, callback):
        """Starts watching the screenshot folder and calls `callback(path)` on each new image."""

        class Handler(FileSystemEventHandler):
            def on_created(self_inner, event):
                if event.is_directory:
                    return
                path = Path(event.src_path)
                if path.suffix.lower() in [".jpg", ".png"]:
                    print(f"[Watcher] New screenshot: {path}")
                    callback(str(path))

        def run_observer():
            observer = Observer()
            observer.schedule(Handler(), str(self.watch_dir), recursive=False)
            observer.start()
            print(f"[Watcher] Watching folder: {self.watch_dir}")
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                observer.stop()
            observer.join()

        # Run in a daemon thread to avoid blocking the main loop
        thread = threading.Thread(target=run_observer, daemon=True)
        thread.start()
