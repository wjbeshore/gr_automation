import csv

def readcsv(filename):	
    ifile = open(filename, "rU")
    reader = csv.reader(ifile, delimiter=";")

    rownum = 0	
    a = []

    for row in reader:
        a.append (row[0].replace(", ", ""))
        rownum += 1
    
    ifile.close()
    return a

newArray = readcsv("DonorNumbers.csv")
print(newArray)