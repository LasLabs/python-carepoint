[![Build Status](https://api.travis-ci.org/laslabs/Python-Carepoint.svg?branch=release%2F0.1)](https://travis-ci.org/laslabs/Python-Carepoint)
[![Coverage Status](https://coveralls.io/repos/laslabs/Python-Carepoint/badge.svg?branch=release%2F0.1)](https://coveralls.io/r/laslabs/Python-Carepoint?branch=release%2F0.1)

Python CarePoint Library
========================

This library will allow you to interact with CarePoint using Python.

For the most part, it just provides some convenience wrappers to encapsulate
all of the tables within one object/session for easy use.

Most of the methods return SQLAlchemy ResultProxies.

Installation
------------

To install this module, you need to:

* Utilize a system able to access all CarePoint network resources (database, SMB)
  * This includes things like DNS entries for the NETBIOS names
* Setup UnixODBC - http://help.interfaceware.com/kb/904
* Install UnixODBC development headers - `apt-get install unixodbc-dev`
* Install dependencies - `pip install -r requirements.txt`
* Install library - `pip install .`


Setup
-----

* Create an Active Directory user
* Give AD user permissions to CarePoint images and data net shares
* Give AD user read & write permissions on the following databases:
  * cph
  * grx_master


Usage
-----

### Connect to Database server

    from carepoint import Carepoint
    
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

### Get image using SMB path from database

    cp = Carepoint(**opts)
    img_rec = cp.search(cp['FdbImg']).first()
    image_file = cp.get_file(img_rec.IMAGE_PATH)
    image_data = image_file.read()


Known Issues / Road Map
-----------------------

* More usage samples
* Test coverage is showing less than what it actually is (carepoint and db modules)
* A decent amount of models are missing
* Create documentation of models
* Add some basic validations
* Create a column type that will retrieve file from SMB path in DB
* Better SMB support (allow ftimes, dir list, caching)
* FDB images only serve from store ID 1's net share
* Having to pass the model to the Carepoint object is annoying, objectify the syntax

Bug Tracker
-----------

Bugs are tracked on [Github Issues](https://github.com/laslabs/python-carepoint/issues>).
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, please help us to smash it by providing a detailed and welcomed feedback.


Contributors
------------

* Dave Lasley <dave@laslabs.com>
* Vinnie Corcoran <vcorcoran@laslabs.com>

Maintainer
----------

[![LasLabs Inc.](https://laslabs.com/logo.png "LasLabs Inc.")](https://laslabs.com)

This module is maintained by [LasLabs Inc.](https://laslabs.com)

* https://github.com/laslabs/Python-Carepoint
