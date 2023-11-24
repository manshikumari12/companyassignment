

import pandas as pd

def calculate_moving_average(csv_file):
    df = pd.read_csv(csv_file)
    window_size = 3

    if len(df) >= window_size:
    
        df['Moving_Avg'] = df['Close'].rolling(window=window_size).mean().shift(-window_size + 1)

        print("Simple Moving Average:")
        print(df[['Date', 'Time', 'Close', 'Moving_Avg']])

    
