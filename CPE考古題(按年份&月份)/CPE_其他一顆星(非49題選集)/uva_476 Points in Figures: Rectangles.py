rectangle = []

while True:
    line = list(map(str, input().split()))

    if line[0] == "*":
        break
    # (x1, y1)左上 (x2, y2)右下
    x1, y1, x2, y2 = float(line[1]), float(line[2]), float(line[3]), float(line[4])
    rectangle.append([x1, y1, x2, y2])

point_num = 1
while True:
    x, y = map(float, input().split())
    if x == 9999.9 and y == 9999.9:
        break

    status = False
    for i in range(len(rectangle)):
        x1, y1, x2, y2 = rectangle[i]

        if x1 < x < x2 and y2 < y < y1:
            print(f"Point {point_num} is contained in figure {i+1}")
            status = True
    
    if not status:
        print(f"Point {point_num} is not contained in any figure")
    
    point_num += 1
