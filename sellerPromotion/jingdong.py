__author__ = 'hongweiye'

import urllib2
url = 'http://developer.51cto.com/art/200908/144391.htm'
response = urllib2.urlopen(url)
html = response.read()
print html
