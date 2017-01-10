#!/usr/bin/env python
#! -*- encoding=utf-8

import urllib
from urllib.parse import urlparse
'''
File: url.py
Author: Xu Xinran <xxr3376@gmail.com>
Description: Some util functions for processing url
'''

def encode_query_dict(d):
    result = {}
    for k, v in d.iteritems():
        if isinstance(v, unicode):
            v = v.encode('utf-8')
        if isinstance(v, list):
            v = map(lambda x: x.encode('utf-8') if isinstance(x, unicode) else x, v)
        result[k] = v
    return result

def change_get_args(url, func):
    """
    func: a callback receives old query dictionary,\
            return new query dictionary
    """
    url_parts = list(urlparse.urlparse(url))
    query = urlparse.parse_qs(url_parts[4])
    query = func(query)
    query = encode_query_dict(query)
    url_parts[4] = urllib.urlencode(query, doseq=True)
    return urlparse.urlunparse(url_parts)
