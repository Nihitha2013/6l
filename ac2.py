import random
import time
def getRDate(sd,ed):
    print("Printing date between ",sd,"and",ed)
    r=random.random()
    dateformat='%m/%d/%Y'
    st=time.mktime(time.strptime(sd,dateformat))
    et=time.mktime(time.strptime(ed,dateformat))
    rt=st+r*(et-st)
    rd=time.strftime(dateformat,time.localtime(rt))
    return rd

print("Random date:",getRDate("03/01/2025","05/01/2025"))





