#coding=utf-8
from OTXv2 import OTXv2
import IndicatorTypes
import hashlib

API_KEY = '49d4cbdb5501679c2096f6ec9ccb2258ed26f8e553f2d10f802a3e483fd934b1'
OTX_SERVER = 'https://otx.alienvault.com/'
otx = OTXv2(API_KEY, server=OTX_SERVER)

def scanipv4(ipv4):
    res = otx.get_indicator_details_full(IndicatorTypes.IPv4, ipv4)
    print res
    return res

def scanipv6(ipv6):
    res = otx.get_indicator_details_full(IndicatorTypes.IPv6, ipv6)
    print res
    return res

def scandomain(domain):
    res = otx.get_indicator_details_full(IndicatorTypes.DOMAIN, domain)
    print res
    return res

def scanhost(hostname):
    res = otx.get_indicator_details_full(IndicatorTypes.HOSTNAME, hostname)
    print res
    return res

def scanurl(url):
    res = otx.get_indicator_details_full(IndicatorTypes.URI, url)
    print res
    return res

def scanmd5(filepath):
    md5 = hashlib.md5(open(filepath,'rb').read()).hexdigest()
    res = otx.get_indicator_details_full(IndicatorTypes.FILE_HASH_MD5, md5)
    print res
    return res

def scanfile(filepath):
    res = otx.get_indicator_details_full(IndicatorTypes.FILE_PATH, filepath)
    print res
    return res

def searchcve(cve):
    res = otx.get_indicator_details_full(IndicatorTypes.CVE, cve)
    print res
    return res

# scanipv4('162.253.66.75')