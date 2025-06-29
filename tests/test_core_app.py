from unittest.mock import MagicMock
from steamprotipsai.core.app import SteamProTipsApp
from steamprotipsai.core.ports import ScreenshotCapturer, GameDetector, GPTClient, ScreenshotWatcher


def test_app_triggers_tip_flow_on_screenshot():
    # Arrange
    mock_screenshot = MagicMock(spec=ScreenshotCapturer)
    mock_game = MagicMock(spec=GameDetector)
    mock_gpt = MagicMock(spec=GPTClient)
    mock_watcher = MagicMock(spec=ScreenshotWatcher)

    mock_game.detect.return_value = "TestGame"
    mock_gpt.ask_for_tip.return_value = "Here is a tip."

    captured_callback = None

    def watch_side_effect(callback):
        nonlocal captured_callback
        captured_callback = callback

    mock_watcher.watch.side_effect = watch_side_effect

    app = SteamProTipsApp(
        screenshot_capturer=mock_screenshot,
        game_detector=mock_game,
        gpt_client=mock_gpt,
        screenshot_watcher=mock_watcher,
    )

    # Act
    app.run()

    # Assert watcher started
    mock_watcher.watch.assert_called_once()
    assert captured_callback is not None

    # Simulate screenshot detection (bypassing zenity)
    app._handle_screenshot = SteamProTipsApp._handle_screenshot.__get__(app)
    SteamProTipsApp._handle_screenshot.__globals__["subprocess"] = MagicMock()
    SteamProTipsApp._handle_screenshot.__globals__["subprocess"].run.return_value.returncode = 0

    captured_callback("new_screenshot.png")

    # Assert ports called
    mock_game.detect.assert_called_once()
    mock_gpt.ask_for_tip.assert_called_once_with(
        "Game: TestGame. See the attached image. Give a short, practical tip in the style of a 90s magazine.",
        "new_screenshot.png"
    )
