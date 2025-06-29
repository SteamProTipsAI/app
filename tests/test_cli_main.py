# tests/test_app_uses_hotkey_listener.py

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

    # Act: create app and run callback directly
    app = SteamProTipsApp(
        hotkey_listener=mock_listener,
        screenshot_capturer=mock_screenshot,
        game_detector=mock_game,
        gpt_client=mock_gpt
    )
    app.handle_hotkey()

    # Assert: all components are used as expected
    mock_screenshot.capture.assert_called_once()
    mock_game.detect.assert_called_once()
    mock_gpt.ask_for_tip.assert_called_once_with(
        "Game: Mock Game. See the attached image. Give a short, practical tip in the style of a 90s magazine.",
        "mock_path.png"
    )
