.. Googlespider documentation master file, created by
   sphinx-quickstart on Fri Jun 16 13:12:49 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Googlespider's documentation!
========================================

Googlespider is a simple command line utility for searching Google.

It supports batch requests with a polite (a.k.a slow) HTTP request policy.

It also supports country and language localisation -
Google results differ from country to country and language to language.

Country codes should be in ISO-3991 format. These determine the Google URL to use, e.g:

    $ googlespider -c us "hyperion gray"  # google.com
    $ googlespider -c ca "hyperion gray"  # google.ca
    $ googlespider -c gb "hyperion gray"  # google.co.uk


Examples of language formats can be found at
https://msdn.microsoft.com/en-gb/library/ee825488(v=cs.20).aspx.

These determine the language of the results, e.g:

    $ googlespider -c ca -l en-ca "hyperion gray"  # return results from google.ca in Canadian English

Contents:

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

