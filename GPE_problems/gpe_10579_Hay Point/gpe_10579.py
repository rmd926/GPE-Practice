def main():
    # 讀取字典大小 m 和 job description 數量 n
    m, n = map(int, input().split())
    # 建立 Hay Point 字典
    hay_points = {}
    for _ in range(m):
        word, value = input().split()
        hay_points[word] = int(value)

    # 處理每一份 job description
    for _ in range(n):
        total_salary = 0
        while True:
            line = input().strip()
            # 碰到單獨一個 "." 表示這份描述結束
            if line == ".":
                break
            # 拆字計分
            for token in line.split():
                total_salary += hay_points.get(token, 0)
        print(total_salary)

if __name__ == "__main__":
    main()
