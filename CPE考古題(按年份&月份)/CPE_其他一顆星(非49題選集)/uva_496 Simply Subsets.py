while True:
    try:
        A = set(map(int, input().split()))
        B = set(map(int, input().split()))
    except:
        break

    if A == B:
        print("A equals B")
    
    elif A & B == A:
        print("A is a proper subset of B")
    
    elif A & B == B:
        print("B is a proper subset of A")
    
    elif A & B == set():
        print("A and B are disjoint")

    else:
        print("I'm confused!")
