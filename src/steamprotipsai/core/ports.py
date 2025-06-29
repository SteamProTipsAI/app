from abc import ABC, abstractmethod

class ScreenshotWatcher(ABC):
    @abstractmethod
    def watch(self, callback):
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

class StatusReporter(ABC):
    @abstractmethod
    def show_message(self, text: str):
        pass
    @abstractmethod
    def show_tip(self, tip: str):
        pass