import threading
import time
import pytest

from steamprotipsai.adapters.hotkey_evdev import EvdevHotkeyListener

evdev_available = sys.platform.startswith("linux")

@pytest.mark.skipif(not evdev_available, reason="Only runs on Linux with evdev")
def test_evdev_hotkey_listener_detects_key(monkeypatch):
    """
    This test runs the listener and asks the user to press F24 (or equivalent mapped button).
    Used for manual integration testing only.
    """

    triggered = {"value": False}

    def fake_callback():
        triggered["value"] = True
        print("✅ Callback triggered!")

    listener = EvdevHotkeyListener(key_code="KEY_F24")

    # Run in separate thread to allow manual key press
    thread = threading.Thread(target=listener.listen, args=(fake_callback,), daemon=True)
    thread.start()

    print("🎮 Please press the configured hotkey (F24 or mapped) within 10 seconds...")
    time.sleep(10)

    assert triggered["value"], "Hotkey was not detected!"
