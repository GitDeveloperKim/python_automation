import PyPDF2

# 실습 1 페이지, 텍스트 얻기
pdfFileObj = open('data/meetingminutes.pdf', 'rb')  # 이진 데이터로 파일 읽기
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  # PDF 파일리더 객체 반환
print(pdfReader.numPages)  # 페이지 갯수 출력
pageObj = pdfReader.getPage(0)  # 페이지 객체 만들기
print(pageObj.extractText())  # PDF 파일에서 텍스트 추출

# 실습 2 encrypted pdf
pdfReader = PyPDF2.PdfFileReader(open('data/encrypted.pdf', 'rb'))
if pdfReader.isEncrypted:
    pdfReader.decrypt('rosebud')
    pageObj = pdfReader.getPage(0)
    print(pageObj.extractText())

# 실습 3 combined pdf (덧붙이기)
pdfFile = open('data/meetingminutes.pdf', 'rb')
pdfFile2 = open('data/meetingminutes2.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfReader2 = PyPDF2.PdfFileReader(pdfFile2)

pdfWriter = PyPDF2.PdfFileWriter()  # PDF file writer 객체 얻기

pageObj = pdfReader.getPage(0)
pdfWriter.addPage(pageObj)
pageObj = pdfReader2.getPage(1)
pdfWriter.addPage(pageObj)

pdfOutputFile = open('data/combineminutes.pdf', 'wb')  # 파일 이진 쓰기모드로 열고
pdfWriter.write(pdfOutputFile)  # pdfWriter를 통해 파일 경로에 쓰기
# 중간 페이지 삽입이 안된다
# addPage() 메소드는 마지막 페이지만 추가가능
pdfOutputFile.close()
pdfFile.close()
pdfFile2.close()

#실습 예제 : overwrite (워터마크)
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

# 기타
# PDF 암호풀기
# 페이지 회전
# 그림추가
