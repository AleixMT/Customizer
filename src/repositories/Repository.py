#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABC


class Repository(ABC):

    def __init__(self):
        pass

    def create(self, model: object):
        pass

    def read_all(self) -> list:
        pass

    def read(self, model_id: object) -> object:
        pass

    def update(self, model_id: object, model: object):
        pass

    def delete(self, model_id: object):
        pass

