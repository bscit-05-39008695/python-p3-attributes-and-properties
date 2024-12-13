#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="", breed=""):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name == "":
            print("Name must be string between 1 and 25 characters.")
        elif type(name) != str:
            print("Name must be string between 1 and 25 characters.")
        elif len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = name
            
            
        
