#!/usr/bin/env python3
"""
Find unique anagram groups from a list of words.

Usage:
  python anagrams.py listen silent enlist
  echo "listen silent enlist inlets google" | python anagrams.py
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from typing import Iterable, List


def find_anagram_groups(words: Iterable[str]) -> List[List[str]]:
    groups: dict[str, set[str]] = defaultdict(set)
    for word in words:
        normalized = word.strip()
        if not normalized:
            continue
        key = "".join(sorted(normalized.lower()))
        groups[key].add(normalized)

    result: List[List[str]] = []
    for key in sorted(groups.keys()):
        group = sorted(groups[key], key=str.lower)
        if len(group) >= 2:
            result.append(group)
    return result


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Output unique anagram groups from a list of words."
    )
    parser.add_argument(
        "words",
        nargs="*",
        help="Words to analyze. If omitted, words are read from stdin.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    words = args.words

    if not words:
        words = sys.stdin.read().split()

    groups = find_anagram_groups(words)
    for group in groups:
        print(" ".join(group))

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
