def stock(daily_prices):
    min_price, maximum_profit = float('inf'), 0.0
    for price in daily_prices:
        profit = price - min_price
        min_price = min(price, min_price)
        maximum_profit = max(profit, maximum_profit)
    print(maximum_profit)
    return

def main():
    daily_prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    stock(daily_prices)
if __name__ == '__main__':
    main()