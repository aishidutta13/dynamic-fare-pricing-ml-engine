import pandas as pd


def load_taxi_data(path):
    df = pd.read_parquet(path)
    return df


def clean_taxi_data(df):
    df = df.copy()

    df = df.dropna()

    df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
    df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])

    df["trip_duration_minutes"] = (
        df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]
    ).dt.total_seconds() / 60

    df["hour"] = df["tpep_pickup_datetime"].dt.hour
    df["day_of_week"] = df["tpep_pickup_datetime"].dt.dayofweek

    df["is_peak_hour"] = df["hour"].isin([7, 8, 9, 17, 18, 19]).astype(int)

    df = df[
        (df["fare_amount"] > 0)
        & (df["trip_distance"] > 0)
        & (df["trip_duration_minutes"] > 0)
    ]

    return df


def save_processed_data(df, output_path):
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    taxi_path = "data/yellow_tripdata_2023-11.parquet"
    output_path = "data/processed_taxi_data.csv"

    taxi_df = load_taxi_data(taxi_path)
    processed_df = clean_taxi_data(taxi_df)
    save_processed_data(processed_df, output_path)

    print("Data preprocessing completed successfully.")
