from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections, Search

class Keywords(object):

### Base keywords
    @keyword
    def setup_connection(self, host):
        

    @keyword
    def query_elastic(self):
        pass

    @keyword
    def get_body(self):
        pass

    @keyword
    def exclude(self):
        pass
###

### Search body built keywords
    @keyword
    def something:
        pass

    @keyword
    def add_filter(self):
        pass

    @keyword
    def exclude(self):
        pass
    
    @keyword
    def aggregate(self):
        pass
###
    