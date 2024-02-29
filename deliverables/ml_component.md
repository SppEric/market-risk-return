## <u> Machine Learning Component </u>

> Note: This project's machine learning components were originally implemented in tandem with our statistical tests, but for the sake of simplicity have been separated into this  file, ml_component.md. Some details from statisical_analyses.md may be referenced in this file.

# Machine Learning Component 1: 

### Overview
Our goal in this component was to analyze and predict the mean annualized returns for S&P 500 companies based on a variety of factors, but namely their beta values. This machine learning component was originally implemented in tandem with (or rather after deriving the results of the statistical test) a two-sample t-test, but has been separated for pedagogy. 

### MODEL CHOICE: Linear Regression
We built a regression model to predict the annualized return of S&P 500 companies based on their beta values. We then used the model to compare the predicted annualized return of high beta companies and low beta companies. The reason for implementing this algorithm is such that we can analyze outputs of the model to see if there exists a significant difference between the predicted annualized returns of high and low beta companies. 

In the implementation the model, we utilized k-fold validation (k = 5) to minimize the final testing loss. Our choice of loss metric was root mean squared error (RMSE). RMSE is a standard choice for a loss metric in linear regression and does not penalize large errors as severely as MSE. 

### Results:
###### Mean cross-validation score: -0.8040566023966509
###### Test RMSE: 0.4480831366870048

The above first parameter, mean cross-validation score, represents how well the model was able to generalize to unseen the unseen testing data; note that this negative score represents a somewhat poor fit. The above second parameter, test RMSE, represents the test RMSE of the best model (selected from our k-fold validation process); a loss of 0.44 is by all means not bad and performs better than the dummy random guessing model.

### Why did you use this ML algorithm ? 
We used linear regression with cross-validation to test the hypothesis that there is a linear relationship between the independent and dependent variables. This test was appropriate because it allowed you to model the relationship between the variables and evaluate the statistical significance of the coefficients.

### Which other tests did you consider or evaluate? 
There could be other statistical tests or machine learning algorithms that are more appropriate. For example, if we are interested in predicting a categorical outcome, logistic regression or decision trees could be more appropriate. Alternatively, if we have a large amount of data with many variables, we could consider using a machine learning algorithm like random forests or gradient boosting.

### What metric(s) did you use to measure success or failure, and why did you use it? 
We used the mean cross-validation score and the test RMSE to evaluate the performance of your model. The mean cross-validation score provides an estimate of the model's performance on new, unseen data. The test RMSE measures the average difference between the predicted and actual values of the dependent variable. These metrics were appropriate because they allowed you to assess the model's predictive accuracy and generalization performance.

### What challenges did you face evaluating the model? Did you have to clean or restructure your data?
We faced challenges related to missing data, outliers, multicollinearity, or other issues. Additionally, choosing the appropriate evaluation metrics and determining the statistical significance of the results were also challenging.

Based on several error messages we encountered, we had to reformat our stock_data JSON file to be compatible with the pandas DataFrame. Additionally, we had to preprocess and clean our data to remove missing values, handle outliers, and transform variables as needed.

### What is your interpretation of the results? Are you satisfied with your prediction accuracy? Intuitively, how do you react to the results? Why did you get the accuracy/success metric you have? Are you confident in the results? 
Based on the results, we can tentatively accept the hypothesis that there is a linear relationship between annualized risk and annualized return. However, the level of predictive accuracy may not be sufficient for all purposes. We may need to evaluate whether the model's performance is sufficient for our needs depending on the level of risk investors are comfortable with when making investment decisions based on these results. The accuracy of the model is slightly low for risk-averse investors to base their investment decisions off of the model alone.

The negative mean cross-validation score and positive test RMSE indicate that the model is not a perfect fit for the data, but it still provides some predictive accuracy. This could indicate that there is a better architecture that can model the data, or that the data cannot be modeled linearly.

The negative mean cross-validation score of -0.8040566023966509 and the test RMSE of 0.4480831366870048 suggest that the model has some level of predictive power, but it is not particularly accurate. This is not surprising, given that stock returns are notoriously difficult to predict with any degree of certainty. Nonetheless, the fact that the model was able to identify a statistically significant difference in returns between high- and low-beta stocks suggests that there is some signal in the data that is not purely random noise.

<br> <br>

# Machine Learning Component 2:

### Overview
Our goal in this component was to analyze and predict the mean annualized returns for S&P 500 companies based on a variety of factors, namely their annualized risk values. This machine learning component was originally implemented in tandem with (or rather after deriving the results of the statistical test) a two-sample t-test, but has been separated for pedagogy. This component was carried out after the first machine learning component, where we found that our linear regression model performed somewhat poorly in terms of prediction on beta values, so in this component, we attempt to use a different inputs to our machine learning model. 

### TECHNIQUE: Linear Regression
We will build a polynomial regression model to predict the annualized return of S&P 500 companies based on their annualized risk values. We will use the model to compare the predicted annualized returns of high annualized risk companies and low annualized risk companies to determine if the difference is statistically significant. We kept metrics as constant as possible, namely the k-value in k-fold validatoin and loss metric of RMSE.

In the implementation the model, we utilized k-fold validation (k = 5) to minimize the final testing loss. Our choice of loss metric was root mean squared error (RMSE). RMSE is a standard choice for a loss metric in linear regression and does not penalize large errors as severely as MSE. 

#### Results:
###### Mean cross-validation score: -0.7623398741108754
###### Test RMSE: 0.4150921783592476

The above first parameter, mean cross-validation score, represents how well the model was able to generalize to unseen the unseen testing data; note that this negative score represents a somewhat poor fit, though notably better than the first case which only depended on the beta value. The above second parameter, test RMSE, represents the test RMSE of the best model (selected from our k-fold validation process); a loss of 0.41 is once again better than the above model, evident by its improved ability to generalize to the unseen case.

### Why did you use this ML algorithm ? 
We considered other statistical tests or machine learning algorithms, such as logistic regression, decision trees, random forests, or gradient boosting. However, linear regression was deemed appropriate for the current hypothesis as it directly tests the relationship between the variables.

### Which other tests did you consider or evaluate? 
There could be other statistical tests or machine learning algorithms that are more appropriate. For example, if we are interested in predicting a categorical outcome, logistic regression or decision trees could be more appropriate. Alternatively, if we have a large amount of data with many variables, we could consider using a machine learning algorithm like random forests or gradient boosting.

### What metric(s) did you use to measure success or failure, and why did you use it? 
We used the mean cross-validation score and the test RMSE to evaluate the performance of the model. The mean cross-validation score provides an estimate of the model's performance on new, unseen data. The test RMSE measures the average difference between the predicted and actual values of the dependent variable. These metrics were appropriate because they allowed us to assess the model's predictive accuracy and generalization performance.

### What challenges did you face evaluating the model? Did you have to clean or restructure your data?
We faced challenges related to missing data, outliers, multicollinearity, or other issues. Additionally, choosing the appropriate evaluation metrics and determining the statistical significance of the results were also challenging.

Based on several error messages we encountered, we had to reformat our stock_data JSON file to be compatible with the pandas DataFrame. Additionally, we had to preprocess and clean our data to remove missing values, handle outliers, and transform variables as needed.

### What is your interpretation of the results? Are you satisfied with your prediction accuracy? Intuitively, how do you react to the results? Why did you get the accuracy/success metric you have? Are you confident in the results? 
The negative mean cross-validation score of -0.7623398741108754 and the test RMSE of 0.4150921783592476 suggest that the model's predictive power is not particularly high. This is not surprising, considering that predicting stock returns is a complex task with many variables at play. While the model was able to identify a statistically significant difference in returns between high- and low-annualized risk stocks, the overall accuracy may not be suitable for making investment decisions, especially for risk-averse investors.

In summary, the results provide some evidence for the hypothesis that there is a significant difference in mean annualized returns between S&P 500 companies with higher and lower annualized risks. However, the model's predictive accuracy is not ideal, and further refinement or exploration of alternative approaches may be necessary to improve its performance. Additionally, investors should consider other factors and risk tolerance when making investment decisions based on these results.
