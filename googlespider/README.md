Googlespider
------------
A python Google scraper.

Extract result URLs from Google search queries.

Requires Python 3.x.x.


Notes
-----

Automated scraping of Google is against their TOS, this script is for educational puposes only. 

Only 'web' results are included. Universal results, e.g. images, news, etc., *are stripped out*.  If you want results that include these, this is not the tool you are looking for.

Requests are throttled in order to be kind to Google (30 seconds). Using this script concurrently from the same IP, or even querying Google while using this script, may trigger captchas and break the script - it does not handle such errors. 


Installation
------------

```bash
$ git clone https://github.com/teamhg-memex/googlespider.git
$ pip3 install -e googlespider
```

Usage
-----

Googlespider provides a shell command. To use (with caution), simply do:

```bash
$ googlespider --query "hyperion gray" --max 10
```

And get the below:

```bash
Requesting https://www.google.com/search?gl=us&q=hyperion+gray&start=0&num=100
hyperion gray	1	http://www.hyperiongray.com/
hyperion gray	2	https://www.punkspider.org/
hyperion gray	3	http://www.forbes.com/sites/thomasbrewster/2015/05/06/punkspider-google-for-all-web-vulnerabilities/
hyperion gray	4	https://twitter.com/hyperiongray?lang=en-gb
hyperion gray	5	http://hyperiongray.tumblr.com/
hyperion gray	6	https://www.linkedin.com/in/amanda-towler-2988167
hyperion gray	7	https://www.linkedin.com/company/hyperion-gray
hyperion gray	8	https://www.linkedin.com/in/alejandrojcaceres
hyperion gray	9	http://upstart.bizjournals.com/companies/innovation/2015/04/13/hyperion-gray-building-an-army-of-robot-interns-to.html
hyperion gray	10	http://www.theregister.co.uk/2013/02/21/punkspider/

```

```bash
$ googlespider --help
usage: googlespider [-h] [--query QUERY] [--country COUNTRY] [--file FILE]
                    [--proxy PROXY] [--language LANGUAGE] [--max MAX]
                    [--results-per-page RESULTS_PER_PAGE]

optional arguments:
  -h, --help            show this help message and exit
  --query QUERY       search phrase for which to perform Google search.
  --country COUNTRY     two letter ISO country code. Determines search
                        URL, e.g. google.co.uk, google.com, google.fr.
  --file FILE           path to phrase file.
  --proxy PROXY         use proxy string USERNAME:PASSWORD@IP:PORT.
  --language LANGUAGE   set ACCEPT-LANGUAGE request header. Can affect results
                        returned by Google.Format is [2-letter language
                        code]-[2-letter country code], or [2 letter language
                        code]. Examples are en-gb, en-us, es-cl, and en. More
                        examples here: https://msdn.microsoft.com/en-
                        gb/library/ee825488(v=cs.20).aspx
  --max MAX             max number of results to check (1 - 1000)
  --results-per-page RESULTS_PER_PAGE
                        number of results per page (1 - 100)

```

HTTPS Warnings
--------------

Googlespider uses the requests module which in turn depends on urllib3. These will trigger various warnings when requesting secure URLs, e.g. https://www.google.com.

`InsecurePlatformWarning` and  `SNIMissingWarning` can sometimes be resolved by installing the requests package with the security dependencies:

```
$ pip install requests[security]
```

If you have not properly configured SSL certificate support you will see `InsecureRequestWarning`. You can temporarily ignore these by setting an environment variable:

```
export PYTHONWARNINGS="ignore:Unverified HTTPS request"
```
