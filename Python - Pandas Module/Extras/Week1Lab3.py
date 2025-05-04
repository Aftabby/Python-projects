import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import various functions from scikit-learn to help with the model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics



# Open the notebook
df = pd.read_csv('data/world_happiness.csv')

# Rename the column names so they dont contain spaces
df = df.rename(columns={i: "_".join(i.split(" ")).lower() for i in df.columns})

# Drop all of the rows which contain empty values. These will not be good for fitting.
df = df.dropna()

# Show the dataframe
df.head()

#The Seaborn pairplot is a very useful function that automatically plots the scatter plots between each pair of columns in the dataframe
sns.pairplot(df)

# Get the data from the dataframe.
X = df[['log_gdp_per_capita']]
y = df['life_ladder']

# Create the train-test split
# Note the test_size=0.2. This means you will use 20% of the data in your test set.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Show how X_train and y_train look like
print(f"Independent (X) variable:\n{X_train.values}\n")
print(f"Dependent (y) variable:\n{y_train.values}")

lr = LinearRegression().fit(X_train, y_train)

b = lr.intercept_
w = lr.coef_
print(f"Model parameters:\nw: {w},\nb: {b}")

# Make a prediction using lr.predict()
y_test_preds = lr.predict(X_test)

# Make a prediction by hand using w, b.
y_pred = np.dot(X_test, w) + b

# Check whether both results are the same
print(f"prediction using np.dot() and predictions using lr.predict are the same: {(y_pred == y_test_preds).all()}\n")

# Compare some of the predictions with actual (target) values.
print(f"Last four predictions on the test set:\n{y_pred[:4]}\n" )
print(f"Target values \n{y_test[:4].values}\n")

mae = metrics.mean_absolute_error(y_test, y_test_preds)
print(f"Mean Absolute Error on the test set: {mae:.2f}")

plt.figure()
plt.scatter(X_train, y_train, label = 'Training Data')
plt.scatter(X_test, y_pred, label = 'Predictions on the Test Set')
plt.legend()
plt.show()




# ======= Multiple Linear Regression =======
#fit_and_plot_linear_model: This function is very similar to the work you already did above. The key difference is that it can take more than one feature at a time, so you will be able to experiment with building models with two or more explanatory variables.
def fit_and_plot_linear_model(data, features):
    
    # Create a list of features you want to use as explanatory variables
    features = list(features)
    
    # Create the linear regression model
    
    # Select the data
    y = data['life_ladder']
    X = data[features]
    # Create a train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    # Fit the linear regression model
    lr = LinearRegression().fit(X_train, y_train)

    y_test_preds = lr.predict(X_test)
    
    # Calculate and print out the mean absolute error
    mae = metrics.mean_absolute_error(y_test, y_test_preds)
    print(f"Mean Absolute Error: {mae:.2f}\n")

# List of all possible predictor variables
predictors = ['year', 'log_gdp_per_capita', 'social_support', 'healthy_life_expectancy_at_birth', 'freedom_to_make_life_choices', 'generosity', 'perceptions_of_corruption', 'positive_affect', 'negative_affect']




