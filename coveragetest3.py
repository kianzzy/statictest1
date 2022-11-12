import unittest
from binarySearch import binary_search
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

class TestBinarySearch(unittest.TestCase):
    def test_case1(self):
        arr = [104, 185, 219, 253, 313, 351, 412, 434, 518, 572, 626, 662, 674, 679, 736, 802, 825, 877, 923, 980]
        self.assertEqual(binary_search(arr,5), 219)# case1 测试数组里不存在的数字，若二分查询返回-1，若通过则说明测试数组中不存在该数字

    def test_case2(self):
        arr = [104, 185, 219, 253, 313, 351, 412, 434, 518, 572, 626, 662, 674, 679, 736, 802, 825, 877, 923, 980]
        self.assertEqual (binary_search (arr, 22572), 9)  # case2  测试数组里不存在的数字，测试二分查询是否返回-1
    def test_case3(self):
        arr = [104, 185, 219, 253, 313, 351, 412, 434, 518, 572, 626, 662, 674, 679, 736, 802, 825, 877, 923, 980]
        self.assertEqual (binary_search (arr, 104), 2)  # case3  测试数组里存在但输入错误位置，测试程序结果是否正确

    def test_case4(self):
        arr = [104, 185, 219, 253, 313, 351, 412, 434, 518, 572, 626, 662, 674, 679, 736, 802, 825, 877, 923, 980]
        self.assertEqual (binary_search1 (arr, 104), 0)  # case4  测试数组里存在且正确位置，测试程序结果是否正确

    def test_case5
test_case6 = [104, 185]

if __name__ == '__main__':
    unittest.main()