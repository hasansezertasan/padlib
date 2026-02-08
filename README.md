# padlib

A string padding library with no code.

## What is this?

`padlib` is a **ghost library**: it ships a specification and test cases instead of executable code. You give these files to an AI coding assistant, tell it what language you need, and it generates a working implementation locally.

The repository contains three files:

- **SPEC.md** -- Complete behavioral specification
- **tests.yaml** -- 111 language-agnostic test cases as input/output pairs
- **INSTALL.md** -- Instructions for generating an implementation

## Functions

| Function     | Description                                         |
| ------------ | --------------------------------------------------- |
| `left_pad`   | Pads a string on the left to reach a target length  |
| `right_pad`  | Pads a string on the right to reach a target length |
| `center_pad` | Centers a string within a target length             |
| `pad`        | General-purpose padding with position control       |
| `zero_pad`   | Pads numbers with leading zeros                     |

## Language Support

Any language an AI coding assistant can target. Verified with Python.

## Why?

In 2016, an 11-line npm package called `left-pad` was unpublished, breaking thousands of projects including Node.js and Babel. The incident showed how fragile dependency chains had become.

Ghost libraries take a different approach: instead of depending on someone else's implementation, you define the **behavior** you need and generate the implementation locally. No supply chain. No dependency conflicts. No breaking changes. Just a spec and tests.

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
- [Porting MiniJinja to Go With an Agent](https://lucumr.pocoo.org/2026/1/14/minijinja-go-port/) by Armin Ronacher -- language-agnostic testing tools are more valuable than ever
- [I don't really use libraries anymore](https://www.youtube.com/watch?v=u9P3CKwtRnM) by Theo -- AI can write and maintain small utilities, removing the need to depend on third-party packages
- The original [left-pad incident](https://www.theregister.com/2016/03/23/npm_left_pad_chaos/)
