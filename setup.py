from setuptools import setup

setup(
    name='flasky',
    install_requires=[
        'Click',
        'Flask'
    ],
    entry_points={
        'console_scripts': [
            'flasky=flasky.cli:cli'
        ],
    },
)