# Installing padlib

`padlib` is a spec-only library. It contains no code, only a specification and tests. You generate the implementation yourself using an AI coding assistant.

## Quick Start

1. Copy the prompt below
2. Paste it into your AI assistant (Claude, ChatGPT, Cursor, Copilot, etc.)
3. Replace `[LANGUAGE]` with your target language
4. The assistant will generate a working implementation

## The Prompt

```
I need you to implement the `padlib` library in [LANGUAGE].

Please read these files from the padlib-spec repository:
- SPEC.md - The complete behavioral specification
- tests.yaml - All test cases that must pass

Implement all five functions:
1. left_pad(string, length, fill_char=' ')
2. right_pad(string, length, fill_char=' ')
3. center_pad(string, length, fill_char=' ')
4. pad(string, length, fill_char=' ', position='left')
5. zero_pad(number, length)

Requirements:
- Follow the specification exactly
- Handle all edge cases documented in SPEC.md
- Ensure all tests in tests.yaml pass
- Use idiomatic [LANGUAGE] style
- Include type hints/annotations if the language supports them

After implementation, run through the test cases to verify correctness.
```

## Alternative: Direct File References

If you're using an AI assistant that can read files directly (like Claude Code, Cursor, or GitHub Copilot), you can simply say:

```
Implement padlib in Python. Read SPEC.md for the specification and tests.yaml for test cases.
```

## Language-Specific Notes

### Python

```python
# The implementation will typically be a single module
# Usage:
from padlib import left_pad, right_pad, center_pad, pad, zero_pad

left_pad("foo", 5)  # "  foo"
```

### JavaScript/TypeScript

```javascript
// Can be a module or standalone functions
import { leftPad, rightPad, centerPad, pad, zeroPad } from "./padlib";

leftPad("foo", 5); // "  foo"
```

### Rust

```rust
// Typically a module with public functions
use padlib::{left_pad, right_pad, center_pad, pad, zero_pad};

left_pad("foo", 5, None);  // "  foo"
```

## Verification

After generating your implementation, verify it passes all tests:

1. Parse the `tests.yaml` file
2. Run each test case against your implementation
3. Compare actual output with expected output
4. All tests must pass before using in production

Most AI assistants can generate a test runner along with the implementation.

## Why This Approach?

Traditional libraries have dependencies, version conflicts, and supply chain risks. The original `padlib` incident in 2016 broke thousands of projects when an 11-line package was unpublished from npm.

With spec-only libraries:

- **No dependencies** - The code is generated fresh for your project
- **No supply chain** - Nothing to unpublish or compromise
- **Language agnostic** - Same spec works for any language
- **Always compatible** - Generated for your specific environment
- **Inspectable** - You can read every line of the generated code

## Troubleshooting

**"The AI generated incorrect code"**

- Ensure you provided both SPEC.md and tests.yaml
- Ask the AI to run through test cases and fix any failures
- Try a different AI model (Claude Opus tends to work well)

**"Some tests are failing"**

- Check edge cases: empty strings, negative lengths, unicode
- Verify multi-character fill patterns are handled correctly
- Check that negative number handling preserves the sign

**"The code doesn't match my language's style"**

- Ask the AI to refactor using idiomatic patterns
- Specify coding conventions in your prompt
