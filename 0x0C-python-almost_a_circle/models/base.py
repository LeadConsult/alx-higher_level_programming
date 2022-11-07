#!/usr/bin/python3
"""A base model class is defined."""
import json
import csv
import turtle


class Base:
    """Represent the fundamental model.
    The "base" class for all other classes in project 0x0C.*.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """
    
    
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.
        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects



    @staticmethod
    def to_json_string(list_dictionaries):
        """The JSON serialization of a list of dicts is returned..
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)


    @classmethod
    def save_to_file(cls, list_objs):
        """Create a file with the JSON serialization of a collection of objects.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))


    @staticmethod
    def from_json_string(json_string):
        """Get a JSON string's deserialization back.
        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            An empty list if json string is None or empty.
            If not, the Python list represented by json string will be used..
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)


    @classmethod
    def create(cls, **dictionary):
        """Bring back a class created using a dictionary of attributes.
        Args:
            **dictionary (dict): Initialize attribute key/value pairs.
        """
        
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new


    @classmethod
    def load_from_file(cls):
        """Give back a list of classes that were created from a JSON string file.
        Reads from `<cls.__name__>.json`.
        Returns:
            If the file is missing, the list will be empty.
            If not, a list of classes that have been instantiated.
        """
        
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Create a file and serialize a list of objects in CSV format.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())


    @classmethod
    def load_from_file_csv(cls):
        """Give back a list of classes that were created using a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file is missing, the list will be empty.
            If not, a list of classes that have been instantiated.
        """
        
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []


    @staticmethod
    def draw(list_rectangles, list_squares):
        """The turtle module can be used to draw squares and rectangles.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
