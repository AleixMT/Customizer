#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.models.Capability import Capability


class PackageCapability(Capability):

    def __init__(self):
        self.package_names: list = []

