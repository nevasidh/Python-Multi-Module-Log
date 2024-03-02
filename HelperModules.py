import logging
logger = logging.getLogger(__name__)


def doAdd(Num1, Num2):
    logger.debug('Executing method doAdd with params {0} , {1}'.format(Num1, Num2) )
    Ans = Num1 + Num2
    logger.info('Result is  {0}'.format(Ans) )
    return Ans
