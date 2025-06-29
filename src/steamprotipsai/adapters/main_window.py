import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
from steamprotipsai.core.ports import StatusReporter

class MainWindow(StatusReporter):
    def __init__(self):
        self.window = Gtk.Window(title="SteamProTipsAI")
        self.window.set_default_size(400, 150)
        self.window.set_position(Gtk.WindowPosition.CENTER)
        self.window.connect("destroy", Gtk.main_quit)

        self.label = Gtk.Label(label="Starting SteamProTipsAI...")
        self.label.set_line_wrap(True)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_margin_top(20)
        box.set_margin_bottom(20)
        box.set_margin_start(20)
        box.set_margin_end(20)
        box.pack_start(self.label, True, True, 0)

        self.window.add(box)
        self.window.show_all()

    def show_message(self, text: str):
        GLib.idle_add(self.label.set_text, text)

    def show_tip(self, tip: str):
        GLib.idle_add(self.label.set_text, f"💡 {tip}")
