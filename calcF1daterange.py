from datetime import date
import calendar
from dateutil import parser
#from sklearn.metrics import f1_score

# sklearn.metrics.f1_score(y_true, y_pred, *, labels=None, 
# pos_label=1, average='binary', sample_weight=None, 
# zero_division='warn')
# Calculate the f-2 for Thursdays... this is not a trick question! We will search for the first 5 d.p. in your CV
# dates|y|yhat

# def dow(date):
#     days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
#     dayNumber=date.weekday()
#     print(days[dayNumber])

fileHandle = open('test.psv', 'r')
for line in fileHandle:
    fields = line.split('|')
    dates = fields[0]
    y = fields[1]
    yhat = fields[2]

    #print(dates)
    #print(dates)
    #print(y)
    #print(yhat)
    
    #for dateline in dates:
    dt_obj = parser.parse(dates)
    #print("The date is", dt_obj)
    dayofweek = dt_obj.weekday()
    print("date is " + dates + ", y is " + y + ", yhat is " + yhat)
    

fileHandle.close()