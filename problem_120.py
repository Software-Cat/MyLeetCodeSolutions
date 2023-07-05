from typing import Dict, List, Tuple


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp: Dict[Tuple[int, int], int] = {}

        for depth, layerContent in enumerate(triangle):
            for i, currentItem in enumerate(layerContent):
                if depth == 0:
                    dp[(depth, i)] = currentItem
                elif i == 0:
                    dp[(depth, i)] = dp[(depth-1, i)] + currentItem
                elif i == len(layerContent) - 1:
                    dp[(depth, i)] = dp[(depth-1, i-1)] + currentItem
                else:
                    dp[(depth, i)] = min(
                        dp[(depth-1, i-1)],
                        dp[(depth-1, i)]
                    ) + currentItem
            

        return min(i for k, i in dp.items() if k[0] == len(triangle) - 1)
