Eve Genie
=========

A tool for making Eve schema generation easier.

**Use case**: You need to stand up an api quickly. You know what your data looks like in JSON but don't yet know the syntax for Eve/Cerberus.

Requirements
---------------

::

    sudo pip install -r requirements.txt


Use in Terminal
---------------

    python geneve.py your_json_file

Use in Code
-----------

::

    from evegenie import EveGenie
    eg = EveGenie(filename='test.json')
    # Or
    with open('test.json', 'r') as ifile:
        data = ifile.read()
    eg = EveGenie(data=data)
    eg.write_file('mytest.settings.py')

This will producs the file `mytest.settings.py`::

    cat mytest.settings.py

Results in ::

    user = {
        'schema': {
            'name': {'type': 'string'},
            'title': {'type': 'string'},
            'age': {'type': 'integer'},
            'alive': {'type': 'boolean'},
            'inventory': {'type': 'list'},
            'address': {
                'type': 'dict',
                'schema': {
                    'city': {'type': 'string'},
                    'state': {'type': 'string'},
                    'address': {'type': 'string'},
                }
            }
        }
    }

    artifact = {
        'schema': {
            'color': {'type': 'string'},
            'cost': {'type': 'float'},
            'stats': {
                'type': 'dict',
                'schema': {
                    'length': {'type': 'float'},
                    'weight': {'type': 'float'},
                    'power': {'type': 'integer'},
                }
            }
            'name': {'type': 'string'},
        }
    }

Advanced Value Replacement in Strings
-------------------------------------

Strings formated in a special form within the source json file, will be converted to eve
schema types with sane defaults.

- `"fieldname": "objectid:sample-entity"` will add data_relation to sample-entity to the schema
- `"fieldname": "0-100"` will create an integer with a min of 0 and a max of 100
- `"fieldname": "0.0-1.0"` will create a float with a min of 0 and a max of 1
- `"fieldname": {"allow_unknown": true}` will translate directly to fieldname that allows the unknown

Test
-------

A test can be issued with::

    py.test egtest.py


