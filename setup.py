from setuptools import setup, find_packages

setup(
    name='mysite',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'django',
    ],
    package_data={
        'mysite.apps.personal': ['templates/*/*'],
        'mysite.apps.blog': ['templates/*/*']
    }
)
