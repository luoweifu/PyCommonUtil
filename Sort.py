#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 1/17/2019

import copy

arr_sample = [2, 89, 34, 55, 34, 68, 49, 87, 62, 80]

def select_sort(arr):
    """选择排序"""
    newArr = copy.deepcopy(arr)
    for i in range(0, len(newArr)):
        minIndex = i
        for j in range(i, len(newArr)):
            if(newArr[j] < newArr[minIndex]):
                minIndex = j
        tmp = newArr[minIndex]
        newArr[minIndex] = newArr[i]
        newArr[i] = tmp
        # print(newArr)
    return newArr


def bubble_sort(arr):
    """冒泡排序"""
    newArr = copy.deepcopy(arr)
    for i in range(0, len(newArr)):
        for j in range(i, len(newArr) - 1):
            if (newArr[j] > newArr[j + 1]):
                tmp = newArr[j]
                newArr[j] = newArr[j + 1]
                newArr[j + 1] = tmp
        # print("(i:%d, j:%d) list:%s" % (i, j, newArr))
    return newArr


def insert_sort(arr):
    """直接插入排序"""
    newArr = copy.deepcopy(arr)
    for i in range(1, len(newArr)):
        # 插入元素
        tmp = newArr[i]  # 要插入的元素
        for k in range(i-1, -1, -1):
            # 从后往前遍历，依次后移一位元素，直到找着插入的位置时，插入该元素
            if (tmp < newArr[k]):
                newArr[k+1] = newArr[k]
            else:
                newArr[k+1] = tmp
                break
        # print("insertIndex: %d, i:%d list%s:" % (insertIndex, i, newArr))
    return newArr


# 2, 89, 34, 55, 34, 68, 49, 87, 62, 80
def quick_sort(arr):
    """快速排序"""
    return __quick_sort(arr, 0, len(arr) - 1)

def __quick_sort(arr, left, right):
    """递归的快排算法
    相关原理可参考：https://blog.csdn.net/adusts/article/details/80882649"""
    if(left > right):
        return arr

    # 设置基准数和局部变量
    base = arr[left]
    i = left
    j = right

    while(i != j):
        # 从右往左找一个比base小的数：d1
        while(i != j and arr[j] >= base):
            j -= 1
        # 从左往右找一个比base大的数：d2
        while(i != j and arr[i] <= base):
            i += 1
        # d1与d2互换位置
        if(i < j):
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

    # 此时 i == j，将此位置的值与base互换，将base归位置合适的位置
    arr[left] = arr[i]
    arr[i] = base
    # 递归再次排序
    __quick_sort(arr, left, i - 1)
    __quick_sort(arr, i + 1, right)
    return arr


def swap(arr, i, j):
    """调换数组中i, j两个元素的值"""
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def heap_sort(arr):
    """堆排序
    相关原理可参考：https://blog.csdn.net/u013384984/article/details/79496052"""
    # 从n个元素中查找最大的值放在索引n-1的位置，再从n-1个元素中查找最大的值放在索引n-2的位置，依此类推
    for i in range(len(arr) - 1, 0, -1):
        # i ：需要构建大顶堆树的最一个结点索引
        # 最后一个非叶子结点的索引,"//"表示取整的意思
        last = (i + 1) // 2 - 1
        # 构建大顶堆，并取堆顶(根结点)元素作为i+1个结点中的最大值
        __build_tree(arr, last, i)
        # 将最大值放在i位置，(0, 1, .. i-2, i-1)又变成了一课无序的树
        swap(arr, 0, i)
        # print("查找索引%d的最大值：%s" % (i, arr))
    return arr


def __build_tree(arr, last, end):
    """
    构建一棵(end+1)个元素的大顶堆树
    :param arr 要排序的数组
    :param last 最后一个非叶子结点的索引
    :param end 最一个元素的索引
    """
    # 从最后一个非叶子结点开始往上调整
    for i in range(last, -1, -1):
        __adjust_heap(arr, i, end)

def __adjust_heap(arr, root, end):
    """
    调整堆，构建大顶堆
    n个结点的完全二叉树按层序编号后(索引从0开始)，左孩子结点：left = 2*root + 1，右孩子结点：right = 2*root + 2
    :param arr 数组
    :param root 根结点索引
    :param end 最大的索引
    """
    # 取左右结点中值较大的结点
    max_idx = left = 2 * root + 1
    if(2 * root + 2 <= end):
        right = 2 * root + 2
        max_idx = left if arr[left] > arr[right] else right
    if(arr[max_idx] > arr[root]):
        swap(arr, root, max_idx)
        # max_idx 是否有孩子结点
        max_child_idx = 2 * max_idx + 1
        if(max_child_idx <= end):
            __adjust_heap(arr, max_idx, end)


def shell_sort(arr):
    """希尔排序
    相关原理可参考：https://blog.csdn.net/qq_39207948/article/details/80006224"""
    STEP = len(arr) // 2 # 初始步距
    while(STEP > 0):
        for i in range(STEP, len(arr)):
            __shell_insert_sort(arr, STEP, i)
        STEP //=2    # 步距每次缩小2倍，直到等于1
    return arr

def __shell_insert_sort(arr, step, i):
    """
    希尔插入排序
    :param arr 要排序的数组
    :param step 每次前进的步距(增量)
    :param i 第i次遍历
    """
    # 插入元素
    tmp = arr[i]  # 要插入的元素
    # 从后往前遍历，依次后移step位元素，直到找着插入的位置时，插入该元素
    k = i - step
    while (k >=0 and tmp < arr[k]):
        arr[k + step] = arr[k]
        k -= step
    arr[k + step] = tmp


# test
#print(list(range(5, 10, 1)))

print(arr_sample)
# arr_result = bubble_sort(arr_sample)
# arr_result = select_sort(arr_sample)
# arr_result = insert_sort(arr_sample)
# arr_result = quick_sort(arr_sample)
# arr_result = heap_sort(arr_sample)
arr_result = shell_sort(arr_sample)
print(arr_result)