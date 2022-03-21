def difference(data_set):
    difference = list()
    columns = get_df_columns(data_set)
    for i in range(1, len(data_set)):
        difference.append(data_set[columns[0]][i] -data_set[columns[0]][i - 1] )
    df_difference = pd.DataFrame(difference)
    df_difference.columns = ["Difference"]
    return df_difference
