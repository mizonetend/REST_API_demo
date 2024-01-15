# Welcome to  python REST demo repository!


This repository is to demonstrate **python** based **REST** API with efficient finder solution in big sorted lists.


## Task description:

We have created large file containing sorted numbers from 0 to 1000000, for example:
```
Value: 0 10 20 100 … 1000000
Index: 0 1 2 3 … 50000
```

We would like to be able to call designed endpoint with http `GET` method and send `value` that should be found in input file.

As a response we should get `index` number for given value and the corresponding value and optional message.

For example, we are sending GET for /endpoint/100 and as result we should receive 3.

  Remark: `As a requirement`, we want to load that file into `slice` once service starts.

So all search operations should be optimized for that particular slice.

- In case you’re not able to find index for given value, you can return `index` for any other existing value, assuming that conformation is at `10% level`, (for example, you were looking for `index` for value = `1150`, but in input file you have `1100` and `1200`, so in that case you can return index for `1100` or `1200`).

- In case you were not able to find valid `index` number, `error message` should be added into response.

`To summarize`:

- Design API for http `GET` method

- Implement functionality for searching `index` for `given` value (it should be the most efficient algorithm)
- Add logging
- Add possibility to use configuration file where you can specify service port and log level (you should be able to choose between Info, Debug, Error)
- Add `unit tests` for created components
- Add `README.md` to describe your service
- Automate running tests with `make` file
- Remember that code structure matters
- Upload solution into `GitHub` account and share the link

# Project

## Virtual environment
The project is written in python3. To help in the installation and avoid interfere with other python projects - the solution uses **venv**.

The `venv` module supports creating lightweight “virtual environments”, each with their own independent set of Python packages installed in their [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.") directories. A virtual environment is created on top of an existing Python installation, known as the virtual environment’s “base” Python, and may optionally be isolated from the packages in the base environment, so only those explicitly installed in the virtual environment are available.

## Installation

**The project requires the latest python3. If you do not have on your machine - please  [download python](https://www.python.org/downloads/)**
- if do not have pip - [install pip](https://pip.pypa.io/en/stable/installation/#)

### make
- run ```make init```

### manually
- create new python virtual environment: ```python -m venv finder```
- install requirements: ```pip install -r required_packages.txt``` 
- you might need to update pip ```python -m pip install --upgrade pip```

Now you have a working environment.

## using python venv

activate the environment:

- go to the project folder

|Platform|command|
|:--|:--|
|POSIX|```source \<venv\>/bin/activate```|
|Windows|```C:\\>  \<venv\>\Scripts\activate.bat```|


deactivate the environment:
```
deactivate
```

## Files
- The source code is in the **./src** folder
- The application / executable code is **./finder.py**
- The data files are in the **./data** folder (eg.: input.txt)
- The configurations can be found in the **.env** file.

## Code structure
### ./finder.py
The finder.py is the entry point of the application.

To get help type python finder.py -h
```
VERSION: 1.1.0a
usage: finder.py [-h] [-v] [-s] [-e] [--self_check] [--unit_test]
[--log_level {0,1,2,3,4,5}]
optional arguments:
-h, --help          show this help message and exit
-v, --verbose       enable verbose logs
-s, --sort          sort input list
-e, --example       generate usage example for the finder service
--self_check        run self check
--unit_test         run default unit tests
--log_level         {0,1,2,3,4,5} can overwrite the minimum log level (All 0, Debug 1, Info 2, Warning 3, Error 4, Critical 5)
```

### ./src/server.py
The server.py - uses flask to create REST service. It maps the endpoint to the proper function and manages the http response.**

### ./src/logic.py
The logic.py contains the finder logic - to find the given index or indexes.
### ./src/logger.py
This is a simple logger - what uses colorant - to colour the output and supports log-levels:
```
class  Loglevels(Enum):
  ALL = 0
  DEBUG = 1
  INFO = 2
  WARNING = 3
  ERROR = 4
  CRITICAL = 5
```
### ./src/helper.py
The helper.py file contains helper functions eg.: SelfCheck, Example, ...

### .env
All the configurations stored in the .env file.
```
VERSION=1.1.0a
EXAMPLE=./data/example.txt
FOLDER_SRC=./src/
FOLDER_DATA=./data/
HOST=0.0.0.0
PORT=3333
INPUT_FILE=./input_2.txt
MISS_RATIO=10
LOG_LEVEL=2
```

- If the project cannot start because of the configured port is already in use: please modify the **PORT** in the .env file
- if would use other input data modify the **INPUT_FILE**'s value
- to configure the minimum log level modify the value of the **LOG_LEVEL** field
- also there is an option to modify the default 10% epsilon value by - changing the **MISS_RATIO** field. (the value is in percentage (range: 0-...))

## Starting the porject

to start the project run: ```python3 finder.py```
or ```make run```

**Getting usage example**
run ```python finder.py --example```
or ```make example```


## Code complexity

Lets mark the number of records in the input file with “n” and use the Big O notation to measure the algorithm's efficiency.

The finder's function does binary searching in the list of data. complexity is f(n) = O(log(n)+1)

- Exact match found: **f(n) = O(log(n)+1)**

Finding indexes fit to the ```target_value +- acceptable_error``` range
We are using here two binary searches.
- one from the beginning of the list till the closest match
- another one from the closest match till the end of the list

both of the **g(x) = O(log(n/2)+1)**
the 2 searches has O(log(n)+1) (logarithmic) complexity

In summary, the complexity of the functions is logarithmic. **finder(n) = O(2\*(log(n)+1)) = O(log(n))**

# Known issues and future optimizations

- The code could do automatic self repair - eg.: changing port if it is already in use
- We can extend the code with try - catch blocks - to do proper error handling
- Could use more sophisticated REST handling (application:json, standard responses, proper parameter handling, ...)
- Could use openapi and swagger files to generate the REST on a very modern way
- Could optimize the performance - of the REST server.
- We could use any built-in logger system - to have more advanced functions. (eg.: import logger, or anything else)
- Could extend the REST APIs - with more functions - to make it user friendly

# Work log

- **./finder.py** (1h)
  - added **argparse** - to handle parameters - to make the system user friendly
- **./src/helper.py** (1h)
  - extended the system with some helper logic - eg.: SelfCheck and HelpFunction to show usage info for the tester
- **./src/logger.py** (1h)
  - using colorant - to colour the logs
  - not using in built logger - to show we can make our own logger - or extend any other in-built logger system
  - this is a logger demo
- **./src/tests.py** (1h)
  - using "unittest" module
  - this is a basic unit test for the system
  - testing was more time then the implementation
- **./src/logic.py** (2.5h)
  - had 2 iteration for the "FindIndex" function
  - the implementation was fast, but had some headaches with the testing
- **./src/server.py** (1.5h)
  - used "flask" to handle REST based service
  - spent some extra time to the response handling and testing
- **./.env** (5minutes)
  - using .env as configuration file
  - could use a simple json as well, but .env is also an industrial standard on many areas
- **./README.md** (2h)
  - spent significant time to make a small documentation for the project
- **testing** (3h)
  - spent tons of time to test the system and the extra functionalities
- **MakeFile and environment testing** (2h)
  - not made MakeFile in the past year - and had to refresh my memory a bit.
  - testing the make file takes significant time.

**TOTAL** ~2 days