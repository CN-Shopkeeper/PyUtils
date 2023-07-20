from PyPDF2 import PdfReader, PdfWriter

import os

data_path = os.path.join(os.path.dirname(__file__),"../data")
# 要切割的文件名称
file = "Spatial Regression with Raster Data.pdf"
# file = "regression steps.pdf"
# file = "Geographically Weighted Regression_2023.pdf"
filename, file_extension = os.path.splitext(file)
in_file = os.path.join(data_path,"raw",file)
out_file = os.path.join(data_path,"splitted",filename+"_split"+file_extension)

# 要切割的页码，你最好别加空格，下标从1开始，切割的范围是[start-1, end]
page_out_in = "1-6,18"
# regression steps.pdf
# page_out_in = "1-6,8-12,14-15,17,19,21-31"
# Bayesian spatial and spatiotemporal modeling_2023.pdf
# page_out_in = "1-17,19-22,24-26,28-34,36-42,44,45,47-55"
# "Geographically Weighted Regression_2023.pdf"
# page_out_in = "1-8,11-13,15,16,18-21,26,34,36,41,42,44,46,51,54,55,58-61,63,68-71,73-77"

reader = PdfReader(in_file)
writer = PdfWriter()

pages = len(reader.pages)

page_out_in = page_out_in.replace('，', ',')
page_split = page_out_in.split(',')

for page in page_split:
    page_range = page.split('-')
    page_range_l = len(page_range)
    # 如果输入的是一个范围，获取获取开始页和结束页。例如，1-18,18-39,2-15
    # 起始页大于结束页时，不能正确分割
    if page_range_l > 1:
        start_page = int(page_range[0])
        end_page = int(page_range[1])
        if start_page <= end_page <= pages:
            for i in range(start_page - 1, end_page):
                writer.add_page(reader.pages[i])
        else:
            print("错误:",f'{start_page}-{end_page}')

    # 输入的是某个数值，单独提取一页。例如1,3,12,5,53
    # 输入数值大于待分割文件总页数时，不能正常分割
    elif page_range_l == 1:
        if int(page_range[0]) <= pages:
            writer.add_page(reader.pages[int(page_range[0])-1])
        else:
            print("错误:",f'{page_range[0]}')

with open(out_file, "wb") as fh:
    writer.write(fh)