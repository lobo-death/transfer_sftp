from datetime import datetime as dt, date
import os


def get_filepath():
    filepath = 'path'
    return filepath


def read_folder(filepath):
    files = []
    for i in range(0, 500, 1):
        if 'name_' + str(i) + '.csv' in os.listdir(filepath):
            files.append('name_' + str(i) + '.csv')
    return files


def access_folder(conn, name, listname):
    if name in listname:
        return conn.chdir(name)
    else:
        return print('Folder not found.')


def get_date_str():
    data = str(dt.now())[0:10:1]
    return data


def get_date_iso(data):
    wday = dt.weekday(date.fromisoformat(data))
    return wday


def write_logs(data, message, hour, minu, seco):
    os.system("cat " + data + ";" + message + " at " + str(hour) + ":" + str(minu) + ":" + str(seco) + " >> ../logs/" +
              data + "_log.txt")
