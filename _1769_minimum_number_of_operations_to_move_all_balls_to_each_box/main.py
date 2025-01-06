class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = [int(box) for box in list(boxes)]
        LENGTH = len(boxes)

        # First we count how many boxes we should carry
        prefix_boxes = [0 for _ in range(LENGTH)] # From left to right
        suffix_boxes = [0 for _ in range(LENGTH)] # From right to left

        prefix_boxes[0] = boxes[0]
        suffix_boxes[LENGTH - 1] = boxes[LENGTH - 1]

        for i in range(1, LENGTH):
            prefix_boxes[i] = prefix_boxes[i - 1] + boxes[i]
            suffix_boxes[LENGTH - i - 1] = suffix_boxes[LENGTH - i] + boxes[LENGTH - i - 1]

        # Second we calculate how many movements we must do
        prefix_mvt = [0 for _ in range(LENGTH)] # From left to right
        suffix_mvt = [0 for _ in range(LENGTH)] # From right to left
        
        for i in range(1, LENGTH):
            prefix_mvt[i] = prefix_mvt[i - 1] + prefix_boxes[i - 1]
            suffix_mvt[LENGTH - i - 1] = suffix_mvt[LENGTH - i] + suffix_boxes[LENGTH - i]

        # Lastly we sum the movement from the left side and right side
        for i in range(LENGTH):
            boxes[i] = prefix_mvt[i] + suffix_mvt[i]

        return boxes