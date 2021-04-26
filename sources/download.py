from functions import access_folder, get_filepath, read_folder, get_date_str
import os


data = get_date_str()
filepath = get_filepath()
files = read_folder(filepath)


def get_files_sftp(conn):
    if conn.pwd == "/":
        print(conn.listdir())
        if 'folder' in conn.listdir():
            access_folder(conn, 'folder', conn.listdir())
        else:
            folder = input()
            access_folder(conn, folder, conn.listdir())
        print(conn.listdir())
        arq = conn.listdir()
        arq.remove(arq[1])
        for index in [arq[1], arq[2]]:
            access_folder(conn, index, arq)
            if not conn.listdir():
                print("There aren't files in the folder. Contact the developer.")
            else:
                for file in conn.listdir():
                    localpath = filepath + "downloads/"
                    try:
                        conn.get(file, "", callback=None)
                        print("Transfering...{}".format(file))
                        os.rename(file, localpath + data + "/" + file)
                    except:
                        print("Fail to transfer file...{}".format(file))
                print("Download files successfully from {}".format(conn.pwd))
            conn.chdir("..")
            print(conn.pwd)
        conn.chdir("..")
    else:
        conn.chdir("/")
        conn.pwd

