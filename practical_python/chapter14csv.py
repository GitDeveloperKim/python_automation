import csv

# read
exampleFile = open('data/example.csv')
exampleReader = csv.reader(exampleFile) # read(), readline() 대신 csv.reader 사용
exampleData = list(exampleReader) # reader 객체에 list로 얻음
print(exampleData[0][0])
print(exampleData[0][1])
print(exampleData[0][2])
print(exampleData[6][1])

# write
outputFile = open('data/output.csv','w',newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam','egg','bacon','ham'])
outputWriter.writerow(['hello world!', 'eggs', 'bacon','ham'])
outputWriter.writerow([1, 2, 3.141592, 4])
outputFile.close()
