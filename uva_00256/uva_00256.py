import sys

def main():
    # 讀取每一行輸入，直到檔案結束
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue  # 跳過空行

        n = int(line)               # 位數 (2, 4, 6, 8)
        half = 10 ** (n // 2)       # 一半位數的基底，例如 n=4 時 half=100
        upper_bound = 10 ** n       # 最大 n 位數的上界 (不含)

        # 枚舉所有可能的 s = high + low，範圍 0..2*(half-1)
        for i in range(2 * (half - 1) + 1):
            square_num = i**2       # 計算平方，候選的 quirksome 數字
            if square_num >= upper_bound:
                continue            # 超過 n 位數範圍就跳過

            # 將平方結果拆回high、low兩段
            high = square_num // half
            low  = square_num % half

            # 若 high + low 恰等於 i，則 square_num 就是 quirksome square
            if (high + low) == i:
                # 輸出時補足前導零到 n 位
                print(f"{square_num:0{n}d}")

if __name__ == '__main__':
    main()
