import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/fivethirtyeight/data/master/covid-geography/mmsa-icu-beds.csv"
)

# summary statistics (mean, median, standard deviation)
def statistics(p=False):
    icu_beds = df["icu_beds"]
    bed_mean = icu_beds.mean()
    bed_median = icu_beds.median()
    bed_std = icu_beds.std()
    if p:
        summary_stats = (
            f"Mean = {bed_mean}, Median = {bed_median}, Standard Deviation = {bed_std}"
        )
        print(summary_stats)
    return bed_mean, bed_median, bed_std


# count columns and rows for test
def count_col():
    num_col = len(df.columns)
    return num_col

def count_row():
    num_row = len(df)
    return num_row
