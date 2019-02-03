import geoip2.database
import csv
Countries = {"AE":0,
            "AM":0,
            "AO":0,
            "AR":0,
            "AU":0,
            "AZ":0,
            "BD":0,
            "BH":0,
            "BR":0,
            "BY":0,
            "CA":0,
            "CN":0,
            "CO":0,
            "CU":0,
            "DE":0,
            "EC":0,
            "EE":0,
            "EG":0,
            "ET":0,
            "FR":0,
            "GB":0,
            "GE":0,
            "GM":0,
            "HU":0,
            "ID":0,
            "IN":0,
            "IR":0,
            "IS":0,
            "IT":0,
            "JO":0,
            "JP":0,
            "KE":0,
            "KG":0,
            "KH":0,
            "KR":0,
            "KZ":0,
            "LB":0,
            "LK":0,
            "LY":0,
            "MA":0,
            "MM":0,
            "MW":0,
            "MX":0,
            "MY":0,
            "NG":0,
            "PH":0,
            "PK":0,
            "RU":0,
            "RW":0,
            "SA":0,
            "SD":0,
            "SG":0,
            "SY":0,
            "TH":0,
            "TN":0,
            "TR":0,
            "UA":0,
            "UG":0,
            "US":0,
            "UZ":0,
            "VE":0,
            "VN":0,
            "ZA":0,
            "ZM":0,
            "ZW":0}

reader = geoip2.database.Reader('GeoLite2-Country.mmdb')
#response = reader.country('110.14.105.177')
#Countries[response.country.iso_code] += 1
print (Countries)


#fileIN = open("dbip-country-lite-2019-02.csv", "r")

with open('miraihits.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    first = False
    for row in readCSV:
        if first != False:
            #print(row)
            try:
                response = reader.country(row[0])
                Countries[response.country.iso_code] += 1
                
                #print (response.country.iso_code)
            except:
                pass
                #print(readCSV.line_num)
        first = True

print (Countries)
