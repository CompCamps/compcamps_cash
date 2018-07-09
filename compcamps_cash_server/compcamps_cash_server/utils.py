import datetime

def utcToRegina(dt):
    return dt - datetime.timedelta(seconds = 21600)