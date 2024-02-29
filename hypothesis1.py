import json 
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
from sklearn.linear_model import LinearRegression
import scipy.stats as stats
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score, KFold
from sklearn.metrics import mean_squared_error

# Load the data from the JSON file
with open('stock_data.json', 'r') as f:
    data = json.load(f)

# Convert the data into a pandas DataFrame
df = pd.DataFrame.from_dict(data, orient='index')

# Split the data into training and testing sets
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Standardize the beta values and annualized returns in the training set
scaler = StandardScaler()
train_df[['beta', 'annualized_mean_return']] = scaler.fit_transform(train_df[['beta', 'annualized_mean_return']])

# Extract the beta and annualized return values from the testing set
X_test = test_df['beta'].values.reshape(-1, 1)
y_test = test_df['annualized_mean_return'].values

# Save the scaler for later use on the testing set
joblib.dump(scaler, 'scaler.pkl')

# Load the scaler from step 2
scaler = joblib.load('scaler.pkl')

# Standardize the beta values and annualized returns in the testing set
test_df[['beta', 'annualized_mean_return']] = scaler.transform(test_df[['beta', 'annualized_mean_return']])

# Extract the beta and annualized return values from the training set
X_train = train_df['beta'].values.reshape(-1, 1)
y_train = train_df['annualized_mean_return'].values

# Create a linear regression model and fit it to the training data
model = LinearRegression()
model.fit(X_train, y_train)

# Extract the beta values from the testing set
X_test = test_df['beta'].values.reshape(-1, 1)

# Use the trained model to predict the annualized returns of the testing set
y_pred = model.predict(X_test)

# Define the threshold value used to split the high-beta and low-beta groups
threshold = 1.5

# Extract the predicted annualized returns for the high-beta group
y_high_beta = [y_pred[i] for i in range(len(test_df)) if test_df.iloc[i]['beta'] > threshold]

# Extract the predicted annualized returns for the low-beta group
y_low_beta = [y_pred[i] for i in range(len(test_df)) if test_df.iloc[i]['beta'] < threshold]

# Perform a t-test to determine if the difference between the means of the two groups is significant
t_stat, p_value = stats.ttest_ind(y_high_beta, y_low_beta)

# Print the results of the t-test
print("t-statistic: ", t_stat)
print("p-value: ", p_value)

# Split data into X (features) and y (target variable)
X = np.array([data[company]['beta'] for company in data.keys()]).reshape(-1, 1)
y = np.array([data[company]['annualized_mean_return'] for company in data.keys()])

# Create k-fold cross-validation object with k=10
kf = KFold(n_splits=10, shuffle=True, random_state=42)

# Create list to store cross-validation scores
cv_scores = []

# Loop over each fold
for train_index, val_index in kf.split(X_train):
    # Split data into training and validation sets
    X_train_fold, X_val_fold = X_train[train_index], X_train[val_index]
    y_train_fold, y_val_fold = y_train[train_index], y_train[val_index]

    # Fit Ridge regression model with L2 regularization
    alpha = 0.1  # Regularization strength
    model = Ridge(alpha=alpha)
    model.fit(X_train_fold, y_train_fold)

    # Evaluate model on validation set and store score
    val_score = model.score(X_val_fold, y_val_fold)
    cv_scores.append(val_score)

# Compute mean cross-validation score
mean_cv_score = np.mean(cv_scores)

# Evaluate model on testing set and compute RMSE
y_pred = model.predict(X_test)
test_rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# Print mean cross-validation score and test RMSE
print('Mean cross-validation score:', mean_cv_score)
print('Test RMSE:', test_rmse)
