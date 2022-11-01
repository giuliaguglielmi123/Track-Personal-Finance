

######..... convert decimal values and keep them float
def decimal_converter(value):
    """AI is creating summary for decimal_converter

    Args:
        value ([type]): [description]

    Returns:
        [type]: [description]
    """
    try:
        return float(value.replace(',', '.'))
    except ValueError:
        return value


def clean_df(df):
    """Clean dataframe - lowercase - replace spaces

    Args:
        df: raw data bank account

    Returns:
        df: raw data bank account processed
    """
    # Columns
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.replace(' ', '')
     
    # Entire df
    df = df.applymap(lambda x: x.lower() if type(x) == str else x)

    return df
    

