from steamprotipsai.core.app import SteamProTipsApp
from steamprotipsai.adapters.screenshot_watcher import RealScreenshotWatcher
from steamprotipsai.adapters.mock_game_detector import MockGameDetector
from steamprotipsai.adapters.mock_gpt_client import MockGPTClient
from steamprotipsai.adapters.mock_screenshot import MockScreenshotCapturer

try:
    from steamprotipsai.adapters.main_window import MainWindow
    from gi.repository import Gtk
    UI_AVAILABLE = True
except ImportError:
    MainWindow = None
    Gtk = None
    UI_AVAILABLE = False
    print("[SteamProTipsAI] GTK UI not available. Running in headless mode.")

def main():
    ui = MainWindow() if UI_AVAILABLE else None

    app = SteamProTipsApp(
        screenshot_capturer=MockScreenshotCapturer(),
        game_detector=MockGameDetector(),
        gpt_client=MockGPTClient(),
        screenshot_watcher=RealScreenshotWatcher(),
        status_reporter=ui,
    )

    app.run()

    if Gtk:
        Gtk.main()


if __name__ == "__main__":
    main()
