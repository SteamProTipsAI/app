from steamprotipsai.core.ports import GameDetector


class MockGameDetector(GameDetector):
    def detect(self) -> str:
        print("Simulating game detection...")
        return "Steam Pro Tips AI Game"
