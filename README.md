# Linear Statistical Models — Lecture Notes and Notebooks (Weeks 1–5, Lectures 1–18)

These are companion notes for the IIT Madras BS course **Linear Statistical Models** (Prof. Siva Athreya),
[YouTube playlist](https://youtube.com/playlist?list=PLZ2ps__7DhBb_QIWA52QQHVhpuRKBOq7g).
The material has two parts:

- a LaTeX book (`latex/main.tex` → `main.pdf`, 104 pages) with one chapter per week and one section per lecture;
- executed Python notebooks (`notebooks/`), one per lecture plus one exercises notebook per week.

## Sources — please read

The video transcripts could **not** be accessed, so each lecture header shows timestamps as "not available".
The notes are built from the instructor's published course material at
<https://www.isibang.ac.in/~athreya/Teaching/LSM/>:

| Week | Lectures | Source used |
|------|----------|-------------|
| 1 | 1–3   | `Jan26notes.pdf` (slides) |
| 2 | 4–7   | `Feb2.pdf` (slides) |
| 3 | 8–10  | `Feb9.pdf` (handwritten notes) |
| 4 | 11–14 | `Feb14.pdf` (handwritten notes, "Lectures 2–4"), matched to videos by title |
| 5 | 15–18 | `Feb21.r` (R code) and `hw56.pdf` (assignment). **The Week-5 lecture PDF `Feb21.pdf` was not accessed**; the theory is standard material in the course's notation. |

Material beyond the sources appears in boxes titled **"Supplementary …"**. Every number in the notes was reproduced in the notebooks.
The course page lists 43 videos, but the playlist has 52; 9 videos are not yet matched to a week.

## Compiling the notes

```bash
cd latex
latexmk -pdf main.tex        # or: pdflatex main.tex; pdflatex main.tex
```

This needs a TeX Live installation with `cmbright`, `bbm` (texlive-fonts-extra), `ulem` (texlive-plain-generic),
`pgfplots`, `mdframed` and `cleveref`. The figures in `latex/figures/` are pre-built. To regenerate them, run
`python figures/make_figures.py` from `latex/`.

**Notes on `lindrew.sty`.** The file is included **unchanged**.

- The line `\newcommand{\the}{\vartheta}` cannot work, because `\the` is a TeX primitive, and it stops every engine with an error.
  `main.tex` turns this one error into a warning around `\usepackage[formal]{lindrew}`. The notes write `\vartheta` directly.
- The label "Quiding Question" on the objectives box comes from the `.sty` and is left as it is.

## Running the notebooks

```bash
python -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m ipykernel install --user --name lsm --display-name "Python (LSM)"
```

In VS Code, open a notebook and choose the **Python (LSM)** kernel, or the `.venv` interpreter. The notebooks:

- read data only from `data/`, located by walking up from the notebook's folder, so keep the folder layout;
- use the fixed seed `np.random.default_rng(2024)`;
- download nothing.

To re-run everything:

```bash
jupyter nbconvert --to notebook --execute --inplace notebooks/week*/*.ipynb
```

## Lecture ↔ file map

| # | Lecture | LaTeX section | Notebook |
|---|---------|---------------|----------|
| 1 | Basic Statistics and Introduction to R | `week01/lec01_basic_stats_intro_R.tex` | `week01/L01_basic_stats_intro.ipynb` |
| 2 | Data Visualization using ggplot2 | `week01/lec02_ggplot2.tex` | `week01/L02_ggplot2.ipynb` |
| 3 | Data Visualization using ggplot() — geoms | `week01/lec03_ggplot_geoms.tex` | `week01/L03_ggplot_geoms.ipynb` |
| 4 | Introduction to Linear Models | `week02/lec04_intro_linear_models.tex` | `week02/L04_intro_linear_models.ipynb` |
| 5 | Basics of Linear Models | `week02/lec05_basics_linear_models.tex` | `week02/L05_basics_linear_models.ipynb` |
| 6 | More on Linear Models: Residuals | `week02/lec06_residuals.tex` | `week02/L06_residuals.ipynb` |
| 7 | Playing with More Data Sets | `week02/lec07_more_datasets.tex` | `week02/L07_more_datasets.ipynb` |
| 8 | Fundamentals of Linear Models and the Estimation Problem | `week03/lec08_fundamentals_estimation.tex` | `week03/L08_oneway_sums_of_squares.ipynb` |
| 9 | Theory of Linear Models | `week03/lec09_theory_linear_models.tex` | `week03/L09_theory_linear_models.ipynb` |
| 10 | The Problem of Parameter Estimation | `week03/lec10_parameter_estimation.tex` | `week03/L10_estimability.ipynb` |
| 11 | Different Classifications of Linear Models | `week04/lec11_classifications.tex` | `week04/L11_classification_designs.ipynb` |
| 12 | Normal Equations and Existence of LSE | `week04/lec12_normal_equations.tex` | `week04/L12_normal_equations.ipynb` |
| 13 | A Theorem on Least Squares Estimates | `week04/lec13_theorem_lse.tex` | `week04/L13_uniqueness_of_lse.ipynb` |
| 14 | Fundamentals of Matrices and the Projection P_X | `week04/lec14_fundamentals_matrices.tex` | `week04/L14_matrices_projection.ipynb` |
| 15 | Estimating the Coefficients of Linear Models | `week05/lec15_estimating_coefficients.tex` | `week05/L15_estimating_coefficients.ipynb` |
| 16 | Interval Estimates and Hypothesis Tests | `week05/lec16_intervals_tests.tex` | `week05/L16_intervals_tests.ipynb` |
| 17 | Assessing the Linear Model: RSE and R² | `week05/lec17_rse_rsquare.tex` | `week05/L17_rse_rsquared.ipynb` |
| 18 | Computation of Least Squares Estimates in R | `week05/lec18_computation_R.tex` | `week05/L18_computation_in_R.ipynb` |

Paths are relative to `latex/chapters/` and `notebooks/`. Each week also has `weekNN.tex`, which holds the chapter intro and the exercise solutions, and `notebooks/weekNN/WNN_exercises.ipynb`.

## Data (`data/`)

The files are `airquality`, `mpg`, `sim1`, `Heights`, `Forbes`, `wblake`, `ftcollinssnow`, `iris` and `Boston`.
They are CSV exports of the R datasets used in the course (from R base, ggplot2, modelr, alr4 and MASS).

## Status

Weeks 1–5 (Lectures 1–18) are complete. Weeks 6–12 are pending.
