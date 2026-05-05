from ast import parse
import re
from turtle import end_fill
from typing import List
from unittest import result

class Solution:
    """
    Join the words with a key delimiter such as #
    - With the delimiter put the string length, so you
      know when the word starts and ends.

    Separate the string having a key delimiter such as #
    - Do a split with the key delimiter and then iterate the array
      and get the string length with the key delimiter.
    """

    def encode(self, strs: List[str]) -> str:
        parts = []
        for word in strs:
            parts.append(f"-{len(word)}-{word}")
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        parts = s.split("-")
        i = 1 # Skip first empty string
        result = []
        while i < len(parts):
            length = parts[i]
            word = parts[i + 1]
            result.append(word)
            i += 2
        return result