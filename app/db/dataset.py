import pandas as pd


def clean(dataset_url: str) -> pd.DataFrame:
    """Cleans and transforms the dataset.

    Args:
        dataset_url (str): The link where to get the dataset.

    Returns:
        pd.DataFrame: The dataset presented in a Dataframe format.
    """

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

    # set the id column and start the id values by 1
    df["id"] = df.index + 1
    df.set_index("id", inplace=True)

    # delete rows where missing values are "s" and "No Data"
    for column in df:
        df.drop(df.loc[df[column] == "No Data"].index, inplace=True)
        df.drop(df.loc[df[column] == "s"].index, inplace=True)

    df = set_data_types(df)
    
    return df


def set_data_types(df: pd.DataFrame) -> pd.DataFrame:
    """Set appropriate data types to columns in the dataframe.

    Args:
        df (pd.DataFrame): The dataframe to be modified.

    Returns:
        pd.DataFrame: The dataframe updated with types.
    """

    cols_int = [
        "grade_k",
        "grade_1",
        "grade_2",
        "grade_3",
        "grade_4",
        "grade_5",
        "grade_6",
        "grade_7",
        "grade_8",
        "total_enrollment",
        "total_female",
        "total_male",
    ]
    cols_float = ["ratio_female", "ratio_male"]
    cols_string = ["school_name", "category"]

    df[cols_int] = df[cols_int].astype(int)
    df[cols_float] = df[cols_float].astype(float)
    df[cols_string] = df[cols_string].astype(str)

    return df
