# pylint: disable=missing-docstring

aapl = [ 10, 154.12 ]
goog = [  2, 812.56 ]
tsla = [ 12, 342.12 ]
fb   = [ 18, 209.0  ]

portfolio = [ aapl, goog, tsla, fb ]

#fb_stocks_count = portfolio[3][O]

market = [ 198.84, 1217.93, 267.66, 179.06 ]

sum(market)

pnl = 0
for i in range(0,4):
        pnl += portfolio[i][0]*(market[i]-portfolio[i][1])

print(pnl)
