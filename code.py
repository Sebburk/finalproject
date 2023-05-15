import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("A939RX0Q048SBEA.csv")
print(df.columns)
df.plot(x= "Date", y = ['A939RX0Q048SBEA'])
plt.show() 
