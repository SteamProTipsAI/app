from steamprotipsai.core.ports import (
    ScreenshotCapturer,
    GameDetector,
    GPTClient,
    ScreenshotWatcher,
)

class SteamProTipsApp:
    def __init__(
        self,
        screenshot_capturer: ScreenshotCapturer,
        game_detector: GameDetector,
        gpt_client: GPTClient,
        screenshot_watcher: ScreenshotWatcher,
    ):
        self.screenshot_capturer = screenshot_capturer
        self.game_detector = game_detector
        self.gpt_client = gpt_client
        self.screenshot_watcher = screenshot_watcher

    def run(self):
        print("SteamProTipsAI started.")
        print("Take a screenshot to receive a tip.")
        self.screenshot_watcher.watch(self._handle_screenshot)

    def _handle_screenshot(self, path: str):
        print(f"\n[Watcher] Screenshot automatically detected: {path}")

        try:
            import subprocess
            result = subprocess.run([
                "zenity",
                "--question",
                "--title=SteamProTipsAI",
                "--text=Would you like an AI tip for this moment?"
            ])
            if result.returncode != 0:
                print("[Watcher] User declined the tip.")
                return
        except FileNotFoundError:
            print("[Watcher] Zenity not found. Skipping prompt...")

        game_name = self.game_detector.detect()
        print(f"[Watcher] Game detected: {game_name}")

        prompt = f"Game: {game_name}. See the attached image. Give a short, practical tip in the style of a 90s magazine."
        tip = self.gpt_client.ask_for_tip(prompt, path)

        print(f"\n💡 Tip received: {tip}\n")
