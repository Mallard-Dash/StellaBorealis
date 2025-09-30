# banner.py
# Aurora ASCII banner with optional twinkle, "press any key", and clear-screen.
# Works on Windows/macOS/Linux. Uses 24-bit ANSI colors when available.

import os
import sys
import time
import random
import shutil

APP_NAME = "StellaBorealis"
TAGLINE  = "Budget • Converters • Vehicle Service Log"

# ------------- Terminal utilities -------------

def _supports_truecolor() -> bool:
    # Heuristic: most modern terminals support it.
    if os.environ.get("COLORTERM", "").lower() in ("truecolor", "24bit"):
        return True
    term = os.environ.get("TERM", "").lower()
    return term not in ("dumb", "")

def _rgb(r, g, b, text):
    return f"\x1b[38;2;{r};{g};{b}m{text}\x1b[0m"

def _clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def _center(text, width):
    text = text.rstrip("\n")
    pad = max((width - len(text)) // 2, 0)
    return " " * pad + text

def _move_cursor_up(n: int):
    if n > 0:
        sys.stdout.write(f"\x1b[{n}A")
        sys.stdout.flush()

def _get_terminal_width(default=(80, 24)) -> int:
    try:
        return max(min(shutil.get_terminal_size(default).columns, 120), 60)
    except Exception:
        return 80

# ------------- Keypress (cross-platform) -------------

def _press_any_key(prompt="Press any key to continue..."):
    print(prompt)
    try:
        if os.name == "nt":
            import msvcrt
            msvcrt.getch()
        else:
            import termios, tty
            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    except Exception:
        # Fallback: Enter
        input()

# ------------- Aurora rendering -------------

def _palette():
    # Aurora palette: green -> teal -> blue -> violet
    return [
        (80, 220, 100),
        (50, 200, 190),
        (60, 120, 255),
        (150, 110, 255),
    ]

def _lerp(a, b, t):
    return int(a + (b - a) * t)

def _gradients(n_lines):
    cols = _palette()
    segs = len(cols) - 1
    total = max(n_lines, 1)
    out = []
    for i in range(total):
        pos = i / max(total - 1, 1)
        seg = min(int(pos * segs), segs - 1)
        t = (pos * segs) - seg
        r = _lerp(cols[seg][0], cols[seg + 1][0], t)
        g = _lerp(cols[seg][1], cols[seg + 1][1], t)
        b = _lerp(cols[seg][2], cols[seg + 1][2], t)
        out.append((r, g, b))
    return out

def _wave_line(width, phase):
    import math
    chars = []
    for x in range(width):
        y = 0.5 + 0.5 * math.sin((x / max(width, 1)) * 2 * math.pi + phase)
        if y > 0.85:
            c = "▀"
        elif y > 0.65:
            c = "█"
        elif y > 0.45:
            c = "▄"
        elif y > 0.25:
            c = "▂"
        else:
            c = "·"
        chars.append(c)
    return "".join(chars)

def _render_aurora_block(width, lines=8, phase=0.0, tc=True):
    grads = _gradients(lines)
    for i, (r, g, b) in enumerate(grads):
        wave = _wave_line(width, phase + i * 0.6)
        line = _center(wave, width)
        print(_rgb(r, g, b, line) if tc else line)
    return grads

def _render_title(width, grads, tc=True, app_name=APP_NAME, tagline=TAGLINE):
    # Title with pyfiglet if available
    r, g, b = grads[len(grads) // 2]
    banner = None
    try:
        import pyfiglet  # optional
        banner = pyfiglet.figlet_format(app_name, font="ANSI Shadow")
    except Exception:
        pass

    if banner:
        for row in banner.rstrip("\n").splitlines():
            text = _center(row, width)
            print(_rgb(r, g, b, text) if tc else text)
    else:
        title = f"== {app_name} =="
        text = _center(title, width)
        print(_rgb(r, g, b, text) if tc else text)

    r2, g2, b2 = grads[-1]
    tag = _center(tagline, width)
    print(_rgb(r2, g2, b2, tag) if tc else tag)

# ------------- Twinkle animation -------------

def _twinkle(width, lines=3, frames=24, fps=16, density=0.06):
    """
    Draws a small starfield area that twinkles in-place beneath the title.
    Uses ANSI cursor-up to animate in-place without scrolling.
    """
    tc = _supports_truecolor()
    delay = 1.0 / max(fps, 1)

    # Pre-print empty lines to animate over:
    blank = " " * width
    for _ in range(lines):
        print(blank)

    for _ in range(frames):
        # Move cursor up to overwrite those lines
        _move_cursor_up(lines)
        for _line in range(lines):
            chars = []
            for x in range(width):
                if random.random() < density:
                    # Star brightness & hue
                    r, g, b = random.choice(_palette())
                    # boost a bit for stars
                    br = min(r + 80, 255)
                    bg = min(g + 80, 255)
                    bb = min(b + 80, 255)
                    c = random.choice(("·", "•", "✦", "✧", "⋆"))
                    chars.append(_rgb(br, bg, bb, c) if tc else "*")
                else:
                    chars.append(" ")
            line = "".join(chars)
            print(line)
        sys.stdout.flush()
        time.sleep(delay)

# ------------- Public API -------------

def show_banner(animate=True, aurora_lines=8, twinkle_lines=3, twinkle_frames=24, fps=16,
                press_key=True, clear_before=False, clear_after=True):
    """
    Render the aurora banner, optional twinkle, wait for a key, and clear screen.

    Parameters:
        animate: bool        -> enable twinkle animation
        aurora_lines: int    -> number of aurora rows
        twinkle_lines: int   -> number of animated star lines
        twinkle_frames: int  -> frames of twinkle
        fps: int             -> frames per second for twinkle
        press_key: bool      -> wait for a key after banner
        clear_before: bool   -> clear screen before drawing
        clear_after: bool    -> clear screen after keypress
    """
    width = _get_terminal_width()
    if clear_before:
        _clear_screen()
    tc = _supports_truecolor()

    grads = _render_aurora_block(width, lines=aurora_lines, phase=0.0, tc=tc)
    _render_title(width, grads, tc=tc, app_name=APP_NAME, tagline=TAGLINE)

    if animate:
        _twinkle(width, lines=twinkle_lines, frames=twinkle_frames, fps=fps)

    if press_key:
        print()
        _press_any_key("Press any key to continue...")

    if clear_after:
        _clear_screen()

# ------------- Demo -------------
if __name__ == "__main__":
    show_banner()
