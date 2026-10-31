# Guards: <kbd>...</kbd> in Markdown is rendered styled, without the raw tags.
from rich.console import Console
from rich.markdown import Markdown


def test_kbd_tag_is_styled():
    console = Console(width=40, force_terminal=True, color_system="truecolor")
    with console.capture() as capture:
        console.print(Markdown("press <kbd>Ctrl</kbd> now"))
    out = capture.get()
    assert "<kbd>" not in out
    assert "\x1b[1;93mCtrl" in out
