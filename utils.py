import pandas as pd
import numpy as np
import os

def load_data(file_path):
    """Loads data from a CSV file."""
    return pd.read_csv(file_path)

def save_data(data, file_path):
    """Saves data to a CSV file."""
    data.to_csv(file_path, index=False)

def main():
    """Main function for the auto-experiment-tracker tool."""
    # Set the directory path for the experiment data
    experiment_dir = 'experiment_data'
    
    # Check if the directory exists, if not create it
    if not os.path.exists(experiment_dir):
        os.makedirs(experiment_dir)
    
    # Load the experiment data
    experiment_data = load_data('experiment.csv')
    
    # Perform some data analysis
    analysis_results = experiment_data.describe()
    
    # Save the analysis results
    save_data(analysis_results, os.path.join(experiment_dir, 'analysis_results.csv'))
    
    print("Experiment analysis completed successfully.")

if __name__ == "__main__":
    main()