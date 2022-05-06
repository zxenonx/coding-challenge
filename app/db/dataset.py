import pandas as pd
import numpy as np

def clean(dataset_url: str) -> pd.DataFrame:

    # initialize pandas dataframe with the csv file with the columns specified
    columns = [
        "School Name",
        "Category",
        "Total Enrollment",
        "#Grade K",
        "#Grade 1",
        "#Grade 2",
        "#Grade 3",
        "#Grade 4",
        "#Grade 5",
        "#Grade 6",
        "#Grade 7",
        "#Grade 8",
        "#Female",
        "%Female",
        "#Male",
        "%Male",
    ]

    df = pd.read_csv(dataset_url, usecols=columns)

    new_columns = {
        "School Name": "school_name",
        "Category": "category",
        "Total Enrollment": "total_enrollment",
        "#Grade K": "grade_k",
        "#Grade 1": "grade_1",
        "#Grade 2": "grade_2",
        "#Grade 3": "grade_3",
        "#Grade 4": "grade_4",
        "#Grade 5": "grade_5",
        "#Grade 6": "grade_6",
        "#Grade 7": "grade_7",
        "#Grade 8": "grade_8",
        "#Female": "total_female",
        "%Female": "ratio_female",
        "#Male": "total_male",
        "%Male": "ratio_male",
    }

    df.rename(columns=new_columns, inplace=True)

    # remove all rows in the dataframe where school_name is empty
    df.drop(df[df["school_name"].isnull() == True].index, inplace=True)

    # remove all rows in the dataframe where total_enrollment is empty
    df.drop(df[df["total_enrollment"].isnull() == True].index, inplace=True)

    # replace No Data by np.nan in the whole dataframe
    # No Data can be considered as a N/A value
    df.replace("No Data", np.nan, inplace=True)

    # set the id column
    df["id"] = df.index + 1
    df.set_index("id", inplace=True)

    return df
