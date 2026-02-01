# padlib Specification

This document describes the behavior of the `padlib` library. Any implementation must conform to this specification and pass all tests in `tests.yaml`.

## Overview

`padlib` provides string padding utilities. It handles padding strings to a target length with customizable fill characters, supporting left, right, and center alignment.

## Functions

The library provides five functions:

1. `left_pad(string, length, fill_char)` - Pad on the left
2. `right_pad(string, length, fill_char)` - Pad on the right
3. `center_pad(string, length, fill_char)` - Center the string
4. `pad(string, length, fill_char, position)` - General-purpose padding
5. `zero_pad(number, length)` - Pad numbers with leading zeros

---

## Function: `left_pad`

Pads a string on the left side to reach a target length.

### Signature

```
left_pad(string, length, fill_char=' ') -> string
```

### Parameters

| Parameter   | Type    | Required | Default       | Description                     |
| ----------- | ------- | -------- | ------------- | ------------------------------- |
| `string`    | string  | Yes      | -             | The input string to pad         |
| `length`    | integer | Yes      | -             | The target length               |
| `fill_char` | string  | No       | `' '` (space) | Character(s) to use for padding |

### Behavior

1. If `string` length >= `length`, return `string` unchanged
2. If `length` is negative, treat as 0 (return `string` unchanged)
3. Calculate padding needed: `length - len(string)`
4. Prepend `fill_char` repeated as needed to reach target length
5. If `fill_char` is longer than 1 character, repeat the pattern and truncate to exact length needed

### Examples

```
left_pad("foo", 5)         -> "  foo"
left_pad("foo", 5, "-")    -> "--foo"
left_pad("foo", 5, "ab")   -> "abfoo"
left_pad("foobar", 5)      -> "foobar"  # Already >= target length
left_pad("foo", 10, "abc") -> "abcabcafoo"  # Pattern repeats, truncates
left_pad("", 3)            -> "   "
left_pad("x", 0)           -> "x"
left_pad("x", -5)          -> "x"
```

### Edge Cases

- Empty string input: Pad entirely with fill characters
- Empty fill character: Return string unchanged (no padding possible)
- Unicode: Measure length by characters (code points), not bytes
- Null/None input: Convert to empty string first

---

## Function: `right_pad`

Pads a string on the right side to reach a target length.

### Signature

```
right_pad(string, length, fill_char=' ') -> string
```

### Parameters

Same as `left_pad`.

### Behavior

1. If `string` length >= `length`, return `string` unchanged
2. If `length` is negative, treat as 0 (return `string` unchanged)
3. Calculate padding needed: `length - len(string)`
4. Append `fill_char` repeated as needed to reach target length
5. If `fill_char` is longer than 1 character, repeat the pattern and truncate

### Examples

```
right_pad("foo", 5)         -> "foo  "
right_pad("foo", 5, "-")    -> "foo--"
right_pad("foo", 5, "ab")   -> "fooab"
right_pad("foobar", 5)      -> "foobar"
right_pad("foo", 10, "abc") -> "fooabcabca"
right_pad("", 3)            -> "   "
```

---

## Function: `center_pad`

Centers a string within a target length, padding both sides.

### Signature

```
center_pad(string, length, fill_char=' ') -> string
```

### Parameters

Same as `left_pad`.

### Behavior

1. If `string` length >= `length`, return `string` unchanged
2. Calculate total padding needed: `length - len(string)`
3. Left padding: `floor(total_padding / 2)`
4. Right padding: `ceil(total_padding / 2)` (extra character goes on right)
5. Apply padding on both sides

### Examples

```
center_pad("foo", 7)         -> "  foo  "
center_pad("foo", 8)         -> "  foo   "  # Extra space on right
center_pad("foo", 8, "-")    -> "--foo---"
center_pad("x", 5)           -> "  x  "
center_pad("foobar", 5)      -> "foobar"
center_pad("ab", 6, "xyz")   -> "xyabxy"  # Pattern applied to both sides
```

### Edge Cases

- Odd padding amount: Extra character goes on the right side
- Multi-char fill: Each side gets its own pattern application

---

## Function: `pad`

General-purpose padding function with position control.

### Signature

```
pad(string, length, fill_char=' ', position='left') -> string
```

### Parameters

| Parameter   | Type    | Required | Default  | Description                                      |
| ----------- | ------- | -------- | -------- | ------------------------------------------------ |
| `string`    | string  | Yes      | -        | The input string to pad                          |
| `length`    | integer | Yes      | -        | The target length                                |
| `fill_char` | string  | No       | `' '`    | Character(s) to use for padding                  |
| `position`  | string  | No       | `'left'` | Where to pad: `'left'`, `'right'`, or `'center'` |

### Behavior

Delegates to the appropriate function based on `position`:

- `'left'` -> `left_pad`
- `'right'` -> `right_pad`
- `'center'` -> `center_pad`

Invalid position values should raise an error or exception.

### Examples

```
pad("foo", 5)                    -> "  foo"
pad("foo", 5, "-", "left")       -> "--foo"
pad("foo", 5, "-", "right")      -> "foo--"
pad("foo", 7, "-", "center")     -> "--foo--"
pad("foo", 5, position="right")  -> "foo  "  # Named argument
```

---

## Function: `zero_pad`

Pads numbers with leading zeros. Convenience function for common use case.

### Signature

```
zero_pad(number, length) -> string
```

### Parameters

| Parameter | Type             | Required | Description       |
| --------- | ---------------- | -------- | ----------------- |
| `number`  | number or string | Yes      | The number to pad |
| `length`  | integer          | Yes      | The target length |

### Behavior

1. Convert `number` to string if needed
2. If number is negative, preserve the sign and pad the digits
3. Apply `left_pad` with `fill_char='0'`

### Examples

```
zero_pad(5, 3)      -> "005"
zero_pad(42, 5)     -> "00042"
zero_pad(12345, 3)  -> "12345"  # Already exceeds length
zero_pad("7", 4)    -> "0007"   # String input accepted
zero_pad(-5, 4)     -> "-005"   # Negative: sign preserved, digits padded
zero_pad(0, 3)      -> "000"
zero_pad(3.14, 6)   -> "003.14" # Floats: pad the whole representation
```

### Edge Cases

- Negative numbers: Pad after the minus sign (e.g., `-5` with length 4 -> `-005`)
- Floats: Treat decimal point and decimals as part of the string
- String input: Accept strings that represent numbers

---

## Unicode Handling

All functions measure string length by **characters (code points)**, not bytes.

```
left_pad("", 3)     -> "  "   # emoji is 1 character
left_pad("caf", 6)    -> "  caf"  # accent is 1 character
```

For languages with different string models:

- Python 3: Use `len()` which counts code points
- JavaScript: Use `[...string].length` for accurate count
- Rust: Use `.chars().count()`

---

## Error Handling

### Required Errors

These conditions should raise an error/exception:

1. `pad` with invalid `position` value (not 'left', 'right', or 'center')
2. `length` that is not an integer (or cannot be converted to one)

### Graceful Handling

These conditions should be handled gracefully:

1. `None`/`null` string input: Treat as empty string
2. Negative length: Treat as 0 (return string unchanged)
3. Empty fill character: Return string unchanged
4. Non-string input for `string`: Convert to string first

---

## Implementation Notes

### Performance

For typical use cases (strings under 1000 characters, padding under 100 characters), performance is not critical. Implementations may use simple string concatenation.

For high-performance needs, consider:

- Pre-allocating the result buffer
- Avoiding repeated string concatenation in loops

### Thread Safety

All functions should be pure (no side effects) and thread-safe.

### Immutability

Input strings should never be modified. Always return a new string.

---

## Changelog

- **v1.0.0** (2026-01-19): Initial specification
