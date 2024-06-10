import pytest
import pandas as pd

@pytest.fixture
def get_excel_data():
    df = pd.read_excel("..//ExcelData//test_data.xlsx")
    data = df.to_dict(orient='records')
    return data





















'''def get_data(sheetName):
    workbook = openpyxl.load_workbook("..//ExcelData//test_data.xlsx")
    sheet = workbook[sheetName]
    totalrows = sheet.max_row
    totalcols = sheet.max_column
    print("total cols are ",str(totalcols))
    print("total rows are ", str(totalrows))
    mainList = []

    for i in range(2,totalrows+1):
        dataList = []
        for j in range(1, totalcols+1):
            data = sheet.cell(row=i,column=j).value
            dataList.insert(j,data)
        mainList.insert(i,dataList)
        print(mainList)
    return mainList'''