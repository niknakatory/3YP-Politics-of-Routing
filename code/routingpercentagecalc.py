from array import *
import csv

fileIN = open("routingpercentagesCSVShort.csv")
data_CSV = csv.reader(fileIN)
list_CSV = list(data_CSV)
#print (list_CSV[48][89])
#print (len(list_CSV))
#line = fileIN.readline()
#i = 0
#instances = 0
#lastline = ""
T = [["Country", "AE", "AU", "BE", "BH", "CA", "CN", "DE", "EG", "ES", "FR", "GB", "GM", "HK", "ID", "IL", "IN", "IQ", "IR", "IT", "JO", "JP", "KP", "KR", "LB", "MX", "NL", "NZ", "RU", "SA", "SG", "SY", "TH", "TR", "US", "VN"]]
#T.append(["Andorra"])
#T[1].append("AE")
#print (T)
#print (T[0][28])
#print (T[1])
#if list_CSV[48][89] == T[0][28]:
#    print ("True")
i = 0
for i in range(len(list_CSV)):
    t = 1
    T.append([list_CSV[i][0]]) #append country name
    for t in range(1,len(T[0])): #for every surveying country...
        j = 1
        found = 0
        for j in range(1,len(list_CSV[i])): #for every possible path
            #print (T[0][t])
            if T[0][t] == list_CSV[i][j]: #if path matches surveying cntry
                T[i+1].append(list_CSV[i][j+1]) #record
                found = 1
        if found == 0: #else put 0 to form a table
            T[i+1].append(0)

f = open('temp.csv','w')
for i in range(len(T)):
    for j in range(len(T[i])):
        f.write(str(T[i][j]))
        f.write(',')
    f.write('\n')
f.close()
print (T)
