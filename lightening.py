import pandas as pd
import matplotlib.pyplot as plt

v=pd.read_csv("dataset.csv")
v['month'] = pd.to_datetime(v['date']).dt.month
sum=v.groupby('month')['number_of_strikes'].sum()

plt.figure(figsize=(10, 6))
sum.plot(kind='bar', color='blue', edgecolor='black')
plt.title('Monthly Lightning Strikes in 2018', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Total Strikes', fontsize=14)
plt.xticks(ticks=range(12), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

average_strikes=sum.mean()
print(f'Average lightning strikes per month: {average_strikes:.2f}')
