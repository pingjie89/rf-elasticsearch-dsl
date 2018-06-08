from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections, Search

from robot.api import logger
from robot.api.deco import keyword

class Keywords(object):
### Base keywords
    @keyword
    def setup_es_connection(self, hosts=None, port=9200, http_auth=None, 
        use_ssl=False, verify_certs=True, ca_certs=None, client_cert=None,
        client_key=None, headers=None):
        '''Keyword wrapper on top elasticsearch-py constructor
        '''
            self.es = Elasticsearch(hosts, port=port, http_auth=http_auth, 
                                    use_ssl=use_ssl, verify_certs=verify_certs, 
                                    ca_certs=ca_certs, client_cert=client_cert,
                                    client_key=client_key, headers=headers)

    @keyword
    def simple_query(self):
        '''Simple query based on doc_type and body without advanced setting
        '''
        self.es.search(self.search_setting['index'],doc_type=self.search_setting['doc_type'],self.search_setting['body'])

    @keyword
    def query_elastic(self):
        pass

    @keyword
    def exclude(self):
        pass
###

### Search setting keywords
    @keyword 
    def set_doc_type(self, type='doc'):
        self.search_setting['doc_type'] = type
    
    @keyword
    def get_body_from_file(self,filepath):
        with open(filepath, 'r') as file:
            self.search_setting['body'] = file.read()
###

### Search body built keywords
    @keyword
    def something():
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
    