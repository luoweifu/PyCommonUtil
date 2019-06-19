#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 4/16/2019

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        Add Two Numbers
        https://leetcode.com/problems/add-two-numbers/
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        n1 = n2 = 0
        h = l = p = None
        tmp = 0 # 进位
        while(l1 is not None or l2 is not None):
            n1 = l1.val if l1 is not None else 0
            n2 = l2.val if l2 is not None else 0
            n = n1 + n2 + tmp
            d = n %10  # 个位
            tmp = n // 10 # 十位
            p = ListNode(d)
            if l is None:
                h = l = p
            else:
                l.next = p
                l = p
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            # 处理进位
            if tmp > 0:
                l.next = p = ListNode(tmp)
        return h


    def threeSum(self, nums):
        """
        3Sum
        https://leetcode.com/problems/3sum/
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = stack = []
        for n in nums:
            if len(stack) < 3:
                stack.append(n)
            elif stack[0] + stack[1] + stack[2] == 0:
                result = stack
                stack.pop()
                stack.pop()

    def lengthOfLongestSubstring(self, s):
        """
        Longest Substring Without Repeating Characters
        https://leetcode.com/problems/longest-substring-without-repeating-characters/
        :type s: str
        :rtype: int
        """
        i1 = i2 = 0
        maxL = 0
        while(i2 < len(s)):
            s1 = s[i1:i2]
            if s[i2] in s1:
                l = i2 - i1
                if maxL < l:
                    maxL = l
                i2 = i1 = i1 + 1
            else:
                i2 += 1
        l = i2 - i1
        maxL = l if maxL < l else maxL
        return maxL

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif p and q:
            if p.val != q.val:
                return False
            else:
                # if p.left is None and q.left is None:
                #     isSameLeftTree = True
                # elif p.left is not None and q.left is not None:
                #     isSameLeftTree = self.isSameTree(p.left, q.left)
                # else:
                #     isSameLeftTree = False
                # if p.right is None and q.right is None:
                #     isSameRightTree = True
                # elif p.right is not None and q.right is not None:
                #     isSameRightTree = self.isSameTree(p.right, q.right)
                # else:
                #     isSameRightTree = False
                # return isSameLeftTree and isSameRightTree
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        if root.left:
            result += self.inorderTraversal(root.left)
        result.append(root.val)
        if root.right:
            result += self.inorderTraversal(root.right)
        return result;


    def preTraversal(self, root):
        if not root:
            return []
        result = []
        result.append(root.val)
        if root.left:
            result += self.preTraversal(root.left)
        if root.right:
            result += self.preTraversal(root.right)
        return result


    def generateTrees(self, n):
        cache = {}

        def generateTrees(start, end):
            print("start: " + str(start) + " - end: " + str(end))
            if start > end:
                return [None]

            if str((start, end)) in cache:
                return cache[str((start, end))]

            all_trees = []
            for i in range(start, end + 1):
                left_trees = generateTrees(start, i - 1)
                right_trees = generateTrees(i + 1, end)

                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            cache[str((start, end))] = all_trees
            return all_trees

        return generateTrees(1, n) if n else []


        # def BSTNum(start, end):
        #     if start > end:
        #         return 0
        #     elif start == end:
        #         return 1
        #     else:
        #         for i in range(start, end + 1):
        #             leftTrees = BSTNum(start, i-1)
        #             rightTrees = BSTNum(i + 1, end)
        #             leftTrees + rightTrees + 1

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0:
            return 0
        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(0)
        max = nums[0]
        for i in range(1, len(nums)):
            dp[i] = dp[i-1] + nums[i] if dp[i-1] > 0 else nums[i]
            max = max if max > dp[i] else dp[i]
        return max

    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0:
            return [[], 0]

        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(0)

        start = end = 0
        max = nums[0]
        for i in range(1, len(nums)):
            if dp[i - 1] > 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
                start = i
            if max < dp[i]:
                max = dp[i]
                end = i
        return [nums[start : end+1], max]

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 :
            return 1
        if n == 2:
            return 2
        n1 = 1
        n2 = 2
        for i in range(3, n + 1):
            tmp = n1 + n2
            n1 = n2
            n2 = tmp
        return n2

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 0:
            return 0
        minPrice = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            if minPrice > prices[i]:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
        return maxProfit

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0 :
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        m1 = nums[0]
        m2 = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            tmp = max(m2, m1 + nums[i])
            m1 = m2
            m2 = tmp
        return m2

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) <= 0:
            return 0
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])

        dp = [cost[0], min(cost[0], cost[1])]
        for i in range(2, len(cost)-1):
            dp.append(min(dp[i-1] + cost[i], dp[i-2] + cost[i]))
        dp.append(min(dp[len(cost) - 2], dp[len(cost) - 3] + cost[len(cost)-1]))
        return dp[len(cost) - 1]

    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return not (N & 0x01) # is even number (N & 0x01 is a odd number)

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]

        dp = [0]
        for i in range(1, num + 1):
            dp.append(dp[i >> 1] + (i & 1))
        return dp

    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        Let dp(r, c) be the minimum total weight of a falling path starting at (r, c) and reaching the bottom row.
        Then, dp(r, c) = A[r][c] + min(dp(r+1, c-1), dp(r+1, c), dp(r+1, c+1)), and the answer is min dp(0,c).
        """
        rowNum = len(A)
        colNum = len(A[0])
        for r in range(rowNum - 2, -1, -1):
            for c in range(0, colNum):
                minWeight = A[r+1][c]
                if(c > 0):
                    minWeight = min(minWeight, A[r+1][c-1])
                if(c < colNum-1):
                    minWeight = min(minWeight, A[r + 1][c + 1])
                A[r][c] += minWeight
                # print(A[r][c], end="\t")
            # print()
        return min(A[0])


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.__sums =  [0]
        curSum = 0
        for n in nums:
            curSum += n
            self.__sums.append(curSum)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.__sums[j+1] - self.__sums[i] # sums[j+1] - sums[i+1 - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

def testAddTwoNums():
    l1 = p = ListNode(2)
    p.next = ListNode(4)
    p = p.next
    p.next = ListNode(3)

    l2 = p = ListNode(5)
    p.next = ListNode(6)
    p = p.next
    p.next = ListNode(4)
    l = Solution().addTwoNumbers(l1, l2)
    print(l.val)


def testLogetstSubStr():
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"
    o = Solution()
    print(o.lengthOfLongestSubstring(s1))
    print(o.lengthOfLongestSubstring(s2))
    print(o.lengthOfLongestSubstring(s3))
    # print(o.lengthOfLongestSubstring(""))
    print(o.lengthOfLongestSubstring("dvdf"))


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def testIsSameTree():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    # tree2.right = TreeNode(3)
    sObj = Solution()
    isSameTree = sObj.isSameTree(tree, tree2)
    print(isSameTree)

def testInnorderTravel():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    sObj = Solution()
    result = sObj.inorderTraversal(tree)
    print(result)


def testUniqueBST():
    obj = Solution()
    treeList = obj.generateTrees(3)
    for node in treeList:
        result = obj.preTraversal(node)
        print(result)
    # tree = TreeNode(1)
    # tree.right = TreeNode(2)
    # tree.right.right = TreeNode(3)
    # print(obj.preTraversal(tree))


class Node:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def getFirst(self):
        return self.__head

    def getSize(self):
        return self.__size

    def deleteFirt(self):
        val = 1
        if self.__head is not None:
            val = self.__head.val
            self.__head = self.__head.next
            self.__size -= 1
        return val

    def delete(self, node):
        if self.__head == node:
            self.__head = node.next
        elif self.__tail == node:
            self.__tail = node.pre
        else:
            node.pre.next = node.next
            node.next.pre = node.pre
        self.__size -= 1

    def pushBack(self, node):
        # node = Node(val)
        if self.__size == 0:
            self.__head = self.__tail = node
        else:
            self.__tail.next = node
            node.pre = self.__tail
            self.__tail = node
        self.__size += 1

    def printLink(self):
        pt = self.__head
        while pt is not None:
            print(pt.val)
            pt = pt.next


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.__data = {}
        self.__capacity = capacity
        self.__list = LinkedList()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.__data :
            node = self.__data.get(key, -1)
            self.__list.delete(node)
            self.__list.pushBack(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = Node(value)
        if self.__list.getSize() >= self.__capacity :
            val = self.__list.deleteFirt()
            del self.__data[val]
        self.__data[key] = node
        self.__list.pushBack(node)


def testLRU():
    # listObj = LinkedList()
    # listObj.pushBack(Node(1))
    # listObj.pushBack(Node(3))
    # listObj.pushBack(Node(5))
    # listObj.pushBack(Node(7))
    # listObj.delete(listObj.getFirst().next)
    # listObj.deleteFirt()
    # listObj.printLink()
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))
    lru.put(3, 3)
    print(lru.get(2))
    lru.put(4, 4)
    print(lru.get(1))
    print(lru.get(3))
    print(lru.get(4))


def test():
    l = [1,2,3,4,5]
    print(l)
    l2 = list(reversed(l))
    print(l2)
    for i in range(4, -1, -1):
        print(i)
    dp = [False for i in range(6)]
    print(dp)
    l2 = [i for i in range(4)]
    print(l2)


def testMaxSubArray():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    obj = Solution()
    result, sum = obj.maxSubArray2(nums)
    print(result)
    print(sum)

def testClimbStairs():
    obj = Solution()
    result = obj.climbStairs(3)
    print(result)

def testRob():
    obj = Solution()
    # nums = [1,2,3,1]
    nums = [2,7,9,3,1]
    result = obj.rob(nums)
    print(result)

def testMinCostClimbingStairs():
    obj = Solution()
    # cost = [10, 15, 20]
    # cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    # cost = [0,0,0,1]
    cost = [0,1,1,0]
    result = obj.minCostClimbingStairs(cost)
    print(result)

def testRangeSum():
    nums = [-2, 0, 3, -5, 2, -1]
    arr = NumArray(nums)
    print(arr.sumRange(0, 2))
    print(arr.sumRange(2, 5))
    print(arr.sumRange(0, 5))

def testDivisorGame():
    obj = Solution()
    print(obj.divisorGame(1))
    print(obj.divisorGame(2))
    print(obj.divisorGame(3))

def testCountBits():
    obj = Solution()
    print(obj.countBits(2))
    print(obj.countBits(5))


def testMinFallingPathSum():
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    obj = Solution()
    print(obj.minFallingPathSum(A))
    print(A)

# testAddTwoNums()
# testLogetstSubStr()
# print(len("Hello"))
# print('n' in "hello")
# testIsSameTree()
# testInnorderTravel()
# testUniqueBST()
# testLRU()
# testMaxSubArray()
# testClimbStairs()
# testRob()
# testMinCostClimbingStairs()
# testRangeSum()
# testDivisorGame()
# testCountBits()
testMinFallingPathSum()
# test()