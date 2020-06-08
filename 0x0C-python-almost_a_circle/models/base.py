#!/usr/bin/python3
""" Module: Base """

import json


class Base:
    """ Base Class """

    _nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base._nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + '.json'
        obs = []
        if list_objs is not None:
            for idx in range(len(list_objs)):
                obs.append(cls.to_dictionary(list_objs[idx]))
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(obs))

    @staticmethod
    def from_json_string(json_string):
        """returns the dictionary representation of a Square"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 2)
        if cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances"""
        filename = cls.__name__ + '.json'
        ins_list = []
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            new_list = cls.from_json_string(content)
            for i in range(len(new_list)):
                ins_list.append(cls.create(**new_list[i]))
        return ins_list
