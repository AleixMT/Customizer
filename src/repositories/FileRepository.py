#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.repositories.Repository import Repository
import json
import os


class FileRepository(Repository):

    def __init__(self):
        super().__init__()
        self.data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))),
                                      "data")

    def create(self, model: str):
        #  TODO: Create files
        pass

    def read_all(self) -> list:
        pass

    def read(self, model_id: str) -> str:
        try:
            f = open(os.path.join(self.data_path, model_id))
            content = ""
            for line in f.readlines():
                content += line
            return content

        except IOError:
            pass

    def update(self, model_id: str, model: str):
        pass

    def delete(self, model_id: str):
        pass

