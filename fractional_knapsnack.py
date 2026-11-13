def knapsack(w, p, m):
    ratio = [p[i]/w[i] for i in range(len(w))]
    items = sorted(zip(ratio, w, p), reverse=True)

    profit = 0
    for r, wt, val in items:
        if m >= wt:
            profit += val
            m -= wt
        else:
            profit += r*m
            break

    print("Maximum Profit:", profit)

n = int(input("Enter number of items: "))
w, p = [], []

for i in range(n):
    w.append(int(input("Enter weight: ")))
    p.append(int(input("Enter profit: ")))

m = int(input("Enter capacity: "))
knapsack(w, p, m)
