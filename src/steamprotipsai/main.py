from steamprotipsai.core.app import SteamProTipsApp
from steamprotipsai.adapters.mock_screenshot import MockScreenshotCapturer
from steamprotipsai.adapters.mock_game_detector import MockGameDetector
from steamprotipsai.adapters.mock_gpt_client import MockGPTClient


def main():
    app = SteamProTipsApp(
        hotkey_listener=EvdevHotkeyListener(key_code="KEY_F24"),
        screenshot_capturer=MockScreenshotCapturer(),
        game_detector=MockGameDetector(),
        gpt_client=MockGPTClient(),
    )
    app.run()


if __name__ == "__main__":
    main()
