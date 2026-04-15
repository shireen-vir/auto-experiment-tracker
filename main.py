def main():
    """
    Auto Experiment Tracker is a data science tool designed to track and record 
    experiments, providing an easy way to manage and compare the results.
    
    Parameters:
    None
    
    Returns:
    None
    """
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error

    # Sample dataset
    data = {
        'X': np.random.rand(100),
        'y': np.random.rand(100)
    }

    df = pd.DataFrame(data)

    # Split dataset into training set and test set
    X = df['X'].values.reshape(-1, 1)
    y = df['y'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a linear regression model
    model = LinearRegression()

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, predictions)

    print("Mean Squared Error: ", mse)

if __name__ == "__main__":
    main()