# 標準入力を受け付ける。
N = int(input())

S = list(map(int, input().split()))

# 実際の建築面積になりうる値を演算する関数。
def calc_area(a, b):
    return 4 * a * b + 3 * a + 3 * b

# 予想した面積が確実に誤りであるとわかる人数
error_cnt = 0
for i in range(N):
    # 各人が予想した建築面積が正しいかどうか、検査する。
    # a, bは正の整数。正の整数の初期化を行う。
    a = 1
    b = 1
    # 各人が予想した建築面積が正しいか判定するためのフラグを用意する。
    is_correct = False
    # 各人が予想した建築面積。
    expected = S[i]
    # a, bの値へ正の整数を与えて、各人が予想した建築面積が正しいかどうか検査する。
    # 各人が予想する建築面積より「4ab+3a+3b」の値が大きくなった場合、ループを終了する。
    while True:
        while True:
            actual = calc_area(a, b)

            # 各人が予想した建築面積が正しければループを終了する。
            if actual == expected:
                is_correct = True
                break

            # 各人が予想する建築面積より「4ab+3a+3b」の値が大きくなった場合、ループを終了する。
            if actual > expected:
                break

            b += 1

        # 各人が予想した建築面積が正しければループを終了する。
        if is_correct == True:
            break

        a += 1
        b = 1

        actual = calc_area(a, b)

        # 各人が予想する建築面積より「4ab+3a+3b」の値が大きくなった場合、ループを終了する。
        if actual > expected:
            break

    if is_correct == False:
        error_cnt += 1

print(error_cnt)
