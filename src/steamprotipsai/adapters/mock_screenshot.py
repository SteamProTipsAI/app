from steamprotipsai.core.ports import ScreenshotCapturer


class MockScreenshotCapturer(ScreenshotCapturer):
    def capture(self) -> str:
        print("Simulating screenshot...")
        return "mock_screenshot.png"
