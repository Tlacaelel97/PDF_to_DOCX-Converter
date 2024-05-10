from pdf2docx import Converter
from pathlib import Path

dir_in = Path('data\In')
work_file = Path(input())
fname, ext = work_file.split('.')
pdf_file = dir_in / work_file

dir_out = Path('data\Out')
file_out = Path(fname+'.docx')
word_file = dir_out / file_out
