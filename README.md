[![Build Status](https://api.travis-ci.org/laslabs/Python-Carepoint.svg?branch=release%2F0.1)](https://travis-ci.org/laslabs/Python-Carepoint)
[![Coverage Status](https://coveralls.io/repos/laslabs/Python-Carepoint/badge.svg?branch=release%2F0.1)](https://coveralls.io/r/laslabs/Python-Carepoint)

Python CarePoint Library
========================

This library will allow you to interact with CarePoint using Python.

For the most part, it just provides some convenience wrappers to encapsulate
all of the tables within one object/session for easy use.

Most of the methods return SQLAlchemy ResultProxies.

Installation
------------

To install this module, you need to:

* Setup UnixODBC - http://help.interfaceware.com/kb/904
* Install UnixODBC development headers - `apt-get install unixodbc-dev`
* Install dependencies - `pip install -r requirements.txt`
* Install library - `pip install .`


Setup
-----

* Create an Active Directory user 


Usage
-----

### Connect to Database server

    cp = Carepoint(
        server='127.0.0.1',
        user='test_db_user',
        passwd='db_pass',
    )

### Perform a search for a patient with the last name Smith

    res = cp.search(
        cp['Patient'],
        {'lname': 'Smith'},
    )
    for row in res:
        print row.fname

### Perform a patient search, but only return the `mname` column

    res = cp.search(
        cp['Patient'],
        {'lname': 'Smith'},
        ['mname'],
    )
    for row in res:
        print row.mname

### Get patients modified in 2015

    res = cp.search(
        cp['Patient'],
        {
            'chg_date': {
                '<=': '2015-12-31',
                '>=': '2015-01-01',
            }
        },
    )
    for row in res:
        print row.fname

Known Issues / Road Map
-----------------------

* More usage samples
* Test coverage is showing less than what it actually is (carepoint and db modules)
* A decent amount of models are missing
* Create documentation of models
* Image SMB paths are stored in DB, need to write download mechanism

Contributors
------------

* Dave Lasley <dave@laslabs.com>
* Vinnie Corcoran <vcorcoran@laslabs.com>

Maintainer
----------

[![LasLabs Inc.](https://laslabs.com/logo.png "LasLabs Inc.")](https://laslabs.com)

This module is maintained by [LasLabs Inc.](https://laslabs.com)

* https://repo.laslabs.com/projects/CP/repos/python-carepoint/
