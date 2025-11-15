import pandas as pd
from functools import reduce

data = {
    'num': [1,2,3,4,5],
    'let': ['a','b','c','d','e']
}

df = pd.DataFrame(data)

# square of numbers
sq = list(map(lambda x: x**2, df['num']))
print(sq)

# even numbers
ev = list(filter(lambda x: x % 2 == 0, df['num']))
print(ev)