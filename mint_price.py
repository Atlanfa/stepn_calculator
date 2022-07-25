import openpyxl
from ranks import get_rank_name_by_num

path = 'C:/Users/mc_al/OneDrive/Документы/python/pythonProject/table with prices.xlsx'

wb_obj = openpyxl.load_workbook(path)


def get_mint_price(shoe_1, shoe_2, gst):
    if gst < 2:
        shoes = [shoe_1.rank, shoe_2.rank]
        min_rank = shoes[shoes.index(min(shoes))]
        max_rank = shoes[shoes.index(max(shoes))]
        sheet_name = 'gst<2'
        sheet_obj = wb_obj[sheet_name]
        if shoe_1.rank != shoe_2.rank:
            cell_obj = sheet_obj['A10':'G16']
            cell_data = [cell.value for cell in cell_obj[shoe_1.mint_level]][shoe_2.mint_level]
            gst = float(cell_data.split()[0])
            gmt = float(cell_data.split()[-1])
            return gst, gmt
        elif shoe_1.rank and shoe_2.rank == 1:
            cell_obj = sheet_obj['A2':'G8']
            cell_data = [cell.value for cell in cell_obj[shoe_1.mint_level]][shoe_2.mint_level]
            gst = float(cell_data.split()[0])
            gmt = float(cell_data.split()[-1])
            return gst, gmt
        elif shoe_1.rank and shoe_2.rank == 2:
            cell_obj = sheet_obj['A18':'G24']
            cell_data = [cell.value for cell in cell_obj[shoe_1.mint_level]][shoe_2.mint_level]
            gst = float(cell_data.split()[0])
            gmt = float(cell_data.split()[-1])
            return gst, gmt
    elif 2 <= gst < 3:
        shoes = [shoe_1.rank, shoe_2.rank]
        min_rank = shoes[shoes.index(min(shoes))]
        max_rank = shoes[shoes.index(max(shoes))]
        sheet_name = "2<gst<3"
        sheet_obj = wb_obj[sheet_name]
        if shoe_1.rank != shoe_2.rank:
            cell_obj = sheet_obj['A10':'G16']
            cell_data = [cell.value for cell in cell_obj[shoe_1.mint_level]][shoe_2.mint_level]
            gst = float(cell_data.split()[0])
            gmt = float(cell_data.split()[-1])
            return gst, gmt
        elif shoe_1.rank and shoe_2.rank == 1:
            cell_obj = sheet_obj['A2':'G8']
            cell_data = [cell.value for cell in cell_obj[shoe_1.mint_level]][shoe_2.mint_level]
            gst = float(cell_data.split()[0])
            gmt = float(cell_data.split()[-1])
            return gst, gmt
        elif shoe_1.rank and shoe_2.rank == 2:
            cell_obj = sheet_obj['A18':'G24']
            cell_data = [cell.value for cell in cell_obj[shoe_1.mint_level]][shoe_2.mint_level]
            gst = float(cell_data.split()[0])
            gmt = float(cell_data.split()[-1])
            return gst, gmt
    elif 3 <= gst < 4:
        shoes = [shoe_1.rank, shoe_2.rank]
        min_rank = shoes[shoes.index(min(shoes))]
        max_rank = shoes[shoes.index(max(shoes))]
        sheet_name = "3<gst<4"
        sheet_obj = wb_obj[sheet_name]
        if shoe_1.rank != shoe_2.rank:
            cell_obj = sheet_obj['A10':'G16']
            cell_data = [cell.value for cell in cell_obj[shoe_1.mint_level]][shoe_2.mint_level]
            gst = float(cell_data.split()[0])
            gmt = float(cell_data.split()[-1])
            return gst, gmt
        elif shoe_1.rank and shoe_2.rank == 1:
            cell_obj = sheet_obj['A2':'G8']
            cell_data = [cell.value for cell in cell_obj[shoe_1.mint_level]][shoe_2.mint_level]
            gst = float(cell_data.split()[0])
            gmt = float(cell_data.split()[-1])
            return gst, gmt
        elif shoe_1.rank and shoe_2.rank == 2:
            cell_obj = sheet_obj['A18':'G24']
            cell_data = [cell.value for cell in cell_obj[shoe_1.mint_level]][shoe_2.mint_level]
            gst = float(cell_data.split()[0])
            gmt = float(cell_data.split()[-1])
            return gst, gmt

    # if shoe_1.rank != shoe_2.rank:
    #     shoes = [shoe_1.rank, shoe_2.rank]
    #     min_rank = shoes[shoes.index(min(shoes))]
    #     max_rank = shoes[shoes.index(max(shoes))]
    #     sheet_name = f'{get_rank_name_by_num(min_rank)} + {get_rank_name_by_num(max_rank)}'
    #     sheet_obj = wb_obj[sheet_name]
    #     cell_obj = sheet_obj['A1':'G7']
    #     cell_data = [cell.value for cell in cell_obj[shoe_1.mint_level]][shoe_2.mint_level]
    #     gst = float(cell_data.split()[0])
    #     gmt = float(cell_data.split()[-1])
    #     return gst, gmt
    # else:
    #     sheet_name = f'{get_rank_name_by_num(shoe_1.rank)}'
    #     sheet_obj = wb_obj[sheet_name]
    #     cell_obj = sheet_obj['A1':'G7']
    #     cell_data = [cell.value for cell in cell_obj[shoe_1.mint_level]][shoe_2.mint_level]
    #     gst = float(cell_data.split()[0])
    #     gmt = float(cell_data.split()[-1])
    #     return gst, gmt



