<img src="https://github.com/johncoleman83/AirBnB_clone/blob/master/dev/HBTN-hbnb-Final.png" width="160" height=auto />

# AirBnB Clone Phase #1

: python BaseModel Class, unittests, python CLI, & web static

## Description

Project attempts to clone the the AirBnB application and website, including the
database, storage, RESTful API, Web Framework, and Front End.

## Environment

* __OS:__ Ubuntu 14.04 LTS
* __language:__ Python 3.4.3
* __style:__ PEP 8 (v. 1.7.0)

<img src="https://github.com/johncoleman83/AirBnB_clone/blob/master/dev/hbnb_step5.png" />

## Testing


#### `unittest`

This project uses python library, `unittest` to run tests on all python files.
All unittests are in the `./tests` directory with the command:

* `python3 -m unittest discover -v ./tests/`

The bash script `init_test.sh` executes all these tests:

  * checks `pep8` style

  * runs all unittests

  * runs all w3c_validator tests

  * cleans up all `__pycache__` directories and the storage file, `file.json`

**Usage:**

```
$ ./dev/init_test.sh
```

#### CLI Interactive Tests

This project uses python library, `cmd` to run tests in an interactive command
line interface.  To begin tests with the CLI, run this script:

```
$ ./console.py
```

* For a detailed description of all tests, run these commands inside the
custom CLI:

```
$ ./console.py
(hbnb) help help
List available commands with "help" or detailed help with "help cmd".
(hbnb) help

Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  airbnb  create   help  show
BaseModel  EOF   Review  User   all     destroy  quit  update

(hbnb) help User
class method with .function() syntax
        Usage: User.<command>(<id>)
(hbnb) help create
create: create [ARG]
        ARG = Class Name
        SYNOPSIS: Creates a new instance of the Class from given input ARG
```

* Tests in the CLI may also be executed with this syntax:

  * **destroy:** `<class name>.destroy(<id>)`

  * **update:** `<class name>.update(<id>, <attribute name>, <attribute value>)`

  * **update with dictionary:** `<class name>.update(<id>, <dictionary representation>)`

# AirBnB Clone Phase #3

Tasks:

1. Making sure all unittests pass and adding more tests.

2. Review the code to if there any logical errors, are all cases fully implemented, are the new automated tests sufficient for the new code, does the new code conform to existing style guidelines?.

3. Update DBStorage and FileStorage, adding two new methods: 1. A method to retrieve one object 2. A method to count the number of objects in storage.

4. Start the API.

5. Create an endpoint that retrieves the number of each objects by type.

6. In api/v1/app.py, create a handler for 404 errors that returns a JSON-formatted 404 status code response. The content should be: "error": "Not found".

7. Create a new view for `State` objects that handles all default RestFul API actions.

8. Same as `State`, create a new view for City objects that handles all default RestFul API actions.

9. Create a new view for `Amenity` objects that handles all default RestFul API actions.

10. Create a new view for `User` object that handles all default RestFul API actions.

11. Create a new view for `Place` objects that handles all default RestFul API actions.

12. Create a new view for `Review` object that handles all default RestFul API actions.

#### Continuous Integration

Uses [Travis-CI](https://travis-ci.org/) to run all tests on all commits to the
github repo

## Authors

* MJ Johnson, [@mj31508](https://github.com/mj31508)
* David John Coleman II, [davidjohncoleman.com](http://www.davidjohncoleman.com/)
* Kimberly Wong, [kjowong](http://github.com/kjowong) | [@kjowong](http://twitter.com/kjowong) | [kjowong@gmail.com](kjowong@gmail.com)
* Carrie Ybay, [hicarrie](http://github.com/hicarrie) | [@hicarrie_](http://twitter.com/hicarrie_)
* Spencer Cheng, [spencerhcheng](https://github.com/spencerhcheng) | [@spencerhcheng ](https://twitter.com/spencerhcheng)
* Katya Kalache, [katyakalache](https://github.com/KatyaKalache) | [@katyakalache](https://twitter.com/KatyaKalache)

## License

Public Domain, no copyright protection
