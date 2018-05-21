import urllib2
import getpass
from base64 import b64encode
import simplejson as json
import csv

D42_URL = 'https://device42.your.domain'
D42_USERNAME = raw_input("Enter your username: ")
D42_PASSWORD = getpass.getpass("Enter your password: ")
CSV_FILE_NAME = 'subnet_report.csv'

d42_get_devices_url = D42_URL+'/api/1.0/subnets/'
request = urllib2.Request(d42_get_devices_url)
request.add_header('Authorization', 'Basic ' + b64encode(D42_USERNAME + ':' + D42_PASSWORD))

try:
    r = urllib2.urlopen(request)
    obj = r.read()
    subnetdata = json.loads(obj)

    f = csv.writer(open(CSV_FILE_NAME, "wb+"))
    f.writerow(['Name', 'Description', 'Network', 'Mask_Bits', 'Begin_address','End_address'])
    for subnet in subnetdata['subnets']:
        f.writerow([subnet['name'], subnet['description'], subnet['network'], subnet['mask_bits'], subnet['range_begin'], subnet['range_end']])

except Exception, s:
    print str(s)
