import seaborn as sns
import matplotlib.pyplot as plt

penguins_data = sns.load_dataset("penguins")
# x must be a string of your data
print("--data.shape--")
print(penguins_data.shape)
print("--data.describe--")
print(penguins_data.describe())

# Simple Histogram
# You need to import pyplot to show the plot of the seaborn.
sns.histplot(data=penguins_data, x="flipper_length_mm")
plt.show()
