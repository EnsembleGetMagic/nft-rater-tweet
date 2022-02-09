from pymongo import MongoClient
import os

CLUSTER = os.getenv('CLUSTER')

client = MongoClient(CLUSTER)

db = client.nftrater

collection = db.images