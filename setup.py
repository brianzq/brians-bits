from setuptools import setup, find_packages

setup(
    name='mysite',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'django',
        'pillow',
    ],
    package_data={
        'mysite': ['db.sqlite3'],
    },
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'mysiteadmin=mysite.manage:main',
        ],
    },
)
