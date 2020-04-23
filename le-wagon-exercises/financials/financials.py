# pylint: disable=missing-docstring

# TODO: 1st exercise: Define the `forward_price` function

# TODO: 2nd exercise: Define the `short_pnl` function

import match

def forward_price(spot, interest_rate, time):
    forward_price = spot * match.exp(interest_rate * time)
    return round(forward_price, 2)

def short_pnl(positions, mtm):
    net_income = 0
    for i in range(len(positions)):
        net_income += positions[i]-mtm[i]
    return net_income
