from setuptools import setup, find_packages
import sys, os
import django_siteanalytics

setup(
    name='django-siteanalytics',
    version='0.1',
    description="Basic visitor tracking for Django",
    long_description=open('README.md', 'r').read(),
    keywords='django, tracking, visitors',
    author='Marcos Lopez',
    author_email='dev@scidentify.info',
    url='http://github.com/mikelopez/django-siteanalytics',
    license='MIT',
    package_dir={'django_siteanalytics': 'django_siteanalytics'},
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: Log Analysis",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Page Counters",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        "Topic :: Security",
        "Topic :: System :: Monitoring",
        "Topic :: Utilities",
    ]
)
