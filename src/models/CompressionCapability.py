#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.models.Capability import Capability


class CompressionCapability(Capability):

    def __init__(self):
        self.originPath: str = ""
        self.destinationPath: str = ""
        self.decompressInPlace: str = ""  # possible values: True, False, Deduce

        