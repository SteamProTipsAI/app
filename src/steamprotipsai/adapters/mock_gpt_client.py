from steamprotipsai.core.ports import GPTClient


class MockGPTClient(GPTClient):
    def ask_for_tip(self, prompt: str, screenshot_path: str) -> str:
        print(f"Sending prompt to AI (mock) with screenshot (mock): {screenshot_path} {prompt}")
        return "At the top right, after the wooden box, there's a special star that gives you an extra life."
