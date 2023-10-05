#!/usr/bin/python3
"""You have n number of locked boxes in front of you. Each box is numbered
    sequentially from 0 to n - 1 and each box may contain keys to the other
    boxes.

    Write a method that determines if all the boxes can be opened.

    Prototype: def canUnlockAll(boxes)
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """Create dfs(box), a recursive helper function that
       performs Depth-First Search. It takes a box number as input, marks
       it as visited, and recursively visits all the boxes
       that can be opened from this box.
    """
    def dfs(box):
        """
        initialize an empty set visited to keep track of visited boxes.
        Then, call the DFS function starting from the
        first box (box number 0).
        """
        visited.add(box)
        for key in boxes[box]:
            if key not in visited:
                dfs(key)

    """After the DFS traversal, if the number of visited boxes equals the
        total number of boxes (n), it means all boxes can be opened,
        and the function returns True. Otherwise, it returns False.
    """
    n = len(boxes)
    visited = set()
    dfs(0)

    """This algorithm ensures that it explores all reachable boxes from the
      first box. If all boxes are visited, it means every box can be opened,
      and the function returns True. If there are unvisited boxes,
      it returns False.
    """
    return len(visited) == n
