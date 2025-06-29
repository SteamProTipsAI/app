from unittest.mock import MagicMock
from steamprotipsai.core.app import SteamProTipsApp
from steamprotipsai.core.ports import HotkeyListener, ScreenshotCapturer, GameDetector, GPTClient


def test_app_run_registers_hotkey_callback_and_triggers_flow():
    # Arrange
    mock_listener = MagicMock(spec=HotkeyListener)
    mock_screenshot = MagicMock(spec=ScreenshotCapturer)
    mock_game = MagicMock(spec=GameDetector)
    mock_gpt = MagicMock(spec=GPTClient)

    mock_screenshot.capture.return_value = "mock_screenshot.png"
    mock_game.detect.return_value = "Cool Game"
    mock_gpt.ask_for_tip.return_value = "Here's a cool tip!"

    captured_callback = None

    def capture_callback(callback):
        nonlocal captured_callback
        captured_callback = callback

    mock_listener.listen.side_effect = capture_callback

    # Act
    app = SteamProTipsApp(
        hotkey_listener=mock_listener,
        screenshot_capturer=mock_screenshot,
        game_detector=mock_game,
        gpt_client=mock_gpt
    )
    app.run()

    # Assert: run() registered callback
    mock_listener.listen.assert_called_once()
    assert captured_callback is not None

    # Simulate pressing the hotkey
    captured_callback()

    # Assert: ports called correctly
    mock_screenshot.capture.assert_called_once()
    mock_game.detect.assert_called_once()
    mock_gpt.ask_for_tip.assert_called_once_with(
        "Game: Cool Game. See the attached image. Give a short, practical tip in the style of a 90s magazine.",
        "mock_screenshot.png"
    )


def test_handle_hotkey_calls_ports_in_correct_order():
    call_order = []

    def track_screenshot():
        call_order.append("screenshot")
        return "screen.png"

    def track_game():
        call_order.append("game")
        return "MockGame"

    def track_gpt(prompt, screenshot_path):
        call_order.append("gpt")
        return "AI tip"

    mock_listener = MagicMock(spec=HotkeyListener)
    mock_screenshot = MagicMock(spec=ScreenshotCapturer)
    mock_game = MagicMock(spec=GameDetector)
    mock_gpt = MagicMock(spec=GPTClient)

    mock_screenshot.capture.side_effect = track_screenshot
    mock_game.detect.side_effect = track_game
    mock_gpt.ask_for_tip.side_effect = track_gpt

    captured_callback = None

    def capture_callback(cb):
        nonlocal captured_callback
        captured_callback = cb

    mock_listener.listen.side_effect = capture_callback

    app = SteamProTipsApp(
        hotkey_listener=mock_listener,
        screenshot_capturer=mock_screenshot,
        game_detector=mock_game,
        gpt_client=mock_gpt,
    )

    app.run()
    assert captured_callback is not None

    # Simulate hotkey press
    captured_callback()

    # Assert: call order
    assert call_order == ["screenshot", "game", "gpt"], f"Unexpected call order: {call_order}"
