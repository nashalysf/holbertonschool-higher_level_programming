#!/usr/bin/python3
"""Module with class Base"""
import json


class Base:
    """Base super class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON representation of a list of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string to file"""
        if list_objs is None or len(list_objs) == 0:
            list_objs = []

        tmp_list = []
        filename = cls.__name__ + '.json'

        with open(filename, 'w') as file:
            """iterate over list"""
            for i in list_objs:
                tmp_list.append(i.to_dictionary())
            """write on file"""
            data = Base.to_json_string(tmp_list)
            file.write(data)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with attributes

        Create: dummy instance
        """
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ == "Square":
            obj = cls(1)

        obj.update(**dictionary)
        return (obj)
