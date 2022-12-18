from typing import List, NoReturn


class Solution:

    def __init__(self):
        self._result_list = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        remain_list = nums
        permu_list = []
        for i in range(len(remain_list)):
            self.search(remain_list, permu_list, i)
        return self._result_list

    def search(self, remain_list: List[int], permu_list: List[int], action: int) -> NoReturn:
        remain_list_new = remain_list.copy()
        permu_list_new = permu_list.copy()
        number = remain_list_new.pop(action)
        permu_list_new.append(number)
        if not remain_list_new:
            self._result_list.append(permu_list_new)
            return
        for i, _ in enumerate(remain_list_new):
            self.search(remain_list_new, permu_list_new, i)


if __name__ == "__main__":
    num_in = [1, 2, 3]
    solu = Solution()
    result = solu.permute(num_in)
    print(result)
