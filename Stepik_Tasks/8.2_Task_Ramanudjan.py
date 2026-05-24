for a1 in range(1, 33):
    for b1 in range(1, 33):
        for a2 in range(1, 33):
            for b2 in range(1, 33):
                if a1**3 + b1**3 == a2**3 + b2**3 and (
                    a1 != a2 and b1 != b2 and a1 != b2 and a2 != b1 and a2 != b2
                ):
                    print(a1**3 + b1**3)
                    print(a1, b1, a2, b2)
