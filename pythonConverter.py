#%% imports
import pdf2docx

#%% Check available methods
dir(pdf2docx)

#%% Import the pdf2docx converter
from pdf2docx import Converter
help(Converter)

#%% Convert the pages
pdf_file = 'data\In\sample.pdf'
word_file = 'data\Out\sample.docx'

cv = Converter(pdf_file)
cv.convert(word_file)

cv.close()