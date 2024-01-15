from os.path import exists
from logger import Logger
import json


################ Example ################
def Example(config):
    print(f"Welcome in finder REST demo!\n\n")

    with open('./data/example.txt') as f:
        content = f.read()
        content = content.replace("{PORT}", config['PORT'])
        content = content.replace("{CONFIG}", json.dumps(config, indent=2))
        print(content)
    
    print(f"Welcome in finder REST demo!")

################ SelfCheck ################
def SelfCheck(config):
    logger = Logger(int(config['LOG_LEVEL']))
    logger.INFO('Starting Self Check service...')
    res = True
    env_ok = True
    mandatory_fields= ['HOST', 'PORT', 'INPUT_FILE']

    for value in mandatory_fields:
        if value not in config.keys():
            logger.INFO(f"{value} is not defined in the .env file")
            env_ok = False

    if (env_ok):
        logger.OK('.env tests passed')
    else:
        logger.ERROR('.env tests failed')

    data_files = True
    mandatoy_data_files = ['./input.txt', './src/server.py', './src/logger.py']

    for value in mandatoy_data_files:
        if (not exists(value)):
            data_files = False
            logger.INFO(f"{value} not found")

    if (data_files):
        logger.OK('resource tests passed')
    else:
        logger.ERROR('resource tests failed')

    is_valid_input, err_idx, err_value = CheckData(config)
    if (is_valid_input):
        logger.OK('input file test passed')
    else:
        logger.ERROR('input file test failed')

    res = data_files and env_ok and is_valid_input

    logger.INFO('Self testing finished')

    if (res == True):
        logger.OK('All tests passed')
    else:
        logger.ERROR('Some tests failed - please check the report and fix the issues.')
    
    return res

################ SelfCheck ################
def Sort(config):
    Logger().CRITICAL(f"[Sort] - Function not yet available - contact the developer team")
    return True

################ SelfCheck ################
def Normalize(config):
    Logger().CRITICAL(f"[Normalize] - Function not yet available - contact the developer team")
    return True

################ CheckData ################
def CheckData(config):
    logger = Logger(int(config['LOG_LEVEL']))
    input = config['INPUT_FILE']
    logger.DEBUG(f"Validating input file ({input})")

    with open(input) as datasource: 
        #data = datasource.readlines() 
        data=datasource.read().splitlines()
    
    length = len(data)
    
    bad_pairs = []
    bad_indexes = []

    res = True
    if length > 1:
        for index in range(1, length, 1):
            if int(data[index - 1]) > int(data[index]):
                bad_pairs.append([data[index - 1], data[index]])
                bad_indexes.append([data[index - 1], data[index]])
                res = False
                logger.DEBUG(f"not sorted at: index({index-1}-{index}) value: ({data[index - 1]},{data[index]})")
    
    logger.DEBUG(f"Finished input file ({input}) validation - valid: {res}")

    return res, bad_indexes, bad_pairs