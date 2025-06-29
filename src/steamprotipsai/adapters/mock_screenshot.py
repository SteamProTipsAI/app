from steamprotipsai.core.ports import ScreenshotCapturer


class MockScreenshotCapturer(ScreenshotCapturer):
    def capture(self) -> str:
        print("Simulando captura de tela...")
        return "mock_screenshot.png"
