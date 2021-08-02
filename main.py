import subprocess
import os

subprocess.call('git clone https://github.com/nikdubois/vsftpd-2.3.4-infected.git', shell = True)
os.system('sudo apt-get install build-essential')
os.system('cd vsftpd-2.3.4-infected')
# os.system('$y')


os.system('cd -f makefile2  ~/vsftpd-2.3.4-infected/Makefile')
#os.system('make')


#os.system('useradd nobody')
os.system('sudo mkdir /usr/share/empty')
os.system(' cd vsftpd-2.3.4-infected/')
os.system('sudo cp vsftpd /usr/local/sbin/vsftpd')
os.system('sudo cp vsftpd.8 /usr/local/man/man8')

~                                                                                                 ~                                
