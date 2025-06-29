from unittest.mock import MagicMock
from steamprotipsai.core.app import SteamProTipsApp
from steamprotipsai.core.ports import HotkeyListener, ScreenshotCapturer, GameDetector, GPTClient


def test_app_invokes_callback_on_hotkey():
    # Arrange: create mocks
    mock_listener = MagicMock(spec=HotkeyListener)
    mock_screenshot = MagicMock(spec=ScreenshotCapturer)
    mock_game = MagicMock(spec=GameDetector)
    mock_gpt = MagicMock(spec=GPTClient)

    mock_screenshot.capture.return_value = "mock_path.png"
    mock_game.detect.return_value = "Mock Game"
    mock_gpt.ask_for_tip.return_value = "Test Tip"

    # Act: create app and run
    app = SteamProTipsApp(
        hotkey_listener=mock_listener,
        screenshot_capturer=mock_screenshot,
        game_detector=mock_game,
        gpt_client=mock_gpt
    )

    # Simulate calling the callback
    app.handle_hotkey()

    # Assert: interactions happened
    mock_screenshot.capture.assert_called_once()
    mock_game.detect.assert_called_once()
    mock_gpt.ask_for_tip.assert_called_once_with(
        "Jogo: Mock Game. Veja a imagem anexa. Dê uma dica curta e prática no estilo revista dos anos 90.",
        "mock_path.png"
    )
