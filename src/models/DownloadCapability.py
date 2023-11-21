#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.models.Capability import Capability


class DownloadCapability(Capability):

    def __init__(self):
        self.url: str = ""
        self.destinationPath: str = ""
        self.fileName: str = ""

