from steamprotipsai.core.ports import GPTClient


class MockGPTClient(GPTClient):
    def ask_for_tip(self, prompt: str, screenshot_path: str) -> str:
        print(f"Enviando prompt para IA (mock): {prompt}")
        return "No canto superior direito, depois da caixa de madeira, tem uma estrela especial que te dá uma vida extra."
