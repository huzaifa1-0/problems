import pandas as pd

data = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

df = pd.DataFrame(data)

print(df)

left_diagonal = [df.iloc[i,i] for i in range(min(df.shape))]