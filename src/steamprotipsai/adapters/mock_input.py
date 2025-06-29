from steamprotipsai.core.ports import HotkeyListener


class MockHotkeyListener(HotkeyListener):
    def listen(self, callback):
        while True:
            user_input = input("\nPressione 'h' para simular o atalho ou 'q' para sair: ").strip().lower()
            if user_input == 'h':
                callback()
            elif user_input == 'q':
                print("Encerrando SteamProTipsAI.")
                break
            else:
                print("Comando não reconhecido.")
