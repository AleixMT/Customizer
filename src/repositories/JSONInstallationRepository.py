#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.models.Installation import Installation
from src.repositories.FileRepository import FileRepository
from src.repositories.InstallationRepository import InstallationRepository
import json
import os


class JSONInstallationRepository(InstallationRepository):

    def __init__(self):
        self.fileRepository = FileRepository()

    def create(self, model: Installation):
        #  TODO: create installation parsed json.dumps
        pass

    def read_all(self) -> list:
        pass

    def read(self, model_id: str) -> Installation:
        content = self.fileRepository.read(model_id)
        installation = Installation()
        installation_data = json.loads(content)
        installation.name = installation_data["name"]
        installation.description = installation_data["description"]
        installation.version = installation_data["version"]
        installation.tags = installation_data["tags"]
        installation.categories = installation_data["categories"]
        installation.icon = installation_data["icon"]
        installation.steps = installation_data["steps"]
        return installation

    def update(self, model_id: str, model: Installation):
        pass

    def delete(self, model_id: str):
        pass

