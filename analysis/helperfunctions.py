import pandas as pd




def extract_columns(name: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Extracts the columns from the dataframe
    :param name: name of the dataframe
    :param columns: The columns to extract
    :return: The dataframe with only the columns specified
    """
    column_mapping = {'czname': 'city', 'par_median': 'parent_median', 'k_median': 'student_median', 'par_q1': 'bottom20%_fraction', 'par_top1pc': 'top1%_fraction', 'kq5_cond_parq1':'bot20_to_top20','ktop1pc_cond_parq1':'bottom20_to_top1','mr_kq5_pq1':'mrate_top20','mr_ktop1_pq1':'mrate_top1'}

    df = pd.read_csv('datasets/' + name + '.csv')
    df = df.rename(columns=column_mapping)
    df = df[columns]

    # Identify numeric columns
    numeric_cols = df.select_dtypes(include='number').columns

    # Round numeric columns to 0 decimal places and convert to integers
    df[numeric_cols] = df[numeric_cols].round(0).astype(int)
    
    return df

