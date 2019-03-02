#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 1/17/2019

import copy

arr_sample = [2, 89, 34, 55, 34, 68, 49, 87, 62, 80]

def selectSort(arr):
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


def bubbleSort(arr):
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


def insertSort(arr):
    """插入排序"""
    newArr = copy.deepcopy(arr)
    for i in range(1, len(newArr)):
        insertIndex = -1
        for j in range(0, i):
            if newArr[i] < newArr[j] :
                insertIndex = j
                break
        if insertIndex > -1:
            # 插入元素
            tmp = newArr[i]
            for k in range(i, insertIndex, -1):
                # 从后往前遍历，后移一位元素
                newArr[k] = newArr[k - 1]
            newArr[insertIndex] = tmp
        # print("insertIndex: %d, i:%d list%s:" % (insertIndex, i, newArr))
    return newArr


# 2, 89, 34, 55, 34, 68, 49, 87, 62, 80
def quickSort(arr, left, right):
    """快速排序"""
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
    quickSort(arr, left, i-1)
    quickSort(arr, i+1, right)
    return arr



print(arr_sample)
# arr_result = bubbleSort(arr_sample)
# arr_result = selectSort(arr_sample)
# arr_result = insertSort(arr_sample)
arr_result = quickSort(arr_sample, 0, len(arr_sample)-1)
print(arr_result)