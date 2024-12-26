for _ in range(int(input())):
    t, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    clients = list(zip(a, b))
    n = len(clients)
    clients.sort(key=lambda x: x[1])
    prices = sorted(set([x for a, b in clients for x in (a, b)]))
    num_prices = len(prices)

    max_profit_value = 0
    negative_clients_indices = []
    negative_count = 0
    j = 0
    for i in range(num_prices):
        price = prices[i]
        while j < n and clients[j][0] < price <= clients[j][1]:
            negative_clients_indices.append(j)
            j += 1
        l = 0
        while l < len(negative_clients_indices):
            if clients[negative_clients_indices[l]][1] < price:
                negative_clients_indices.pop(l)
            else:
                l += 1
        negative_count = len(negative_clients_indices)
        positive_count = 0
        for client in clients:
            if price <= client[0]:
                positive_count += 1
        if negative_count <= k:
            current_profit = price * (positive_count + negative_count)
            max_profit_value = max(max_profit_value, current_profit)
    print(max_profit_value)