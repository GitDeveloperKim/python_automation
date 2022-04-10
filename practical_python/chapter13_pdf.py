import PyPDF2

pdfFileObj = open('data/meetingminutes.pdf', 'rb') # 이진 데이터 읽기
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)  #페이지 객체 만들기
print(pageObj.extractText())    # 페이지 객체에서 텍스트 추출

# encrypted pdf
pdfReader = PyPDF2.PdfFileReader(open('data/encrypted.pdf', 'rb'))
if pdfReader.isEncrypted:
    pdfReader.decrypt('rosebud')
    pageObj = pdfReader.getPage(0)
    print(pageObj.extractText())

#combined pdf
pdfFile = open('data/meetingminutes.pdf', 'rb')
pdfFile2 = open('data/meetingminutes2.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfReader2 = PyPDF2.PdfFileReader(pdfFile2)

pdfWriter = PyPDF2.PdfFileWriter()

pageObj = pdfReader.getPage(0)
pdfWriter.addPage(pageObj)
pageObj = pdfReader2.getPage(1)
pdfWriter.addPage(pageObj)

pdfOutputFile = open('data/combineminutes.pdf', 'wb') # 파일 이진 쓰기모드로 열고
pdfWriter.write(pdfOutputFile) # pdfWriter 를 통해 파일 경로에 쓰기
# 중간 페이지 삽입이 안된다
# addPage() 메소드는 마지막 페이지만 추가한다
pdfOutputFile.close()
pdfFile.close()
pdfFile2.close()

#overwrite
minutesFile = open('data/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader.getPage(0)

pdfWatermarkReader = PyPDF2.PdfFileReader(open('data/watermark.pdf', 'rb'))
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

resultPdfFile = open('data/watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()