# <u> Analysis </u>
https://docs.google.com/document/d/1F2LwBz8P0Z6OEajBwEShBrxolS_L1Kd9DCLDOdqKDuI/edit?usp=sharing 

# <u> Hypotheses Overview </u>

### Hypothesis 1: The mean annualized return of S&P 500 companies with higher betas is significantly different from the mean annualized return of S&P 500 companies with lower betas.

#### Statistical Testing Method: Two-Sample t-Test

##### Null Hypothesis: The mean annualized return of S&P 500 companies with higher betas is equal to or lower than the mean annualized return of S&P 500 companies with lower betas.
##### Alternative Hypothesis: The mean annualized return of S&P 500 companies with higher betas is higher than the mean annualized return of S&P 500 companies with lower betas.

### Reasoning:
This revised hypothesis seeks to investigate whether there is a difference in mean annualized returns between S&P 500 companies with higher betas (greater than 1) and those with lower betas (less than or equal to 1). A two-sample t-test can be used to compare the means of two independent groups and can help determine whether any observed difference between the means is statistically significant.

### Hypothesis 2: The average abnormal return of the stock market on November 3, 2020, is significantly different from zero.

#### Statistical Testing Method: One-Sample t-Test

##### Null Hypothesis: The average abnormal return of the stock market on November 3, 2020, is equal to zero.

##### Alternative Hypothesis: The average abnormal return of the stock market on November 3, 2020, is not equal to zero.

### Reasoning:
This revised hypothesis seeks to investigate whether there was a significant change in the average abnormal return of the stock market on November 3, 2020, which was the day of the US presidential election. The abnormal return is defined as the difference between the actual return and the expected return of a stock. A one-sample t-test can be used to test whether the observed mean abnormal return is significantly different from the expected mean abnormal return, which is assumed to be zero under the null hypothesis.

### Hypothesis 3: The mean annualized return of S&P 500 companies with higher annualized risks is significantly different from the mean annualized return of S&P 500 companies with lower annualized risks.

#### Statistical Testing Method: Two-Sample t-Test

##### Null Hypothesis: The mean annualized return of S&P 500 companies with higher annualized risks is equal to or lower than the mean annualized return of S&P 500 companies with lower annualized risks.

##### Alternative Hypothesis: The mean annualized return of S&P 500 companies with higher annualized risks is higher than the mean annualized return of S&P 500 companies with lower annualized risks.

### Reasoning:
This hypothesis seeks to investigate whether there is a difference in mean annualized returns between S&P 500 companies with higher annualized risks and those with lower annualized risks. A two-sample t-test can be used to compare the means of two independent groups and can help determine whether any observed difference between the means is statistically significant.


<br><br><br>


# <u> Hypothesis Analyses </u>

## <u> Hypothesis 1 </u>:
##### Null Hypothesis: The mean annualized return of S&P 500 companies with higher betas is not significantly different from the mean annualized return of S&P 500 companies with lower betas.
##### Alternative Hypothesis: The mean annualized return of S&P 500 companies with higher betas is significantly different from the mean annualized return of S&P 500 companies with lower betas.

### STATISTICAL TECHNIQUE: Two Sample t-Test (alpha: 0.05) 
We compare the predicted annualized return of high beta companies and low beta companies and see if the difference is statistically significant.

#### RESULTS: 
###### t-statistic:  9.027627434487139
###### p-value:  1.4426540224673013e-14

### Why did you use this statistical test? 
We used the two sample t-test because we were analyzing the statistical significance between two groups: companies with low beta values and companies with high beta values. This test was appropriate because it allowed you to model the relationship between the variables and evaluate the statistical significance of the coefficients.

### Which other tests did you consider or evaluate? 
In this case, the two sample t-test is applicable since we are dividing the data into two and then comparing the means. Another statistical test considered was the one sample t-test, though this would be testing a different hypothesis (that is, seeing if the samples with low or high betas were significantly different from the population mean).

### Did you have to clean or restructure your data?
Yes, based on several error messages we encountered, we had to reformat our stock_data JSON file to be compatible with the pandas DataFrame. Additionally, we had to preprocess and clean our data to remove missing values, handle outliers, and transform variables as needed.

### What is your interpretation of the results? Do you accept or deny the hypothesis?
The results suggest that there is a since the p-value is under our chosen alpha value, we reject the null hypothesis. This is to say, the mean annualized return of S&P 500 companies with higher betas is significantly different from the mean annualized return of S&P 500 companies with lower betas.


### Intuitively, how do you react to the results? Are you confident in the results?
Based on the results, it seems that there is a statistically significant difference between the mean annualized returns of S&P 500 companies with higher betas and those with lower betas. This is indicated by the t-statistic of 9.027627434487139 and the very small p-value of 1.4426540224673013e-14.

From an investment perspective, beta is a measure of systematic risk, or the risk associated with the overall market. Companies with higher betas are generally considered riskier investments because their stock prices tend to be more volatile and sensitive to market fluctuations. As a result, investors may demand higher returns to compensate for the additional risk they are taking on.

The fact that there is a significant difference in annualized returns between companies with higher and lower betas suggests that the market is indeed compensating investors for the additional risk associated with higher-beta stocks. This is consistent with the Capital Asset Pricing Model (CAPM), which states that expected return is proportional to beta.


<br><br>

## <u> Hypothesis 2 </u>:
The average abnormal return of the stock market on November 3, 2020, is significantly different from zero.

### Statistical Testing Method: One-sample t-test
##### Null Hypothesis: The average abnormal return of the stock market on November 3, 2020, is equal to zero.
##### Alternative Hypothesis: The average abnormal return of the stock market on November 3, 2020, is not equal to zero.

### TECHNIQUE: One Sample z-Test (alpha: 0.05)
#### RESULTS:
##### H_0: average abnormal return of the stock market on November 3, 2020 is equal to zero
##### H_a: average abnormal return of the stock market on November 3, 2020 is not equal to zero
###### Z-score with value = 0: 0.21373513864376223
###### P-value with value = 0: 0.8307536077929717
Note here that the p-value is significantly higher than that of our chosen alpha value. Consequently, we fail to reject the null hypothesis.

<br>

##### H_0: average abnormal return of the stock market on November 3, 2020 is equal to the sample mean abnormal return
##### H_a: average abnormal return of the stock market on November 3, 2020 is not equal to the sample mean abnormal return
###### Z-score with value = mean_abnormal_returns: 0.1048038305434851
###### P-value with value = mean_abnormal_returns: 0.9165314704574674
Note here that the p-value is significantly higher than that of our chosen alpha value. Consequently, we fail to reject the null hypothesis.


### Why did you use this statistical test?
We use a 1-sample t-test here in order to see if the abnormal return of the stock market significantly differs from the abnormal return for day to day operations. The 1-sample t-test is applicable in this situation because in the first hypothesis, only one sample was required and was used to determine the sample mean. In the second hypothesis, there was additionally only one sample used. 

###  Which other tests did you consider or evaluate?
We considered two-sample z-tests to compare each company’s mean abnormal return with the others in order to isolate which companies had greater variation in that value and thus remove any outliers but it would have been a large amount of calculations and impossible to do with our hardware.

###  Did you have to clean or restructure your data?
A few of the data points includes NaN values, indicative of a lack of data for some days. These were initially troublesome to deal with, but our group dealt with this by ignoring NaN values (see np.nanmean). Aside from this, the data was not restructured significantly as we had this sort of hypothesis in mind when preprocessing and scraping our data.

### What is your interpretation of the results?
Our interpretation of the result is that the effects of abnormal returns on November 3rd, that of election day, were not statistically significantly different from the mean abnormal return of days leading up to and after the event. This would imply that while the November 3rd election had an effect on some other variables, mean abnormal return of stocks were not big enough. 

###  Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy?
Because the p-value is (much) greater than 0.05 for both hypotheses, this means that we cannot reject the null hypothesis.

### Intuitively, how do you react to the results? Are you confident in the results?
This result makes a lot of sense. A quick visual inspection of the data shows that most of the abnormal returns for that date are close to 0. We are confident in this result because empirically, one wouldn’t expect the stock market to change too drastically after the result of the presidential election.

<br><br>

## <u> Hypothesis 3 </u>:
##### Null Hypothesis: The mean annualized return of S&P 500 companies with higher annualized risks is not significantly different from the mean annualized return of S&P 500 companies with lower annualized risks.
##### Alternate Hypothesis: The mean annualized return of S&P 500 companies with higher annualized risks is significantly different from the mean annualized return of S&P 500 companies with lower annualized risks.

### TECHNIQUE: Two Sample t-Test
We compare the predicted annualized return of low and high annualized risks companies and see if the difference is statistically significant.

### VALIDATION: K-fold cross-validation
#### RESULTS:
###### t-statistic: 7.39673826859103
###### p-value: 4.285239077218654e-11

### Why did you use this statistical test or ML algorithm?
We used the two sample t-test because we were analyzing the statistical significance between two groups: companies with low annualized risk values and companies with high annualized risk values. This test was appropriate because it allowed you to model the relationship between the variables and evaluate the statistical significance of the coefficients.

### Which other tests did you consider or evaluate?
In this case, the two sample t-test is applicable since we are dividing the data into two and then comparing the means. Another statistical test considered was the one sample t-test, though this would be testing a different hypothesis (that is, seeing if the samples with low or high betas were significantly different from the population mean).

### Did you have to clean or restructure your data?
Yes, we reformatted the stock_data JSON file to be compatible with the pandas DataFrame. We also preprocessed and cleaned the data to remove missing values, handle outliers, and transform variables as needed.

### What is your interpretation of the results? Do you accept or deny the hypothesis?
The results suggest that there is a since the p-value is under our chosen alpha value, we reject the null hypothesis. This is to say, the mean annualized return of S&P 500 companies with higher annualized risk is significantly different from the mean annualized return of S&P 500 companies with lower annualized risk.

From `ml_component.md`, there is a statistically significant linear relationship between annualized risk and annualized return. The negative mean cross-validation score and the positive test RMSE indicate that the model is not a perfect fit for the data, but it still provides some predictive accuracy.

### Intuitively, how do you react to the results? Are you confident in the results?
The results show that there is a statistically significant difference between the mean annualized returns of S&P 500 companies with higher annualized risks and those with lower annualized risks, as indicated by the t-statistic of 7.39673826859103 and the small p-value of 4.285239077218654e-11.

This outcome aligns with the general expectation that higher risk investments tend to yield higher returns to compensate for the increased volatility and uncertainty. The results, therefore, seem reasonable and consistent with the risk-return tradeoff principle in finance.

However, (in reference to `ml_component.md`) the negative mean cross-validation score of -0.7623398741108754 and the test RMSE of 0.4150921783592476 suggest that the model's predictive power is not particularly high. This is not surprising, considering that predicting stock returns is a complex task with many variables at play. While the model was able to identify a statistically significant difference in returns between high- and low-annualized risk stocks, the overall accuracy may not be suitable for making investment decisions, especially for risk-averse investors.

In summary, the results provide some evidence for the hypothesis that there is a significant difference in mean annualized returns between S&P 500 companies with higher and lower annualized risks. However, the model's predictive accuracy is not ideal, and further refinement or exploration of alternative approaches may be necessary to improve its performance. Additionally, investors should consider other factors and risk tolerance when making investment decisions based on these results.

<br><br>

## <u> Machine Learning Components </u>

> Note: This project's machine learning components were originally implemented in tandem with our statistical tests, but for the sake of simplicity have been separated into the separate file, ml_component.md. Some details from statisical_analyses.md may be referenced in said file.