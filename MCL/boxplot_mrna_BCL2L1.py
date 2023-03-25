import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_excel("BCL2L1.cna.STAD.mrna.xlsx")
df = df[df["group"]!= "loss"]
plt.subplots(figsize=(12, 10))
sns.boxplot(x="dataset", y="BCL2L1", hue="group",data=df)
sns.stripplot(x="dataset", y="BCL2L1", dodge=True, hue="group", size = 2, color = "black", legend = False, data=df)
plt.savefig("BCL2L1.cna.STAD.mrna.datasets.box.png")

sta = []
for i in df["dataset"].unique():
    df_ = df.loc[df["dataset"] == i]
    neutral = df_.loc[df_["group"] == "neutral"]["BCL2L1"].values
    gain = df_.loc[df_["group"] == "gain"]["BCL2L1"].values
    t, p = stats.ttest_ind(neutral, gain)
    sta.append({"dataset": i, "p": p})

pd.DataFrame(sta).to_excel("BCL2L1.cna.STAD.mrna.datasets.p.xlsx", index=False)

