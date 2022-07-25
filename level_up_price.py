import openpyxl

path = 'C:/Users/mc_al/OneDrive/Документы/python/pythonProject/level up price.xlsx'

wb_obj = openpyxl.load_workbook(path)


def get_level_up_price(current_level, level_you_want):
    sheet_name = 'level_up'
    sheet_obj = wb_obj[sheet_name]
    cell_obj = sheet_obj['B2':'G31']
    cell_data = []
    for i in range(level_you_want-current_level):
        cell_data.append([cell.value for cell in cell_obj[i]])
    # print(cell_data)
    gst = 0
    gmt = 0
    time = 0
    for row in cell_data:
        gst += int(row[0][:-3])
        try:
            gmt += int(row[1][:-3])
        except:
            gmt += int(row[1])
        time += int(row[4])
    # print(f'{gst} - GST, {gmt} - GMT, {time} - Time')
    return gst, gmt, time



get_level_up_price(0,5)
