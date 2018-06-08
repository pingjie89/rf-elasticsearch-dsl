from .keywords import Keywords

class RobotElasticsearch(Keywords):
    def __init__(self):
        self.search_setting = {
            'index' : None,
            'doc_type' : 'doc',
            'body' : {}
        }