from setuptools import setup

from amazon_advertising_api import versions

setup(
    name='amazon_advertising_api',
    packages=['amazon_advertising_api'],
    version=versions.__version__,
    description='Unofficial Amazon Sponsored Products Python client library.',
    url='https://github.com/pepsico-ecommerce/amazon-advertising-api-python')
