"""
DATA602
Discussion Post #8
Andrew Bowen
"""

import pandas as pd


if __name__ == "__main__":
    # Read in dataset from csv URL
    # https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=TOI
    url = "https://raw.githubusercontent.com/andrewbowen19/advancedProgrammingData602/main/data/TOI_2023.03.07_15.50.16.csv"
    df = pd.read_csv(url, header=69)

    # Print summary stats on new dataframe
    print(df.describe())