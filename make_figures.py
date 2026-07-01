"""results/ 시각화 재현 스크립트 — pandas + seaborn
실행: python make_figures.py
"""
import os
import glob
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

plt.rcParams["font.family"] = "Malgun Gothic"      # 한글 라벨 (Windows)
plt.rcParams["axes.unicode_minus"] = False
sns.set_theme(style="whitegrid", font="Malgun Gothic")

HERE = os.path.dirname(__file__)
R = os.path.join(HERE, "results"); os.makedirs(R, exist_ok=True)
GREEN = "#76B900"

# tips 통계 시각화
tips_path = glob.glob(os.path.join(HERE, "src", "02_data_analysis", "**", "tips.csv"), recursive=True)[0]
t = pd.read_csv(tips_path)
fig, axs = plt.subplots(1, 2, figsize=(11, 4.4))
sns.boxplot(data=t, x="day", y="tip", hue="time", ax=axs[0]); axs[0].set_title("요일·시간대별 팁 분포 (tips)")
sns.scatterplot(data=t, x="total_bill", y="tip", hue="time", size="size", ax=axs[1]); axs[1].set_title("결제금액 vs 팁")
fig.tight_layout(); fig.savefig(f"{R}/seaborn_tips.png", dpi=120); plt.close(fig)

# youtube 카테고리 분포
yt_path = glob.glob(os.path.join(HERE, "src", "02_data_analysis", "**", "youtube_rank_1000.xlsx"), recursive=True)[0]
y = pd.read_excel(yt_path)
top = y["Category"].value_counts().head(10)
fig, ax = plt.subplots(figsize=(7, 4.6))
sns.barplot(x=top.values, y=top.index, color=GREEN, ax=ax)
ax.set(xlabel="채널 수", ylabel="", title="유튜브 상위 1000 채널 — 카테고리별 분포")
fig.tight_layout(); fig.savefig(f"{R}/youtube_categories.png", dpi=120); plt.close(fig)
print("saved figures to", R)
