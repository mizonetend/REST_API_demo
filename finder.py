import argparse
import subprocess
import os
import sys
sys.path.append('./src/')
sys.path.append('./data/')
import json

from dotenv import load_dotenv, dotenv_values
from pathlib import Path



from helper import Example, SelfCheck
from server import Server
from logger import Logger



load_dotenv(dotenv_path=Path('.env'))
config = dotenv_values()
version=os.getenv('VERSION')
print(f"VERSION: {version}")

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', help='enable verbose logs', action='store_true')
parser.add_argument('-s', '--sort' ,help='sort input list', action='store_true')
parser.add_argument('-e', '--example', help='generate usage example for the finder service', action='store_true')
parser.add_argument('--self_check', help='run self check', action='store_true')
parser.add_argument('--unit_test', help='run default unit tests', action='store_true')
parser.add_argument('--log_level', help='can overwrite the minimum log level (All 0, Debug 1, Info 2, Warning 3, Error 4, Critical 5)', required=False, type=int, choices=range(0,6), default=-1)

args = parser.parse_args()

# Overwrite minimum log level
if (args.log_level > -1):
    config['LOG_LEVEL'] = args.log_level

# Enable verbose mode - enable all logs
if (args.verbose):
    config['LOG_LEVEL'] = 0

logger = Logger(config['LOG_LEVEL'])
logger.DEBUG(f"Configuration: {json.dumps(config, indent=2)}")
logger.DEBUG(f"Args: {args}")

# Execute Self Check function
if (args.self_check):
    if (SelfCheck(config) == True):
        exit(0)
    else:
        exit(1)

#Show example    
if (args.example):
    Example(config)
    exit(0)

#Exacute unit tests
if (args.unit_test):
    logger.INFO(f"Starting unit tests...")
    cmd = 'python'
    param = './src/tests.py'
    print(f"run command: {cmd} {param}")
    try:
        logger.DEBUG(f"Executing command: {cmd} param: {param}")
        subprocess.run([cmd, param])
        logger.OK(f"Unit Test finished")
    except:
        logger.ERROR(f"Failed to run unit test")
        exit(1)
    
    exit(0)


#creating and starting server
server = Server(config)

server.Run()
