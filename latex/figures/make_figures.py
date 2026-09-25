"""Regenerates every figure used in the LaTeX notes.
Run from anywhere:  python latex/figures/make_figures.py
Uses only files in data/ (no internet)."""
import numpy as np, pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt, seaborn as sns
import statsmodels.formula.api as smf
from pathlib import Path

D = Path(__file__).resolve().parents[2] / "data"
OUT = Path(__file__).resolve().parent
rng = np.random.default_rng(2024)
sns.set_theme(style="whitegrid", palette="viridis")


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / f"{name}.pdf")
    plt.close(fig)


# ---------- Week 1 ----------
aq = pd.read_csv(D / "airquality.csv")
fig, ax = plt.subplots(1, 2, figsize=(9, 3.2))
ax[0].hist(aq.Temp, bins=np.arange(55, 101, 5), edgecolor="k")
ax[0].set(title="Histogram of Temp", xlabel="Temp", ylabel="Frequency")
ax[1].scatter(aq.Ozone, aq.Temp, s=12)
ax[1].set(xlabel="Ozone", ylabel="Temp", title="Ozone vs Temp")
save(fig, "L01_airquality")

mpg = pd.read_csv(D / "mpg.csv")
fig, ax = plt.subplots(figsize=(6, 3.8))
sns.scatterplot(data=mpg, x="displ", y="hwy", hue="class", palette="viridis", ax=ax)
ax.legend(fontsize=7, title="class")
save(fig, "L02_mpg_class")
g = sns.relplot(data=mpg, x="displ", y="hwy", col="class", col_wrap=4, height=1.8, s=12)
g.savefig(OUT / "L02_mpg_facets.pdf")
plt.close("all")

fig, ax = plt.subplots(1, 2, figsize=(9, 3.4))
sns.regplot(data=mpg, x="displ", y="hwy", lowess=True, scatter_kws=dict(s=10), ax=ax[0])
ax[0].set_title("points + smooth")
mpg["class"].value_counts().sort_index().plot.bar(ax=ax[1])
ax[1].set(title="count by class", ylabel="count")
save(fig, "L03_geoms")

# ---------- Week 2 ----------
h = pd.read_csv(D / "Heights.csv")
fig, ax = plt.subplots(figsize=(4.6, 4.2))
ax.scatter(h.mheight + rng.uniform(-.5, .5, len(h)), h.dheight + rng.uniform(-.5, .5, len(h)), s=3, alpha=.5)
ax.set(xlabel="Mheight (in)", ylabel="Dheight (in)", title="Heights data (jittered)")
save(fig, "L04_heights")

s = pd.read_csv(D / "sim1.csv")
a1 = rng.uniform(-20, 40, 250)
a2 = rng.uniform(-5, 5, 250)
fig, ax = plt.subplots(1, 2, figsize=(9, 3.4))
xx = np.array([0, 11])
for i in range(250):
    ax[0].plot(xx, a1[i] + a2[i] * xx, color="grey", alpha=.15, lw=.7)
ax[0].scatter(s.x, s.y, s=12, zorder=3)
ax[0].set(xlim=(0.5, 10.5), ylim=(0, 30), title="250 random lines", xlabel="x", ylabel="y")
fit = smf.ols("y ~ x", s).fit()
ax[1].scatter(s.x, s.y, s=12)
ax[1].plot(xx, fit.params.iloc[0] + fit.params.iloc[1] * xx, color="C3")
for x, y, yh in zip(s.x, s.y, fit.fittedvalues):
    ax[1].plot([x, x], [y, yh], color="C1", lw=.8)
ax[1].set(xlim=(0.5, 10.5), title="least squares line and residuals", xlabel="x", ylabel="y")
save(fig, "L05_sim1")

fb = pd.read_csv(D / "Forbes.csv")
fb["lp"] = np.log(fb.pres)
fig, ax = plt.subplots(2, 2, figsize=(9, 6))
for j, (col, lab) in enumerate([("pres", "Pressure"), ("lp", "log(Pressure)")]):
    f = smf.ols(f"{col} ~ bp", fb).fit()
    ax[0, j].scatter(fb.bp, fb[col], s=14)
    ax[0, j].plot(fb.bp, f.fittedvalues, color="C3")
    ax[0, j].set(xlabel="Temperature", ylabel=lab)
    ax[1, j].scatter(fb.bp, f.resid, s=14)
    ax[1, j].axhline(0, ls="--", color="k")
    ax[1, j].set(xlabel="Temperature", ylabel="Residuals")
save(fig, "L06_forbes")

w = pd.read_csv(D / "wblake.csv")
sn = pd.read_csv(D / "ftcollinssnow.csv")
fig, ax = plt.subplots(1, 2, figsize=(9, 3.5))
ax[0].scatter(w.Age + rng.uniform(-.15, .15, len(w)), w.Length, s=6, alpha=.6)
m = w.groupby("Age").Length.mean()
ax[0].plot(m.index, m.values, "o-", color="C3", label="mean length at age")
f = smf.ols("Length ~ Age", w).fit()
ax[0].plot([1, 8], f.params.iloc[0] + f.params.iloc[1] * np.array([1, 8]), "--", color="k", label="OLS line")
ax[0].set(xlabel="Age (years)", ylabel="Length (mm)", title="West Bearskin Lake bass")
ax[0].legend(fontsize=7)
ax[1].scatter(sn.Early, sn.Late, s=12)
f = smf.ols("Late ~ Early", sn).fit()
ax[1].plot([0, 45], f.params.iloc[0] + f.params.iloc[1] * np.array([0, 45]), color="C3")
ax[1].axhline(sn.Late.mean(), ls="--", color="k")
ax[1].set(xlabel="Early (Sep-Dec) snowfall", ylabel="Late (Jan-Jun) snowfall", title="Fort Collins snowfall")
save(fig, "L07_bass_snow")

# ---------- Week 5 ----------
ir = pd.read_csv(D / "iris.csv")
ir.columns = [c.replace(".", "_") for c in ir.columns]
B = pd.read_csv(D / "Boston.csv")
fig, ax = plt.subplots(1, 2, figsize=(9, 3.5))
f = smf.ols("Sepal_Length ~ Petal_Width", ir).fit()
ax[0].scatter(ir.Petal_Width, ir.Sepal_Length, s=10)
xs = np.linspace(0, 2.6, 2)
ax[0].plot(xs, f.params.iloc[0] + f.params.iloc[1] * xs, color="C3")
ax[0].set(xlabel="Petal.Width", ylabel="Sepal.Length", title="iris")
f = smf.ols("medv ~ lstat", B).fit()
ax[1].scatter(B.lstat, B.medv, s=6)
xs = np.linspace(0, 40, 2)
ax[1].plot(xs, f.params.iloc[0] + f.params.iloc[1] * xs, color="C3", lw=2)
ax[1].set(xlabel="lstat", ylabel="medv", title="Boston")
save(fig, "L15_iris_boston")

fig, ax = plt.subplots(1, 3, figsize=(10, 3.2))
infl = f.get_influence()
hv = infl.hat_matrix_diag
ax[0].scatter(f.fittedvalues, f.resid, s=6)
ax[0].axhline(0, color="k", ls="--")
ax[0].set(xlabel="fitted", ylabel="residual", title="Residuals vs fitted")
ax[1].scatter(f.fittedvalues, infl.resid_studentized_external, s=6)
ax[1].set(xlabel="fitted", ylabel="studentized residual", title="Studentized residuals")
ax[2].scatter(np.arange(1, len(hv) + 1), hv, s=6)
ax[2].set(xlabel="index", ylabel="leverage", title="Hat values")
save(fig, "L18_boston_diag")
print("figures written to", OUT)
