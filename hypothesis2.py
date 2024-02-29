import json 
import numpy as np
import pandas as pd
import scipy.stats as stats
from statsmodels.stats import weightstats as stests

# Load the data from the JSON file
with open('me_output.json', 'r') as f:
    data = json.load(f)

# Hypothesis 1: 11/3 abnormal returns are not signficantly different from 0
total_abnormal_return = []
for company in data:
    company_data = company['data']

    total_abnormal_return.append(company_data[21]['abnormal_return'])

market_abnormal_return = np.mean(total_abnormal_return)

test_statistic, p_value = stests.ztest(total_abnormal_return, value=0)
print(test_statistic)
print(p_value)

# Hypothesis 2: 11/3 abnormal returns are not significantly different from the sample mean
total_ab_returns = []
for company in data:
    company_data = company['data']
    mean_abornmal_return = np.nanmean([datum['abnormal_return'] for datum in company_data])
    total_ab_returns += [mean_abornmal_return]
mean_ab_returns = np.mean(total_ab_returns)

test_statistic, p_value = stests.ztest(total_abnormal_return, value=mean_ab_returns)
print(test_statistic)
print(p_value)
