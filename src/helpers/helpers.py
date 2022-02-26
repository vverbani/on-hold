# Copy final `csv` file into `xlsx` as it's easier to look at and for users to edit later on
def copy_to_excel(input_file, output_file):
    # Reading the csv file
    df_new = pd.read_csv(WRITE_CSV_FILE)

    # saving xlsx file
    GFG = pd.ExcelWriter(WRITE_XLSX_FILE)
    df_new.to_excel(GFG, index = False)

    GFG.save()
    return output_file