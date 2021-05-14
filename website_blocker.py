import time
from datetime import datetime as dt

blocked_sites = ['www.facebook.com', 'facebook.com']

windows_host = r"C:\Windows\System32\drivers\etc\hosts"
default_host = windows_host
redirect = "127.0.0.1" #IP adress to redirect to




def block_websites(start_hour, start_minute, end_hour, end_minute):
    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day, start_hour, start_minute) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end_hour, end_minute):
            print("You shouldn't visit this website at this time")
            with open(default_host, 'r+') as hostfile:
                hosts = hostfile.read()
                for site in blocked_sites:
                    if site not in hosts:
                        hostfile.write(redirect + ' ' + site + '\n')
        else:
            with open(default_host, 'r+') as hostfile:
                hosts = hostfile.readlines()
                hostfile.seek(0)
                for host in hosts:
                    if not any(site in host for site in blocked_sites):
                        hostfile.write(host)
                hostfile.truncate()
            print("Have fun!")
        time.sleep(3)


if __name__ == '__main__':
    block_websites(18, 33, 18, 34)


