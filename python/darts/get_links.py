#!/bin/python

from util import subprocess_grab

SEARCH = "https://www.google.co.uk/search?q="
#SEARCH = "https://www.bing.com/search?q="

def get_links_lynx(search_terms):
    search = SEARCH + search_terms
    got = subprocess_grab(["lynx", "-listonly", "-dump", search])
    return got

get_links = get_links_lynx
