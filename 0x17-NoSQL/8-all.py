#!/usr/bin/env python3
""" 8-all.py """
import pymongo


def list_all(mongo_collection):
    """ lists all documents in a collection in Python"""
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
