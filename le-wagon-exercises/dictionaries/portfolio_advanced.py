# pylint: disable=missing-docstring

# TODO: start by defining a `portfolio` using a dict!

portfolio = {
    "AAPL": {
        "volume": 10
        "strike": 154.12
    },
    "GOOG": {
        "volume": 2,
        "strike": 812.56
    },
        "TSLA": {
        "volume": 12,
        "strike": 342.12
    },
        "FB": {
        "volume": 18,
        "strike": 209.0
    }
}

print(portfolio)['TSLA']['volume'])
print(portfolio['GOOG']['strike'])

market = {
    "AAPL": 198.84,
    "GOOG": 1217.93,
    "TSLA": 267.66,
    "FB": 179.06
}

#for name, number in portfolio.items():
#print(name, number)

#for name, number in portfolio.items():
#print(f'{name.capitalize()}) à une valeur de {number}-')

#pnl = 0

#pnl = pnl + portfolio ['AAPL']['volume']*(market['AAPL')-portfolio['AAPL']['strike'])
#print(pnl)

pnl = 0

result = 0
result2 = 0

print("-------")
print("portfolio (buying price)")

for key, value in portfolio.items():
    total = round(portfolio[key]['volume'] * portfolio[key]['strike'], 2)
    result2 = result2 + total
    print(str(key)+": "+str(total))

print("-------")
print("market (current price)")

for key, value in market.items():
    total2 = round(market[key] * portfolio[key]['volume'],2)
    result = result + total2
    print(str(key)+": "+str(total2))
    
print("-------")
print("P&L")
pnl = round(result - result2,2)
print(pnl)
