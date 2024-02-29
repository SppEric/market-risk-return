import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_json("stock_data.json").transpose()
df["annualized_mean_return"] = df["annualized_mean_return"].astype(np.float64)
df["beta"] = df["beta"].astype(np.float64)
print(df.head(n=10))

# Annualized mean return for First Republic Bank is an extreme outlier since its value is so high, 
# makes graphing data really annoying D: 
df = df.drop("FRC", axis=0)


# sns.scatterplot(df, x="annualized_mean_return", y="beta")
# sns.displot(df, x="annualized_mean_return", kde=True)
# sns.displot(df, x="beta", kde=True)

# Visualization 1
g = sns.jointplot(df, x="annualized_mean_return", y="beta")
g.plot_joint(sns.regplot, scatter_kws={'s':2})
g.plot_marginals(sns.histplot)
g.fig.suptitle("Relationship and Distributions of Stock Mean Return and Beta")


#sns.regplot(df, x="annualized_mean_return", y="beta")

# Visualization 2
g2 = sns.PairGrid(df)
g2.map_lower(sns.scatterplot, s=10)
g2.map_upper(sns.kdeplot, fill=True)
g2.map_diag(sns.histplot, kde=True)
g2.fig.suptitle("Distributions and Relationships of All Variables")

plt.show()