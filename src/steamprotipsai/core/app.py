from steamprotipsai.core.ports import (
    HotkeyListener,
    ScreenshotCapturer,
    GameDetector,
    GPTClient
)


class SteamProTipsApp:
    def __init__(
        self,
        hotkey_listener: HotkeyListener,
        screenshot_capturer: ScreenshotCapturer,
        game_detector: GameDetector,
        gpt_client: GPTClient
    ):
        self.hotkey_listener = hotkey_listener
        self.screenshot_capturer = screenshot_capturer
        self.game_detector = game_detector
        self.gpt_client = gpt_client

    def run(self):
        print("SteamProTipsAI started. Press the configured shortcut to capture the screen and get a tip!")
        self.hotkey_listener.listen(self.handle_hotkey)

    def handle_hotkey(self):
        print("\nShortcut detected! Capturing screen...")

        screenshot_path = self.screenshot_capturer.capture()
        game_name = self.game_detector.detect()

        print(f"Game detected: {game_name}")
        print(f"Screenshot saved at: {screenshot_path}")

        prompt = f"Game: {game_name}. See the attached image. Give a short, practical tip in the style of a 90s magazine."
        tip = self.gpt_client.ask_for_tip(prompt, screenshot_path)

        print(f"\n💡 Tip received: {tip}\n")
