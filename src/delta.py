
import unittest
import time

"""
this file help to compute the delta between two geoip2 data. 

"""

dict_geoip={}

 
def loadGeoIPData(filename):

    begin = time.time()
    dict_={}
    with open(filename, 'r') as f:
        for each in f:
            fields = each.split(',')
            dict_[fields[0][1:-1]+"-"+fields[1][1:-1]]=fields[4][1:-1]
            
    end = time.time()
    delta = (end - begin)*1000
    print "loadGeoIP2Data: %.0f ms" %delta    
    return dict_
             

def delta(file1,file2):
    begin = time.time()
    dict_1 = loadGeoIPData(file1)
    dict_2 = {}
#     dict_3 = loadGeoIP2Data(file2)
    
    with open(file2,'r') as f:
        for each in f:
            fields = each.split(',')
            key = fields[0][1:-1]+"-"+fields[1][1:-1]
            v   = fields[4][1:-1]
            
            if dict_1.has_key(key):
                if dict_1[key] == v:
                    dict_1.pop(key)
                else:
                    dict_2[key]=v
            else:
                dict_2[key]=v
                
    end = time.time()
    delta = (end - begin)*1000
    print "delta: %.0f ms" %delta 
        
    return dict_1, dict_2
                

class TestGeoIPLoader(unittest.TestCase):
    @unittest.skip("..")
    def testLoadGeoIPFile(self):
        dict_= loadGeoIPData("./GeoIPCountry.csv")
#         print dict_
        self.assertEqual(dict_["1.0.1.0-1.0.3.255"],'CN')
        
    def testDelta(self):
        dict_1,dict_2 = delta("./GeoIPCountry.csv", "GeoIPCountryNew.csv")
        
        print dict_1
        print dict_2
    
if  __name__ == "__main__":
    dict_1,dict_2 = delta("./GeoIPCountry.csv", "GeoIPCountryNew.csv")
        
    print len(dict_1), len(dict_2)
    print "remove: ",dict_1
    print "add:    ",dict_2
    
