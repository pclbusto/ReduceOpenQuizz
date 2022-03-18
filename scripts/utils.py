#!/usr/local/bin/python3
# ========================================
# Common utilities
# ========================================
import argparse
import csv
import io
import json
import inspect
import os
import subprocess
import sys
import unicodedata
import string

# - Help Multiline
# - Show default values
class MyArgumentFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawTextHelpFormatter):
    """ Argument formatter that has best of both worlds: help multiline and show the default values.

    Usage:

    from utils import MyArgumentFormatter

    if __name__ == "__main__":
        parser = argparse.argumentparser(
            formatter_class=MyArgumentFormatter,
            description="""
            .....
""")
    """


    pass

def saveAsCsv(data, file_csv):
    """ Get a map or list and save it as CSV.

    - If data is a list, save every 'row' in the CSV without header.
    - If data is a list of maps, save every element in a CSV with header
    
    """
    if not data or len(data)==0: return

    if type(data[0]) is list:
        with open(file_csv, mode='w', newline='') as fCsv:
            csv_writer = csv.writer(fCsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for item in data:
              csv_writer.writerow(item)
    else:
        # Get all the possilbe field names we find in all the records
        # so we build the header
        fieldnames=[]
        for item in data:
            for key in item:
                if key not in fieldnames: fieldnames.append(key)

        with open(file_csv, mode='w', newline='') as fCsv:
            csv_writer = csv.DictWriter(fCsv, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writeheader()
            for item in data:
              csv_writer.writerow(item)

def list2Map(list, key, allowDuplicates=False):
  """ Convert a list of maps in a map where the key is the value of attribute 'key'. 

  So is list=[ {"name" : "A", "desc" : "Desc A"}, {"name" : "B", "desc" : "Desc B"} ]

  then list2Map(list, 'name') = {
    "A" : {"name" : "A", "desc" : "Desc A"},
    "B" : {"name" : "B", "desc" : "Desc B"}
  }
  """
  data={}
  for item in list:
    val=item[key]
    if allowDuplicates:
      if not val in data: data[val]=[]
      data[val].append(item)
    else:
      if val in data: raiseException("Value %s for key %s already exists" % (val, key))
      data[val]=item

  return data

def csv2List(file, delimiter=","):
  """ Reads a csv file with header and returns a list of the dictionaries. """

  data=[]
  with open(file, newline='', encoding='utf-8') as f:
    # reader = csv.DictReader(f, delimiter=delimiter)
    reader = csv.DictReader(filter(lambda row: row[0]!='#', f), delimiter=delimiter)
    for row in reader:
      data.append(row)

  return data

def remap(p_data, p_map):
    """ Remap p_data (json) to another json extacting some data using p_map.

    p_map in an array of the form
    - new_name
    - path"""

    data={}
    for name, path in p_map.items():
        data[name]=getFieldValue(p_data, path)

    return data

def dedup(values, keyField, keepNone=False):
  data=[]
  for item in values:
    keyValue=item[keyField]
    if (keyValue or  keepNone) and keyValue not in data:
      data.append(keyValue)

  return data

def group(values, keyField, allowDuplicates=True, keyRequired=True):
  data={}
  for item in values:
    keyValue=item
    # Allow keyField as fields.issuetype.name
    for v in keyField.split('.'):
      if v not in keyValue:
          if keyRequired:
              raise Exception("Key %s not found in %s and it is required", v, keyValue) 
          else:
              keyValue=None 
              break
      keyValue=keyValue[v]

    if keyValue:
        keyValue=str(keyValue)
        if allowDuplicates:
            if keyValue not in data:
              data[keyValue]=[]
            data[keyValue].append(item)
        else:
            if keyValue in data:
                raise Exception("Dupplicated key %s in %o and they are not allowed" % (keyValue, item))
            data[keyValue]=item

  return data

def getJsonWithCache(p_file, p_func, save=True):
    """Generic function able to perform a get a JSON from cache and keep it.

    p_func() is a lambda to obtain data and save it to p_file or get it from 
    there in case is stored.

    Example:
    data=_getJson(
        <file>,
        lambda: <function returning JSON>
    )
    """
    data = None
    if save and os.path.isfile(p_file):
        trace("Looking for %s ..." % (p_file))
        with open(p_file) as f:
            data=json.load(f)
            trace("Found, data read from %s!" % (p_file))
    else:
        data=p_func()
        if save:
            with open(p_file, 'w') as json_file:
                json.dump(data, json_file, indent=2)
                trace("Not found, data stored in %s!" % (p_file))

    return data

# TODO : unify, the both do the same
def getFieldValue(item, key, default=None):
    """ Basic function that gets the value of a map but taking into account the '.'. """

    #print ("getFieldValue(%s)" % (key))
    #print (json.dumps(item,indent=2))
    if not item: return default

    if inspect.isfunction(key):
        return key(item)
    else:
      if '.' in key:
          #print("1) key : %s" % (key))
          fields=key.split('.')
          return default if fields[0] not in item else getFieldValue(item[fields[0]], '.'.join(fields[1:]), default)
      else:
          #print("2) key : %s" % (key))
          #print(item)
          return default if key not in item else item[key]

def remove_accents(data):
    return ''.join(x for x in unicodedata.normalize('NFKD', data) if x in string.printable)

def remove_spaces(data):
    return data.translate({ord(c): None for c in string.whitespace})

def updListOfDictionaries(p_origin, p_upd, p_key, p_only_new_fields=True, p_upd_fields=None):
    """Update a list of Dictionaries with new values.

    'origin' contains a list of dictionaries that can be identify unique by 'key'.
    'upd' is a another list with some updates with the same 'key'.
    If 'only_new_fields'==True, only the fields in 'upd' that are NOT in 'origin' are 
    added to 'origin'.
    If 'only_new_fields'==False all the fields or the ones in 'upd_fields' are updated."""

    originById=group(p_origin, p_key, False)
    updById=group(p_upd, p_key, False)

    for upd_key, upd_item in updById.items():
        # TODO : if the key is not in origin, do we add the possibility for ADDING a
        #        new record in origin .... hmmm ....
        if upd_key in originById:
            origin_item = originById[upd_key]
            for upd_field, upd_value in upd_item.items():
                # ADD only fields in upd NOT in origin (new info)
                if p_only_new_fields:
                    if upd_field not in origin_item:
                        origin_item[upd_field] = upd_value
                # OVERWRITE the field
                else:
                    if not p_upd_fields or upd_field in p_upd_fields:
                        origin_item[upd_field] = upd_value

def getPercInt(p_v1, p_v2):
    return 0 if (p_v1+p_v2)==0 else int(p_v1*100/(p_v1+p_v2))

def getSafeFilename(filename):
    return "".join([c for c in filename if c.isalpha() or c.isdigit() or c in ['_','.']]).rstrip()

if __name__ == "__main__":
    pass
