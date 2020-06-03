#!/usr/bin/python3
""" Module: 9-add_item """


import sys


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    filename = 'add_item.json'
    content_list = load_from_json_file(filename) + sys.argv[1:]
except:
    content_list = sys.argv[1:]

save_to_json_file(content_list, filename)
