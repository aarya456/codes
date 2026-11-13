def knapsack(w, p, m):
    n = len(w)
    dp = [[0]*(m+1) for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(m+1):
            if w[i-1] <= j:
                dp[i][j] = max(p[i-1]+dp[i-1][j-w[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    print("Maximum Profit:", dp[n][m])

n = int(input("Enter number of items: "))
w, p = [], []

for i in range(n):
    w.append(int(input("Enter weight: ")))
    p.append(int(input("Enter profit: ")))

m = int(input("Enter capacity: "))
knapsack(w, p, m)
