
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
    cc = ""
    for each in e164ccList:
        if vlrnum.startswith(each) and len(each) > len(cc):
            cc = each 
            
    return cc





dictE164Cc={}

def addE164Cc(cc):
    global dictE164Cc
    
    dict_ = dictE164Cc
    for c in cc[:-1]:
        if c not in dict_.keys():
            dict_[c]={}
            
        dict_=dict_[c]

    if cc[-1] in dict_.keys():
        dict_[cc[-1]]
    else:
        dict_[cc[-1]] = cc
    

def loadplus(filename):
    with open(filename) as f:
        for record in f:
            fields =record.split(',')
            cc = fields[0].strip()
            print cc
            addE164Cc(cc)
            


def e164ccplus(vlrnum):
    
    pass


def genVlrnumList(n):
    import random
    vlrnums=[]
    for _ in range(n):
        vlrnum = ""
        len_ = 3+int(random.random()*10)%10
        for _ in range(len_):
            vlrnum+="%d" %(int(random.random()*10)%10)
        
        vlrnums.append(vlrnum+"\n")
        
    with open("./vlrnumlist%d"%(n), 'w+') as f:
        f.writelines(vlrnums)
        


if __name__ == "__main__":
    begin = time.time()
    load()
    with open("vlrnumList10000",'r') as f:
        for vlrnum in f:
            e164cc(vlrnum)
    
    e164cc("91500") 
    end = time.time()
    delta = (end - begin)
    print "delta: %.06f ms" %(delta*1000) 


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
