for b in range(1, 11):
    for k in range(1, 21):
        for t in range(1, 201):
            if (b * 10) + (k * 5) + (t * 0.5) == 100 and b + k + t == 100:
                print(b, k, t)
