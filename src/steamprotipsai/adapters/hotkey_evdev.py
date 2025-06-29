# src/steamprotipsai/adapters/hotkey_evdev.py

import evdev
from evdev import InputDevice, categorize, ecodes
from steamprotipsai.core.ports import HotkeyListener


class EvdevHotkeyListener(HotkeyListener):
    """
    Hotkey listener that uses evdev to capture global keyboard input,
    suitable for use on Steam Deck or other Linux devices with direct input access.
    """

    def __init__(self, key_code="KEY_F24"):
        self.key_code = key_code

    def listen(self, callback):
        print(f"Listening for hotkey ({self.key_code}) via evdev...")

        # Get all input devices
        devices = [InputDevice(path) for path in evdev.list_devices()]
        keyboards = [dev for dev in devices if "keyboard" in dev.name.lower() or "kbd" in dev.name.lower()]

        if not keyboards:
            print("No keyboard-like input device found via evdev.")
            return

        for dev in keyboards:
            print(f"Listening to: {dev.path} - {dev.name}")
            try:
                dev.grab()  # optional: prevent propagation
            except OSError:
                print(f"Could not grab device: {dev.path}")

        try:
            while True:
                for dev in keyboards:
                    try:
                        for event in dev.read():
                            if event.type == ecodes.EV_KEY:
                                key_event = categorize(event)
                                if (
                                    key_event.keystate == key_event.key_down
                                    and key_event.keycode == self.key_code
                                ):
                                    print(f"Hotkey ({self.key_code}) detected.")
                                    callback()
                    except BlockingIOError:
                        continue
                    except Exception as e:
                        print(f"⚠️ Error reading device {dev.path}: {e}")
        except KeyboardInterrupt:
            print("Listener interrupted by user.")
        finally:
            for dev in keyboards:
                try:
                    dev.ungrab()
                except Exception:
                    pass
