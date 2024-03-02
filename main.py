import logging
import logging.config
import yaml
import HelperModules

with open('Config/ConfigLog.conf') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)
logger = logging.getLogger('MyApp')
logger.info('Logger Initialized!')

def TestFuction():
    Num1 = 15
    Num2 = 12
    logger.info('Calling Helper Methods')
    Ans = HelperModules.doAdd(Num1, Num2)



if __name__ == '__main__':
    logger.info('Started Main Method!')
    TestFuction()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
