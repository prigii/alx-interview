#!/usr/bin/python3
# a method that determines if all the boxes can be opened


def canUnlockAll(boxes):
    # Set to keep track of unlocked boxes
    unlocked_boxes = set([0])

    # Queue to keep track of boxes to be checked
    box_queue = [0]

    while box_queue:
        current_box = box_queue.pop(0)

        # Check all the keys in the current box
        for key in boxes[current_box]:
            # If the key opens a box and that box is not already unlocked
            if key < len(boxes) and key not in unlocked_boxes:
                unlocked_boxes.add(key)
                box_queue.append(key)

    # If all boxes are unlocked, return True
    return len(unlocked_boxes) == len(boxes)
