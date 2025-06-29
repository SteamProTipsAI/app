from steamprotipsai.core.app import SteamProTipsApp
from steamprotipsai.adapters.screenshot_watcher import RealScreenshotWatcher
from steamprotipsai.adapters.mock_game_detector import MockGameDetector
from steamprotipsai.adapters.mock_gpt_client import MockGPTClient
from steamprotipsai.adapters.mock_screenshot import MockScreenshotCapturer
from steamprotipsai.adapters.main_window import MainWindow
from gi.repository import Gtk

def main():
    ui = MainWindow()

    app = SteamProTipsApp(
        screenshot_capturer=MockScreenshotCapturer(),
        game_detector=MockGameDetector(),
        gpt_client=MockGPTClient(),
        screenshot_watcher=RealScreenshotWatcher(),
        status_reporter=ui,
    )

    app.run()
    Gtk.main()

if __name__ == "__main__":
    main()
