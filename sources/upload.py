from functions import access_folder, get_filepath, read_folder, get_date_str
import os


data = get_date_str()
filepath = get_filepath()
files = read_folder(filepath)


def put_files_sftp(conn):
    if conn.pwd == "/":
        print(conn.listdir())
        if "folder" in conn.listdir():
            access_folder(conn, "folder", conn.listdir())
        else:
            folder = input()
            access_folder(conn, folder, conn.listdir())
        print(conn.listdir())
        arq = conn.listdir()
        arq.remove(arq[1])
        if arq[0]:
            access_folder(conn, arq[0], arq)
            if conn.listdir():
                print("There are files of last week in the folder. Them weren't processed yet. Contact the developer.")
            else:
                for file in files:
                    localpath = filepath + "uploads/"
                    try:
                        conn.put(localpath, '', callback=None, confirm=True)
                        print("Transfering...{}".format(file))
                        os.rename(filepath + file, localpath + data + "/" + file)
                    except:
                        print("Fail to transfer file...{}".format(file))
                print("Upload files successfully to {}".format(conn.pwd))
        conn.chdir("..")
    else:
        conn.chdir("/")
        conn.pwd

