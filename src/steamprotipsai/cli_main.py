from steamprotipsai.core.app import SteamProTipsApp
from steamprotipsai.adapters.mock_input import MockHotkeyListener
from steamprotipsai.adapters.mock_screenshot import MockScreenshotCapturer
from steamprotipsai.adapters.mock_game_detector import MockGameDetector
from steamprotipsai.adapters.mock_gpt_client import MockGPTClient


def main():
    app = SteamProTipsApp(
        hotkey_listener=MockHotkeyListener(),
        screenshot_capturer=MockScreenshotCapturer(),
        game_detector=MockGameDetector(),
        gpt_client=MockGPTClient(),
    )
    app.run()


if __name__ == "__main__":
    main()
