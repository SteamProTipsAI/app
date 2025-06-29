from unittest.mock import MagicMock, call
from steamprotipsai.core.app import SteamProTipsApp
from steamprotipsai.core.ports import HotkeyListener, ScreenshotCapturer, GameDetector, GPTClient


def test_app_run_triggers_listener_and_handles_hotkey():
    # Arrange
    mock_listener = MagicMock(spec=HotkeyListener)
    mock_screenshot = MagicMock(spec=ScreenshotCapturer)
    mock_game = MagicMock(spec=GameDetector)
    mock_gpt = MagicMock(spec=GPTClient)

    mock_screenshot.capture.return_value = "mock_screenshot.png"
    mock_game.detect.return_value = "Cool Game"
    mock_gpt.ask_for_tip.return_value = "Here's a cool tip!"

    # Capture the callback
    callback_captured = None

    def capture_callback(callback):
        nonlocal callback_captured
        callback_captured = callback

    mock_listener.listen.side_effect = capture_callback

    # Act
    app = SteamProTipsApp(
        hotkey_listener=mock_listener,
        screenshot_capturer=mock_screenshot,
        game_detector=mock_game,
        gpt_client=mock_gpt
    )
    app.run()  # this should register the callback
    assert callback_captured is not None, "Callback was not passed to listen()"

    # Simulate hotkey press
    callback_captured()

    # Assert
    mock_listener.listen.assert_called_once()
    mock_screenshot.capture.assert_called_once()
    mock_game.detect.assert_called_once()
    mock_gpt.ask_for_tip.assert_called_once_with(
        "Game: Cool Game. See the attached image. Give a short, practical tip in the style of a 90s magazine.",
        "mock_screenshot.png"
    )
