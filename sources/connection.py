import pysftp as sftp


def connect():
    hostname = 'hostname'
    username = 'username'
    password = 'password'
    cnopts = sftp.CnOpts()
    cnopts.hostkeys = None
    conn = sftp.Connection(hostname, username=username, password=password, cnopts=cnopts)
    return conn
