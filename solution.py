import pandas as pd
import numpy as np

from scipy.stats import mannwhitneyu

chat_id = 1395253289 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.03
    pval = mannwhitneyu(x, y).pvalue
    return pval < alpha # Ваш ответ, True или False
