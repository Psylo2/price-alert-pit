import os

import pymongo
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.errors import CollectionInvalid


class Repository:

    def __init__(self):
        self._uri = os.environ.get("REPOSITORY_URI")
        self._client = None
        self._database = None

    @property
    def client(self) -> MongoClient:
        if not self._client:
            self._client = pymongo.MongoClient(self._uri)
        return self._client

    @property
    def database(self) -> Database:
        if not self._database:
            self._database = self.client.get_default_database()
        return self._database

    def initialize(self):
        self.client
        self.database

    def get_collection(self, collection_name: str) -> Collection:
        return self.database.get_collection(name=collection_name)

    def create_collection(self, collection_name: str):
        try:
            self.database.create_collection(name=collection_name)
        except CollectionInvalid:
            pass
