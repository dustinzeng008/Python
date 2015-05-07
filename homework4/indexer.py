from time import *
import pickle
import shelve

def secs2str(secs):
    return strftime("%Y-%m-%d %H:%M:%S",localtime(secs))

def process_data(fileName,shelve_file):
    s=shelve.open(shelve_file)
    data_dict={}
    f=open(fileName,"br")
    myList=pickle.load(f)
    for i in range(len(myList)):
        words=myList[i][1].split()
        for word in words:
            if word in data_dict:
                value=myList[i][0]+" | last modified time is: "+secs2str(myList[i][2])+\
                " | Size: "+str(myList[i][3]) + " bytes"
                data_dict[word].add(value)
            else:
                value=myList[i][0]+" | last modified time is: "+secs2str(myList[i][2])+\
                " | Size: "+str(myList[i][3]) + " bytes" 
                data_dict[word]={value}
    s["data_dict"]=data_dict
    s.close()
    return data_dict;

