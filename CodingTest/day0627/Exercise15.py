# 문제
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
#
# 출력
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

t = int(input())
arr = list(map(int,input().split()))

print(min(arr),max(arr))

# cnt = int(input())
# numbers = list(map(int, input().split()))
# max1 = numbers[0]
# min1 = numbers[0]
#
# for i in numbers[1:]:
#     if i > max1:
#         max1 = i
#     elif i < min:
#         min1 = i
#
# print(min1,max1)


    