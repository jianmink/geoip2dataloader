
import time
import unittest


e164ccList=[]


def load():
    with open("./result_e164cc2mcc.csv_ready4use",'r') as f:
        for record in f:
            fields = record.split(',')
            e164ccList.append(fields[0].strip())
            
        
    #print e164ccList


def e164cc(vlrnum):
    begin = time.time()
    cc = ""
    for each in e164ccList:
        if vlrnum.startswith(each):
            cc = each 
            break
    
    end = time.time()
    delta = (end - begin)
    print begin
    print end
    print "delta: %.19f us" %delta 
    return cc

class TestE164cc(unittest.TestCase):
    
    def setUp(self):
        load()
    
    def test86139(self):
        cc = e164cc("86139")
        self.assertEqual("86", cc)
         
    def test91500(self):
        cc = e164cc("91500")
        self.assertEqual("91", cc)
        
    def test214139(self):
        cc = e164cc("214139")
        self.assertEqual("", cc)
