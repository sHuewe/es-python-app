from elasticsearch import Elasticsearch
import time
import os


esHost=os.environ.get("ES_HOST",None)
esPort=os.environ.get("ES_PORT",9200)
if esHost is not None:
    es = Elasticsearch([{"host":esHost,"port": esPort}])
    notAvailable=True
    while notAvailable:
        try:
            res=es.info()
            notAvailable = False
        except:
            print(f'Elasticsearch not available ({esHost}:{esPort}). Wait for 10 seconds ...')
            time.sleep(10)
    print("Elasticsearch is available!")
else:
    print("Elasticsearch is not configured via ES_HOST env. variable.")