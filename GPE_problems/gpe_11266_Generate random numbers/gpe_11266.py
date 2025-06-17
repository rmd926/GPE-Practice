def count_diff_middle(target: int):
    """
    以中間平方法從初始種子 target 產生序列，
    回傳出現過的不同值個數（含 target 本身）。
    """
    seen = set()
    current = target
    while current not in seen:
        seen.add(current)

        # 平方並補零至 8 位
        mid_sq = str(current ** 2).zfill(8)
        # 取中間 4 位作為下一個值
        current = int(mid_sq[2:6])
    
    return len(seen)


def main():
    while True:
        line = input().strip()
        if line == '0':
            break
        
        # 讀入可能有前導零的 4 位數
        target = int(line)
        print(count_diff_middle(target))


if __name__ == "__main__":
    main()
