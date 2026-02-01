"""Test runner that validates padlib against tests.yaml."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from padlib import center_pad, left_pad, pad, right_pad, zero_pad

TESTS_PATH = Path(__file__).parent / "tests.yaml"
FUNC_MAP = {
    "left_pad": left_pad,
    "right_pad": right_pad,
    "center_pad": center_pad,
    "pad": pad,
    "zero_pad": zero_pad,
}


def _load_tests() -> dict:
    return yaml.safe_load(TESTS_PATH.read_text())


def _collect_cases():
    data = _load_tests()
    cases: list[tuple] = []

    # Standard function tests
    for func_name in ("left_pad", "right_pad", "center_pad", "pad", "zero_pad"):
        for case in data.get(func_name, []):
            test_id = f"{func_name} - {case['description']}"
            cases.append((func_name, case["input"], case["expected"], test_id))

    # Unicode tests
    for func_name, unicode_cases in data.get("unicode", {}).items():
        for case in unicode_cases:
            test_id = f"unicode/{func_name} - {case['description']}"
            cases.append((func_name, case["input"], case["expected"], test_id))

    return cases


def _collect_error_cases():
    data = _load_tests()
    cases: list[tuple] = []
    for func_name, error_cases in data.get("errors", {}).items():
        for case in error_cases:
            test_id = f"error/{func_name} - {case['description']}"
            cases.append((func_name, case["input"], test_id))
    return cases


CASES = _collect_cases()
ERROR_CASES = _collect_error_cases()


@pytest.mark.parametrize(
    "func_name,inputs,expected",
    [(c[0], c[1], c[2]) for c in CASES],
    ids=[c[3] for c in CASES],
)
def test_spec(func_name: str, inputs: list, expected: str) -> None:
    result = FUNC_MAP[func_name](*inputs)
    assert result == expected


@pytest.mark.parametrize(
    "func_name,inputs",
    [(c[0], c[1]) for c in ERROR_CASES],
    ids=[c[2] for c in ERROR_CASES],
)
def test_errors(func_name: str, inputs: list) -> None:
    with pytest.raises(Exception):
        FUNC_MAP[func_name](*inputs)
