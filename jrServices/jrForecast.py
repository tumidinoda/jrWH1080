from datetime import datetime, timedelta

from pywws import DataStore
from pywws import Localisation
from pywws import ZambrettiCore
from pywws.TimeZone import Local, utc


def ZambrettiCode(params, hourly_data):
    north = eval(params.get('Zambretti', 'north', 'True'))
    baro_upper = eval(params.get('Zambretti', 'baro upper', '1050.0'))
    baro_lower = eval(params.get('Zambretti', 'baro lower', '950.0'))
    if not hourly_data['rel_pressure']:
        return ''
    if hourly_data['wind_ave'] is None or hourly_data['wind_ave'] < 0.3:
        wind = None
    else:
        wind = hourly_data['wind_dir']
    if hourly_data['pressure_trend'] is None:
        trend = 0.0
    else:
        trend = hourly_data['pressure_trend'] / 3.0
    return ZambrettiCore.ZambrettiCode(
        hourly_data['rel_pressure'], hourly_data['idx'].month, wind, trend,
        north=north, baro_top=baro_upper, baro_bottom=baro_lower)


# ----------------------------------------------------------------------------------------------------------------------
def Zambretti(params, hourly_data):
    code = ZambrettiCode(params, hourly_data)
    return Localisation.translation.ugettext(ZambrettiCore.ZambrettiText(code))


# ----------------------------------------------------------------------------------------------------------------------
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
print 'Zambretti (at %s):' % lcl.strftime('%H:%M %Z'), \
    Zambretti(params, hourly_data[idx])

Zambretti(params, hourly_data[idx])
