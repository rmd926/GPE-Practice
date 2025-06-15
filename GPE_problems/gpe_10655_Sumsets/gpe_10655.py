from collections import defaultdict

def solve_case(S):
    """
    給定已排序且互異的整數列表 S，
    找出最大的 d ∈ S，使得存在 a,b,c ∈ S 且互異，
    滿足 a + b + c = d。若無解回傳 None。
    """
    n = len(S)

    pairs_sum = defaultdict(list)
    for i in range(n):
        for j in range(i+1, n):
            s = S[i] + S[j]
            pairs_sum[s].append((i, j))

    # 從最大的 d 開始往下找
    for d_index in range(n-1, -1, -1):
        cand_d = S[d_index]

        # 對每個可能的 c 立刻檢查
        for c_index in range(n):
            if c_index == d_index:
                continue
            cand_c = S[c_index]
            target = cand_d - cand_c

            # 如果沒有任何兩數之和等於 target，就跳過
            if target not in pairs_sum:
                continue

            # 檢查 (i, j) 與 c_index, d_index 是否互異
            for i, j in pairs_sum[target]:
                if i != c_index and i != d_index and j != c_index and j != d_index:
                    return cand_d

    return None


def main():
    while True:
        line = input().strip()
        if not line:
            continue
        n = int(line)
        if n == 0:
            break

        # 讀入 S
        S = [int(input().strip()) for _ in range(n)]
        S.sort()

        ans = solve_case(S)
        if ans is None:
            print("no solution")
        else:
            print(ans)

if __name__ == "__main__":
    main()
