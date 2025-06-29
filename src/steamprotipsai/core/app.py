from steamprotipsai.core.ports import (
    ScreenshotCapturer,
    GameDetector,
    GPTClient,
    ScreenshotWatcher,
    StatusReporter
)

class SteamProTipsApp:
    def __init__(
        self,
        screenshot_capturer: ScreenshotCapturer,
        game_detector: GameDetector,
        gpt_client: GPTClient,
        screenshot_watcher: ScreenshotWatcher,
        status_reporter: StatusReporter = None,
    ):
        self.screenshot_capturer = screenshot_capturer
        self.game_detector = game_detector
        self.gpt_client = gpt_client
        self.screenshot_watcher = screenshot_watcher,
        self.status_reporter = status_reporter

    def run(self):
        self.screenshot_watcher.watch(self._handle_screenshot)

    def _handle_screenshot(self, path: str):
        if self.status_reporter:
            self.status_reporter.show_message(f"Screenshot detected: {path}")

        try:
            import subprocess
            result = subprocess.run([
                "zenity",
                "--question",
                "--title=SteamProTipsAI",
                "--text=Would you like an AI tip for this moment?"
            ])
            if result.returncode != 0:
                if self.status_reporter:
                    self.status_reporter.show_message("User declined the tip.")
                return
        except FileNotFoundError:
            if self.status_reporter:
                self.status_reporter.show_message("Zenity not found. Skipping prompt...")

        game_name = self.game_detector.detect()
        prompt = f"Game: {game_name}. See the attached image. Give a short, practical tip in the style of a 90s magazine."
        tip = self.gpt_client.ask_for_tip(prompt, path)

        if self.status_reporter:
            self.status_reporter.show_tip(tip)
