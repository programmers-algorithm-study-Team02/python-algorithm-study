def solution(prices):
    answer = [0] * len(prices)
    
    stocks = []
    for i, price in enumerate(prices):
        while len(stocks) > 0 and stocks[-1][1] > price:
            stock = stocks.pop()
            answer[stock[0]] = i - stock[0]
        stocks.append((i, price))
    
    while len(stocks) > 0:
        stock = stocks.pop()
        answer[stock[0]] = len(prices) - 1 - stock[0]
    
    return answer
