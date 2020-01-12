#PDF Converter
import PyPDF4
PDFfile=open("83.pdf","rb")
pdfread=PyPDF4.PdfFileReader(PDFfile)

i=0
while i<pdfread.getNumPages():
    pageinfo = pdfread.getPage(i)
    text = (pageinfo.extractText())
    fh = open("83.txt", "a")
    fh.write(text)
    fh.close()
    with open("83.txt", "r") as myfile:
        myfile.read().replace("\n", " ")
    i=i+1
