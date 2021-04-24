from functions import get_date_str, get_date_iso, write_logs
from download import get_files_sftp
from upload import put_files_sftp
from connection import connect
import warnings
import time

warnings.simplefilter("ignore")

conn = connect()

if conn:
    print("Connected. {}".format(conn))
    while 1:
        data = get_date_str()
        wday = get_date_iso(data)
        hour = time.localtime().tm_hour
        minu = time.localtime().tm_min
        seco = time.localtime().tm_sec
        if wday == 4:
            if hour == 21 and minu == 45:
                put_files_sftp(conn)
                write_logs(data, "Process 'upload to sftp' run successfully.", hour, minu, seco)
            else:
                write_logs(data, "Waiting the process execution or issues occurred during 'upload to sftp.", hour, minu, seco)
        elif wday == 5:
            if hour == 17 and minu == 45:
                get_files_sftp(conn)
                write_logs(data, "Process 'download from sftp' run successfully.", hour, minu, seco)
            else:
                write_logs(data, "Waiting the process execution or issues occurred during 'download from sftp'.", hour, minu, seco)
        time.sleep(60)

conn.close()
