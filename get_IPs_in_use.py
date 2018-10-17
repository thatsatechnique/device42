import urllib2
import getpass
from base64 import b64encode
import simplejson as json
import csv

D42_URL = 'https://device42.your.domain'
D42_USERNAME = raw_input("Enter your username: ")
D42_PASSWORD = getpass.getpass("Enter your password: ")
CSV_FILE_NAME = 'Available_IP_report.csv'

d42_get_devices_url = D42_URL+'/api/1.0/ips?available=no'
request = urllib2.Request(d42_get_devices_url)
request.add_header('Authorization', 'Basic ' + b64encode(D42_USERNAME + ':' + D42_PASSWORD))

try:
    r = urllib2.urlopen(request)
    obj = r.read()
    data = json.loads(obj)

    f = csv.writer(open(CSV_FILE_NAME, "wb+"))
    f.writerow(['IP Address','Hostname', 'Subnet Name'])
    for ip in data['ips']:
        if "::" not in ip['subnet']: //exclude IPv6 addresses
                f.writerow([ip['ip'], ip['device'], ip['subnet']])

except Exception, s:
    print str(s)
