#!/usr/bin/python3
"""
    In a text file, there is a single character H. Your text editor can
    execute only two operations in this file: Copy All and Paste.
    Given a number n, write a method that calculates the fewest number of
    operations needed to result in exactly n H characters in the file.
"""


def processCount(num):
    """
    computes procsess and returns list of process until n H"""
    count = 1
    process_list = []
    value = num
    while value != 1:
        count += 1
        if value % count == 0:
            while (value % count == 0 and value != 1):
                value /= count
                process_list.append(count)

    return process_list


def minOperations(n):
    """
        return the sum of process until n H
    """
    if n < 2 or type(n) is not int:
        return 0
    val = processCount(n)
    return sum(val)
