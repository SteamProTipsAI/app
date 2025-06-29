from steamprotipsai.core.ports import (
    HotkeyListener,
    ScreenshotCapturer,
    GameDetector,
    GPTClient
)


class SteamProTipsApp:
    def __init__(self, hotkey_listener: HotkeyListener, screenshot_capturer: ScreenshotCapturer, game_detector: GameDetector, gpt_client: GPTClient):
        self.hotkey_listener = hotkey_listener
        self.screenshot_capturer = screenshot_capturer
        self.game_detector = game_detector
        self.gpt_client = gpt_client

    def run(self):
        print("SteamProTipsAI iniciado. Pressione o atalho configurado para capturar a tela e obter uma dica!")
        self.hotkey_listener.listen(self.handle_hotkey)

    def handle_hotkey(self):
        print("\nAtalho detectado! Capturando tela...")

        screenshot_path = self.screenshot_capturer.capture()
        game_name = self.game_detector.detect()

        print(f"Jogo detectado: {game_name}")
        print(f"Screenshot salva em: {screenshot_path}")

        prompt = f"Jogo: {game_name}. Veja a imagem anexa. Dê uma dica curta e prática no estilo revista dos anos 90."
        tip = self.gpt_client.ask_for_tip(prompt, screenshot_path)

        print(f"\n💡 Dica encontrada: {tip}\n")
