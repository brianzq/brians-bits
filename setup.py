from setuptools import setup, find_packages

setup(
    name='mysite',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'django',
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'mysiteadmin=mysite.manage:main',
        ],
    },
)
