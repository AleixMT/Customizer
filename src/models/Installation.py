#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path


class Installation:

    def __init__(self):
        self.name: str = ""
        self.description: str = ""
        self.version: str = ""
        self.tags: list = []  # TODO: this has to be an enum
        self.categories: list = []  # TODO: this has to be an enum
        self.icon: Path  # TODO: initialize this to Customizer's path
        self.steps: list = []

