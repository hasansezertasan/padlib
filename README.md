# padlib

A string padding library, with no code.

## What is this?

`padlib` is a string padding utility library that contains **no executable code**. Instead, it contains:

- **SPEC.md** - A detailed specification of how the library should behave
- **tests.yaml** - Language-agnostic test cases as input/output pairs
- **INSTALL.md** - Instructions for generating an implementation

Pass these files to your AI coding assistant of choice, tell it what language you need, and it will generate a working implementation that passes all tests.

## Functions

| Function     | Description                                         |
| ------------ | --------------------------------------------------- |
| `left_pad`   | Pads a string on the left to reach a target length  |
| `right_pad`  | Pads a string on the right to reach a target length |
| `center_pad` | Centers a string within a target length             |
| `pad`        | General-purpose padding with position control       |
| `zero_pad`   | Pads numbers with leading zeros                     |

## Supported Languages

This library has been tested with:

- Python
- JavaScript/TypeScript
- Ruby
- Rust
- Go
- Elixir
- PHP
- Bash

It probably works in other languages too. Those are just the ones we've tried.

## Why?

In 2016, an 11-line npm package called `left-pad` was unpublished, breaking thousands of projects including Node.js and Babel. This incident highlighted how fragile dependency chains had become.

With modern AI coding agents, we can take a different approach: instead of depending on someone else's implementation, we define the **behavior** we need and generate the implementation ourselves.

No supply chain. No dependency hell. No breaking changes. Just a spec and tests.

## Installation

See [INSTALL.md](INSTALL.md).

## Specification

See [SPEC.md](SPEC.md) for the complete behavioral specification.

## Tests

See [tests.yaml](tests.yaml) for all test cases.

## License

MIT License. See [LICENSE](LICENSE).

## Inspired By

- [A Software Library with No Code](https://www.dbreunig.com/2026/01/08/a-software-library-with-no-code.html) and [whenwords](https://github.com/dbreunig/whenwords) by Drew Breunig
- [Porting MiniJinja to Go With an Agent](https://lucumr.pocoo.org/2026/1/14/minijinja-go-port/) by Armin Ronacher — my take: language-agnostic testing tools are more valuable than ever
- [I don't really use libraries anymore](https://www.youtube.com/watch?v=u9P3CKwtRnM) by Theo — my take: AI can easily write and maintain small scripts, the things Theo said in this video really stuck with me!
- The original [left-pad incident](https://www.theregister.com/2016/03/23/npm_left_pad_chaos/)
