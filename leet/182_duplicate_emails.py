#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
182. Duplicate Emails My Submissions Question
Total Accepted: 16032 Total Submissions: 42286 Difficulty: Easy

Write a SQL query to find all duplicate emails in a table named Person.

    +----+---------+
    | Id | Email   |
    +----+---------+
    | 1  | a@b.com |
    | 2  | c@d.com |
    | 3  | a@b.com |
    +----+---------+

For example, your query should return the following for the above table:

    +---------+
    | Email   |
    +---------+
    | a@b.com |
    +---------+

Note: All emails are in lowercase.

Solution:

    SELECT DISTINCT p1.email
    FROM Person AS p1
    INNER JOIN Person AS p2 ON p1.email = p2.email
    WHERE p1.id != p2.id;


"""

