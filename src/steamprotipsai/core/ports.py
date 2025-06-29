from abc import ABC, abstractmethod


class HotkeyListener(ABC):
    @abstractmethod
    def listen(self, callback):
        pass


class ScreenshotCapturer(ABC):
    @abstractmethod
    def capture(self) -> str:
        pass


class GameDetector(ABC):
    @abstractmethod
    def detect(self) -> str:
        pass


class GPTClient(ABC):
    @abstractmethod
    def ask_for_tip(self, prompt: str, screenshot_path: str) -> str:
        pass
