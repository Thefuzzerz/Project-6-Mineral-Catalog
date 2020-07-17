"""Models file for minerals application."""

import json
from django.db import models


JDATA = open('minerals/minerals.json')
JSON_DATA = json.load(JDATA)

class Mineral(models.Model):
    """Mineral model for minerals application."""
    category = models.CharField(max_length=(255))
    cleavage = models.CharField(max_length=(255))
    color = models.CharField(max_length=(255))
    crystal_habit = models.CharField(max_length=(255))
    crystal_symmetry = models.CharField(max_length=(255))
    crystal_system = models.CharField(max_length=(255))
    diaphaneity = models.CharField(max_length=(255))
    formula = models.CharField(max_length=(255))
    group = models.CharField(max_length=(255))
    image_caption = models.CharField(max_length=(255))
    image_filename = models.CharField(max_length=(255))
    luster = models.CharField(max_length=(255))
    mohs_scale_hardness = models.CharField(max_length=(255))
    name = models.CharField(max_length=(255))
    optical_properties = models.CharField(max_length=(255))
    refractive_index = models.CharField(max_length=(255))
    specific_gravity = models.CharField(max_length=(255))
    streak = models.CharField(max_length=(255))
    strunz_classification = models.CharField(max_length=(255))
    unit_cell = models.CharField(max_length=(255))

    def __str__(self):
        return self.name

def initialize(json_data=JSON_DATA):
    '''Function imported in shell to create database from json.'''
    def create_entries(json_data):
        '''Iterates through entries and sets attributes based on keys.'''
        entry_keys = []
        for mineral in json_data:
            mineral_keys = mineral.keys()
            for key in mineral_keys:
                if key in entry_keys:
                    pass
                else:
                    entry_keys.append(key)
        entry_keys.sort()
        for mineral_entry in json_data:
            mineral_name = mineral_entry.get("name")
            exists = Mineral.objects.filter(name=mineral_name).count() # pylint: disable=E1101
            if exists == 1:
                pass
            else:
                mineral = Mineral()
                for attribute in entry_keys:
                    try:
                        data = mineral_entry[attribute]
                        setattr(mineral, attribute, data)
                    except KeyError:
                        setattr(mineral, attribute, "")
                mineral.save()
    create_entries(json_data)

def common_attributes():
    """Function to query database and return the number of times each
    attribute appears determining most common occurances."""
    attributes = ("category", "cleavage", "color", "crystal_habit",
                  "crystal_symmetry", "crystal_system", "diaphaneity",
                  "formula", "group", "luster", "mohs_scale_hardness",
                  "optical_properties", "refractive_index",
                  "specific_gravity", "streak",
                  "strunz_classification", "unit_cell",
                  )
    occurance_count = []
    for attribute in attributes:
        filter_str = attribute + "__iexact"
        search_string = ""
        count = Mineral.objects.exclude(**{filter_str: search_string}).count() # pylint: disable=E1101
        occurance_count.append((attribute, count))
    occurance_count.sort(key=lambda tup: tup[1], reverse=True)
    return occurance_count
