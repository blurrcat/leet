#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
819. Most Common Word
Easy

Given a paragraph and a list of banned words, return the most frequent word
that is not in the list of banned words.  It is guaranteed there is at least
one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of
punctuation.  Words in the paragraph are not case sensitive.  The answer is in
lowercase.



Example:

Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent
non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is
banned.



Note:

    1 <= paragraph.length <= 1000.
    0 <= banned.length <= 100.
    1 <= banned[i].length <= 10.
    The answer is unique, and written in lowercase (even if its occurrences in
    paragraph may have uppercase symbols, and even if it is a proper noun.)
    paragraph only consists of letters, spaces, or the punctuation symbols
    !?',;.
    There are no hyphens or hyphenated words.
    Words only consist of letters, never apostrophes or other punctuation
    symbols.

Accepted
75,567
Submissions
177,282
"""
from typing import List
import pytest

from collections import Counter
import string

LETTERS = set(string.ascii_lowercase)


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        freq = Counter()

        word_parts = []
        for c in paragraph:
            char_lower = c.lower()
            # parse words
            if char_lower in LETTERS:
                word_parts.append(char_lower)
            else:
                # would have made the following a function in real life
                # but for the sake of speed, copying the code
                if word_parts:
                    word = ''.join(word_parts)
                    if word not in banned:
                        freq[word] += 1
                    word_parts = []

        # parts left after scanning the paragraph
        if word_parts:
            word = ''.join(word_parts)
            if word not in banned:
                freq[word] += 1

        return max(freq.items(), key=lambda item: item[1])[0]


@pytest.mark.parametrize(
    'paragraph,banned,expected', [[
        "Bob hit a ball, the hit BALL flew far after it was hit.", ['hit'],
        'ball'
    ], ["(ada) ada asdf", [], 'ada'], ['a, a, a, a, b,b,b,c, c', ['a'], 'b']]
)
def test_most_common_words(paragraph, banned, expected):
    assert Solution().mostCommonWord(paragraph, banned) == expected
