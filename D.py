################################
# <方針>
# プロジェクトの最大数を二分探索を用いて算出する。
# 二分探索のleft値をプロジェクトの最大数と考える。
# 参考 : https://zenn.dev/fjnkt98/articles/5bef9f4cf2af60
################################

# 標準入力を受け付ける。
N, K = map(int, input().split())

A = list(map(int, input().split()))

# left: 実現可能なプロジェクトの最大数
left = 0
right = 100000000000000000000

# left >= rightになった場合に、プロジェクト数の探索を終了する。
while right - left > 1:
    # mid : 仮のプロジェクトの最大数
    mid = left + (right - left) // 2
    # count : プロジェクトの最大数がmidの時の、各部署から排出すべき人数の合計。
    count = 0

    for i in range(N):
        # プロジェクトの最大数をmidとした場合に、各部署から排出すべき人数を算出する。
        # mid(プロジェクトの最大数) > 各部署の人数(A[i])の場合、各部署の人数(A[i])分しか、排出できないため、A[i]とする。
        # 反対にmid(プロジェクトの最大数) <= 各部署の人数(A[i])の場合、mid(プロジェクト数)分、各部署の人数(A[i])を排出する。
        # 参考 : https://www.youtube.com/watch?v=9o4Lbxd3up4
        count += min(A[i], mid)

    # midのプロジェクト数を満たすためには、mid x K人必要である。
    # プロジェクトの最大数がmidの時の、各部署から排出すべき人数の合計 >= mid x kの時、プロジェクト数(mid)を実現できる。
    if count >= mid * K:
        left = mid
    # プロジェクトの最大数がmidの時の、各部署から排出すべき人数の合計 < mid x kの時、プロジェクト数(mid)を実現できない。
    else:
        right = mid

print(left)
