import os
import datetime
import traceback

log_path = os.path.expanduser("~/.local/share/steamprotipsai/log.txt")
os.makedirs(os.path.dirname(log_path), exist_ok=True)

def log(msg):
    with open(log_path, "a") as f:
        f.write(f"[{datetime.datetime.now()}] {msg}\n")

log("SteamProTipsAI starting...")

from steamprotipsai.core.app import SteamProTipsApp
from steamprotipsai.adapters.screenshot_watcher import RealScreenshotWatcher
from steamprotipsai.adapters.mock_game_detector import MockGameDetector
from steamprotipsai.adapters.mock_gpt_client import MockGPTClient
from steamprotipsai.adapters.mock_screenshot import MockScreenshotCapturer

try:
    from steamprotipsai.adapters.main_window import MainWindow
    from gi.repository import Gtk
    UI_AVAILABLE = True
    log("GTK UI is available.")
except ImportError:
    MainWindow = None
    Gtk = None
    UI_AVAILABLE = False
    log("GTK UI not available. Running in headless mode.")

def main():
    try:
        ui = MainWindow() if UI_AVAILABLE else None

        app = SteamProTipsApp(
            screenshot_capturer=MockScreenshotCapturer(),
            game_detector=MockGameDetector(),
            gpt_client=MockGPTClient(),
            screenshot_watcher=RealScreenshotWatcher(),
            status_reporter=ui,
        )

        log("App initialized, starting watcher...")
        app.run()

        if Gtk:
            log("Calling Gtk.main()")
            Gtk.main()
        else:
            log("Gtk is not available, exiting.")
    except Exception as e:
        log("Unhandled exception:")
        log(traceback.format_exc())

if __name__ == "__main__":
    main()
