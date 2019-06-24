#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2008 John Paulett (john -at- paulett.org)
# Copyright (C) 2009-2013 David Aguilar (davvid -at- gmail.com)
# Copyright (C) 2013 Xingchen Yu (initialxy -at- gmail.com)
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

import os
try:
    import setuptools as setup_mod
except ImportError:
    import distutils.core as setup_mod

here = os.path.dirname(__file__)
version = os.path.join(here, 'jsonstruct', 'version.py')
scope = {}
exec(open(version).read(), scope)

SETUP_ARGS = dict(
    name="jsonstruct",
    version=scope['VERSION'],
    description="Python library for serializing and deserializing "
            "typed Python objets to and from JSON",
    long_description = "jsonstruct is a library for two way conversion of "
            "typed Python object and JSON. This project is originally a fork "
            "of jsonpickle. The key difference between this library and "
            "jsonpickle is that during deserialization, jsonpickle requires "
            "Python types to be recorded as part of the JSON. This library "
            "intends to remove this requirement, instead, requires a class to "
            "be passed in as an argument so that its definition can be "
            "inspected. It will then return an instance of the given class. "
            "This approach is similar to how Jackson (of Java) works.",
    author="Xingchen Yu",
    author_email="initialxy -at- gmail.com",
    url="https://github.com/initialxy/jsonstruct",
    license="BSD",
    platforms=['POSIX', 'Windows'],
    keywords=['jsonstruct', 'typed json', 'json', 'pickle', 'marshal',
            'unmarshal', 'serialization', 'deserialization',
            'JavaScript Object Notation'],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: JavaScript",
    ],
    options={'clean': {'all': 1}},
    packages=["jsonstruct"],
)


if __name__ == '__main__':
    setup_mod.setup(**SETUP_ARGS)
