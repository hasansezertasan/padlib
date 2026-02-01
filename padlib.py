"""Reference implementation of the padlib spec."""

from __future__ import annotations

import math


def _apply_fill(padding_len: int, fill_char: str) -> str:
    if not fill_char or padding_len <= 0:
        return ""
    repeats = math.ceil(padding_len / len(fill_char))
    return (fill_char * repeats)[:padding_len]


def left_pad(string: str | None, length: int, fill_char: str = " ") -> str:
    if string is None:
        string = ""
    string = str(string)
    if not fill_char:
        return string
    if length < 0:
        length = 0
    padding_needed = length - len(string)
    if padding_needed <= 0:
        return string
    return _apply_fill(padding_needed, fill_char) + string


def right_pad(string: str | None, length: int, fill_char: str = " ") -> str:
    if string is None:
        string = ""
    string = str(string)
    if not fill_char:
        return string
    if length < 0:
        length = 0
    padding_needed = length - len(string)
    if padding_needed <= 0:
        return string
    return string + _apply_fill(padding_needed, fill_char)


def center_pad(string: str | None, length: int, fill_char: str = " ") -> str:
    if string is None:
        string = ""
    string = str(string)
    if not fill_char:
        return string
    if length < 0:
        length = 0
    total_padding = length - len(string)
    if total_padding <= 0:
        return string
    left = total_padding // 2
    right = total_padding - left  # ceil goes to right
    return _apply_fill(left, fill_char) + string + _apply_fill(right, fill_char)


def pad(
    string: str | None,
    length: int,
    fill_char: str = " ",
    position: str = "left",
) -> str:
    if position not in ("left", "right", "center"):
        raise ValueError(
            f"Invalid position: {position!r}. Must be 'left', 'right', or 'center'."
        )
    if position == "left":
        return left_pad(string, length, fill_char)
    if position == "right":
        return right_pad(string, length, fill_char)
    return center_pad(string, length, fill_char)


def zero_pad(number: int | float | str, length: int) -> str:
    s = str(number)
    if s.startswith("-"):
        return "-" + left_pad(s[1:], length - 1, "0")
    return left_pad(s, length, "0")
