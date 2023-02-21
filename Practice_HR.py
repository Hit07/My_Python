# def Plusminus(arr):
#     positive,negative,zero = 0,0,0
#     for char in arr:
#         if char>0:
#            positive+=1
#         elif char<0:
#            char+=char
#            negative+=1
#         else:
#            zero = 1
#     # Write your code here
#     print(f'positive:{"%0.6f" %(positive/n)}')
#     print(f'negative:{"%0.6f"%(negative/n)}')
#     print(f"zero:{'%0.6f'%(zero/n)}")
#
# n = int(input("No of elements:"))
# arr = list(map(int,input("Enter the arr elements:").split()))
# Plusminus(arr)
# # x, y = map(int, input().split())
# # print(x,y)


# import math
# import os
# import random
# import re
# import sys
#
# def miniMaxSum(arr):
#     max = sum(arr) - minimum
#     min = sum(arr) - maximum
#     print(f"{min} {max}")
#
#
# arr = list(map(int, input().rstrip().split()))
# maximum = max(arr)
# minimum = min(arr)
# miniMaxSum(arr)