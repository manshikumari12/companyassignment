

import csv
from datetime import datetime
from moving_average import calculate_moving_average

def process_data(data):
    for instrument, price in data.items():
        olhc_data = convert_to_olhc(instrument, price)
        record_to_csv(instrument, olhc_data)

def convert_to_olhc(instrument, price):
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    open_price = price
    low_price = price
    high_price = price
    close_price = price

    return {"Instrument": instrument, "Date": timestamp, "Time": timestamp.split()[1],
            "Open": open_price, "Low": low_price, "High": high_price, "Close": close_price}

def record_to_csv(instrument, olhc_data):
    csv_file = f"{instrument}_data.csv"

    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow(["Instrument", "Date", "Time", "Open", "Low", "High", "Close"])

        writer.writerow([olhc_data["Instrument"], olhc_data["Date"], olhc_data["Time"],
                         olhc_data["Open"], olhc_data["Low"], olhc_data["High"], olhc_data["Close"]])

    calculate_moving_average(csv_file)
