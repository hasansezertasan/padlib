# Generating padlib

padlib is a ghost library -- it ships a specification and test cases instead of executable code. To use it, give the files to an AI coding assistant and tell it what language you need.

## Quick Start

Give your coding assistant this prompt:

```
Implement the padlib library in [LANGUAGE].

1. Read SPEC.md for the complete behavioral specification
2. Parse tests.yaml and generate a test file
3. Implement all five functions: left_pad, right_pad, center_pad,
   pad, zero_pad
4. Run tests until all pass

All 111 test cases in tests.yaml must pass. See the "Error Handling"
section in SPEC.md for error behavior.
```

## Verification

After generation, run the test suite. All 111 tests must pass:

| Function     | Tests |
| ------------ | ----- |
| `left_pad`   | 26    |
| `right_pad`  | 13    |
| `center_pad` | 16    |
| `pad`        | 12    |
| `zero_pad`   | 22    |
| Unicode      | 11    |
| Errors       | 11    |
