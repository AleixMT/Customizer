#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABC

from src.models.Installation import Installation
from src.repositories.Repository import Repository


class InstallationRepository(ABC, Repository):

    def __init__(self):
        pass

    def create(self, model: Installation):
        pass

    def read_all(self) -> list:
        pass

    def read(self, model_id: object) -> Installation:
        pass

    def update(self, model_id: object, model: Installation):
        pass

    def delete(self, model_id: object):
        pass

