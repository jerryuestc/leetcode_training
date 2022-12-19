from typing import List


class Solution:

    def __init__(self):
        self.total_set = None
        self.sub_set_list = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.total_set = nums
        self.sub_set_list.append([])
        for action in range(len(nums)):
            subset = []
            self.search_subset(subset, action)
        return self.sub_set_list

    def search_subset(self, subset, action):
        new_subset = subset.copy()
        new_subset.append(self.total_set[action])
        self.sub_set_list.append(new_subset)
        if action == len(self.total_set) - 1:
            return
        for new_action in range(action + 1, len(self.total_set)):
            self.search_subset(new_subset, new_action)


if __name__ == "__main__":
    solu = Solution()
    print(solu.subsets([]))
