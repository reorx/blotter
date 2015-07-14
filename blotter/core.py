#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import urlparse


def parse_url(url):
    """
    url like: `http://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,600,700`
    """
    query = urlparse.parse_qs(urlparse.urlparse(url).query)
    print query


def blot_font(url):
    resp = requests.get(url)
    css = resp.content


if __name__ == '__main__':
    parse_url('http://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,600,700')
