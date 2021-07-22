#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    checks keys and boxes
    """
    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    for x in range(1, len(boxes) - 1):
        checked_boxes = False
        for y in range(len(boxes)):
            checked_boxes = x in boxes[y] and x != y
            if checked_boxes:
                break
        if checked_boxes is False:
            return checked_boxes
    return True
