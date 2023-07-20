from PyPDF2 import PdfMerger

import os

data_path = os.path.join(os.path.dirname(__file__),"../data")
splitted_path = os.path.join(data_path,"splitted")
merged_path = os.path.join(data_path,"merged")

x = list(map(lambda a: os.path.join(splitted_path,a),[a for a in os.listdir(splitted_path) if a.endswith(".pdf")])) 

merger = PdfMerger()

for pdf in x:
    merger.append(open(pdf, 'rb'))

with open(os.path.join(merged_path,"result.pdf"), "wb") as fout:
    merger.write(fout)