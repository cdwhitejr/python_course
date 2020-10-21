#ex10.py

'''
- Create a list of 5 FTP sites that allow anonymous login
- Create a thread and a queue in order to connect to each site,
    list the content and exit;
- Create 10 threads.
'''


import socket, os, queue
from threading import Thread
from ftplib import FTP
ftplist = [
    'cmp.felk.cvut.cz',
    'audio.serebniti.ru',
    'ports.jp.freebsd.org',
    'ftp.eggheads.org',
    'ftp.analog.com',
    'ftp.morishima.net',
    'ftp.flightsim.com',
    'ftp.ftpx.com',
    'ftp.netlabs.org',
    'ftp.novell.nl'
]



def ftp_worker(ftp_address):
    ftpclient = FTP(ftp_address)
    host = ftp_address
    port = 21
    print(f'Connecting to {host}:{port}')

    #get connection
    ftpclient.login()

    #insert code to extract directory listing below
    #site_content = ftpclient.recv(1024).decode()

    #write listing to file locally
    ftpclient.dir()
    '''
    with open(ftp_address+'.txt','w') as f:
        f.writelines(content)
    '''

q = queue.Queue()
for host  in ftplist:
    q.put(host)

   

# create the threads to go forth and conquer 
def thread_it_all(howmanyT=len(ftplist)):
    for fc in range(howmanyT):

        t = Thread(target=ftp_worker,args=(ftplist[fc]))
        print('Worker',str(fc),'created. Working on',)
        t.start()



class FTP_worker(Thread):
    def __init__(self,socket):
        pass
    
    def output(self):
        pass


def play():
    import socket


    #provides IP add
    print(socket.gethostbyname('google.com'))



    #provides dns name of ip address
    print(socket.gethostbyaddr('8.8.8.8'))


