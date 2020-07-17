import os, re

class WifiPassword(object):
    def __init__(self):
        self.wifi_path = "/etc/NetworkManager/system-connections/"

    def walk_dir(self):
        itrDirs = os.listdir(self.wifi_path)
        itrDirs = [self.wifi_path+i for i in itrDirs if i ]
        return itrDirs

    def read_file(self, itrDirs):
        wifi_data = []
        for file_path in itrDirs:
            reader = open(file_path, 'r').read()
            keys = []
            values = []
            for line in reader.split('\n'):
                if '=' in line:
                    info = line.split('=')
                    keys.append(info[0])
                    values.append(info[1])
            record = dict(zip(keys,values))
            if record:
                wifi_data.append(record)
        return wifi_data

    def main(self):
        list_d = self.walk_dir()
        wifi_info = self.read_file(list_d)
        CGREEN  = '\33[32m'
        print( CGREEN + '--------------------------------------')
        for wifi in wifi_info:
            print(CGREEN + "[WIFI] {} [PASSWORD] {} ".format(wifi.get("ssid","N/A"),wifi.get('psk','N/A')))
        print('--------------------------------------')

obj = WifiPassword()
obj.main()
