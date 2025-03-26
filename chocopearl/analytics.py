import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import statsmodels.api as sm


def correlation_matrix(df,numeric_only=True,cmap='coolwarm'):
    correlation_mat = df.corr(numeric_only=numeric_only)
    correlation_mat = correlation_mat.style.background_gradient(cmap=cmap)
    return correlation_mat


def scatter_predictors_vs_target(df,target):
    ## Distribucion de las predictoras respecto a la variable target
    df_numeric = df.select_dtypes(include=['number'])
    preds = df_numeric.columns.drop(target)
    n_preds = len(preds)

    fig, axes = plt.subplots(nrows=int(np.ceil(n_preds /3)), ncols=3, figsize=(15, 5 * int(np.ceil(n_preds /3))))
    axes = axes.flatten()

    for i,col in enumerate(preds):
        sns.scatterplot(x=df_numeric[col], y=df_numeric[target], alpha=0.5, ax=axes[i])
        axes[i].set_title(f"'{col}' vs. '{target}'")

    plt.tight_layout()
    plt.show()
    
def plot_lm_residuals(model_smf_ols):
    residuals = model_smf_ols.resid
    fitted_values = model_smf_ols.fittedvalues

    # Normalidad: Histograma y Q-Q Plot

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes=axes.flatten()
    # Histograma de residuos
    sns.histplot(residuals, bins=20, kde=True, ax=axes[0])
    axes[0].set_title("Residuals Histogram")
    axes[0].set_xlabel("Residuals")
    axes[0].set_ylabel("Frequency")

    # Q-Q plot 
    sm.qqplot(residuals, line="45", fit=True, ax=axes[1])
    axes[1].set_title("Q-Q Plot of Residuals")


    # Independencia: Residuos vs. Orden 

    axes[2].plot(list(range(len(residuals))),residuals, alpha=0.6)
    axes[2].axhline(y=0, color="r", linestyle="--")
    axes[2].set_title("Independence: Residuals vs. Index")
    axes[2].set_xlabel("Index")
    axes[2].set_ylabel("Residuals")


    # Homocedasticidad: Residuos vs. Valores predichos

    sns.scatterplot(x=fitted_values, y=residuals, alpha=0.6,ax=axes[3])
    axes[3].axhline(y=0, color="r", linestyle="--")
    axes[3].set_title("Homoscedasticity: Residuals vs. Fitted Values")
    axes[3].set_xlabel("Fitted Values")
    axes[3].set_ylabel("Residuals")


    plt.tight_layout()
    plt.show()


