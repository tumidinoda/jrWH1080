from datetime import datetime, timedelta

from pywws import DataStore
from pywws import Localisation
from pywws.TimeZone import Local, utc
from pywws import ZambrettiCore

print ("Hello World")
data_dir = '/home/robert/jrWH1080/data'
params = DataStore.params(data_dir)
Localisation.SetApplicationLanguage(params)
hourly_data = DataStore.hourly_store(data_dir)
idx = hourly_data.before(datetime.max)
print 'Zambretti (current):', Zambretti(params, hourly_data[idx])
idx = idx.replace(tzinfo=utc).astimezone(Local)
if idx.hour < 8 or (idx.hour == 8 and idx.minute < 30):
    idx -= timedelta(hours=24)
idx = idx.replace(hour=9, minute=0, second=0)
idx = hourly_data.nearest(idx.astimezone(utc).replace(tzinfo=None))
lcl = idx.replace(tzinfo=utc).astimezone(Local)
print 'Zambretti (at %s):' % lcl.strftime('%H:%M %Z'),\
       Zambretti(params, hourly_data[idx])















Zambretti(params, hourly_data[idx])