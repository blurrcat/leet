#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory
subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\t
subsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1
contains a file file1.ext and an empty second-level sub-directory subsubdir1.
subdir2 contains a second-level sub-directory subsubdir2 containing a file
file2.ext.

We are interested in finding the longest (number of characters) absolute path
to a file within our file system. For example, in the second example above, the
longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is
32 (not including the double quotes).

Given a string representing the file system in the above format, return the
length of the longest absolute path to file in the abstracted file system. If
there is no file in the system, return 0.

Note:
The name of a file contains at least a . and an extension.
The name of a directory or sub-directory will not contain a ..
Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path, if there is
another path aaaaaaaaaaaaaaaaaaaaa/sth.png.
"""
import pytest
from collections import namedtuple


class Stack:
    def __init__(self):
        self._s = []

    def push(self, item):
        # print('stack: push {}'.format(item))
        self._s.append(item)

    def pop(self):
        item = self._s.pop()
        # print('stack: pop {}'.format(item))
        return item

    @property
    def top(self):
        return self._s[-1]


class Word:
    def __init__(self, level=0, letters=None):
        self.level = level
        self.letters = letters or []

    @property
    def length(self):
        return len(self.letters)

    @property
    def is_filename(self):
        return '.' in self.letters

    def __str__(self):
        return '[{}]{}'.format(self.level, ''.join(self.letters))


class Lexer:
    """
    for parsing words
    """
    def __init__(self):
        self.reset()

    def parse(self, stream):
        for token in stream:
            self.read(token)
            if self.terminated:
                # print('lex: "{}"'.format(self.word))
                yield self.word
                self.reset()
        # yield final word in memory
        # print('lex: "{}"'.format(self.word))
        yield self.word

    def read(self, token):
        if token == '\t':
            self.word.level += 1
        elif token == '\n':
            self.terminated = True
        else:
            self.word.letters.append(token)

    def reset(self):
        self.terminated = False
        self.word = Word()


Path = namedtuple('Path', ['level', 'length', 'is_filename'])


class Parser:
    """
    constructs syntax tree
    """
    def __init__(self):
        self.stack = Stack()
        self.stack.push(Path(-1, 0, True))
        self.lexer = Lexer()
        self.longest = 0

    def parse(self, stream):
        for word in self.lexer.parse(stream):
            # print('parser: read {}'.format(word))
            if word.level <= self.stack.top.level:
                # top path is a leaf
                self.remember_length(self.stack.top)
            # if word is not top's child, find its parent
            while word.level <= self.stack.top.level:
                self.stack.pop()
            # get length of the new path: top + word
            length = self.stack.top.length + word.length
            if not word.is_filename:
                length += 1  # for "/" at the end of the path
            self.stack.push(Path(word.level, length, word.is_filename))
        # what's left in the stack is a leaf
        self.remember_length(self.stack.top)

    def remember_length(self, path):
        # only files count; ignore directories
        if path.is_filename and path.length > self.longest:
            self.longest = path.length
        # print('longest is {}'.format(self.longest))


class Solution(object):

    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        parser = Parser()
        parser.parse(input)
        return parser.longest


TESTCASES = [
    ['''dir
\tsubdir1
\t\tfile1.ext
\t\tsubsubdir1
\tsubdir2
\t\tsubsubdir2
\t\t\tfile2.ext''', 32],
    ['''a
\ta
\ta.txt
\tbbbb.txt''', 10],
    ['a.b', 3],
    ['a', 0],
    ['', 0],
    ['''dir
\tl1
\t\tl2
\t\t\tl3.1
\tr1''', 14],
]


@pytest.mark.parametrize('s,longest', TESTCASES)
def test_388(s, longest):
    assert Solution().lengthLongestPath(s) == longest
