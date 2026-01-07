from setuptools import setup

setup(name='googlespider',
      version='0.1',
      description='A command line google spider. Extracts links.',
      # setup_requires=['setuptools-markdown'],
      long_description_markdown_filename='README.md',
      url='http://github.com/teamhg-memex/googlespider',
      author='Luke Maxwell',
      author_email='luke@codepunk.xyz',
      license='MIT',
      packages=['googlespider'],
      install_requires=[
          'tldextract',
          'requests',
          'beautifulsoup4',
          'lxml',
      ],
      include_package_data=True,
      exclude_package_data={'': ['*.pyc']},
      test_suite='nose.collector',
      tests_require=['nose'],
      entry_points={
          'console_scripts': ['googlespider=googlespider.command_line:main'],
      },
      zip_safe=False)
