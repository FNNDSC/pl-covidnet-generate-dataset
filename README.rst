pl-covidnet-generate-dataset
================================

.. image:: https://badge.fury.io/py/covidnet_generate_dataset.svg
    :target: https://badge.fury.io/py/covidnet_generate_dataset

.. image:: https://travis-ci.org/FNNDSC/covidnet_generate_dataset.svg?branch=master
    :target: https://travis-ci.org/FNNDSC/covidnet_generate_dataset

.. image:: https://img.shields.io/badge/python-3.5%2B-blue.svg
    :target: https://badge.fury.io/py/pl-covidnet_generate_dataset

.. contents:: Table of Contents


Abstract
--------

A ChRIS plugin app that downloads dataset and generates combined dataset for Covid-Net 


Synopsis
--------

.. code::

    python covidnet_generate_dataset.py                                           \
        [-v <level>] [--verbosity <level>]                          \
        [--version]                                                 \
        [--man]                                                     \
        [--meta]                                                    \
        <inputDir>
        <outputDir> 

Description
-----------

``covidnet_generate_dataset.py`` is a ChRIS-based application that...

Arguments
---------

.. code::

    [-v <level>] [--verbosity <level>]
    Verbosity level for app. Not used currently.

    [--version]
    If specified, print version number. 
    
    [--man]
    If specified, print (this) man page.

    [--meta]
    If specified, print plugin meta data.


Run
----

This ``plugin`` can be run in two modes: natively as a python package or as a containerized docker image.

Using PyPI
~~~~~~~~~~

To run from PyPI, simply do a 

.. code:: bash

    pip install covidnet_generate_dataset

and run with

.. code:: bash

    covidnet_generate_dataset.py --man /tmp /tmp

to get inline help. The app should also understand being called with only two positional arguments

.. code:: bash

    covidnet_generate_dataset.py /some/input/directory /destination/directory


Using ``docker run``
~~~~~~~~~~~~~~~~~~~~

To run using ``docker``, be sure to assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``. *Make sure that the* ``$(pwd)/out`` *directory is world writable!*

Now, prefix all calls with 

.. code:: bash

    docker run --rm -v $(pwd)/out:/outgoing                             \
            fnndsc/pl-covidnet_generate_dataset covidnet_generate_dataset.py                        \

Thus, getting inline help is:

.. code:: bash

    mkdir in out && chmod 777 out
    docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
            fnndsc/pl-covidnet_generate_dataset covidnet_generate_dataset.py                        \
            --man                                                       \
            /incoming /outgoing

Examples
--------





