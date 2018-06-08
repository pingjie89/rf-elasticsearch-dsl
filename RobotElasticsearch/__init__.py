from robot.api import logger

from .keywords import Keywords
from .version import __version__

class RobotElasticsearch(Keywords):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    
    def __init__(self):
        self.search_setting = {
            'index' : None,
            'doc_type' : 'doc',
            'body' : {}
        }