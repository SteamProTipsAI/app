from steamprotipsai.core.ports import GameDetector


class MockGameDetector(GameDetector):
    def detect(self) -> str:
        print("Simulando detecção do jogo...")
        return "Hollow Knight"
