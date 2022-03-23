def get_dataset_columns(df):
    columns = list()
    for col in df.columns:
        columns.append(col)
    return columns

def df_elements_to_list(df):
    columns = get_dataset_columns(df)
    predicted = list()
    expected = list()
    for i in range(len(df)):
        predicted.append(df[columns[0]][i])
        expected.append(df[columns[1]][i])
    return expected, predicted
