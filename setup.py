from setuptools import find_packages
from setuptools import setup


setup(
    name='team5499-hooks',
    description='team5499 specific kotlin precommit hooks',
    url='https://github.com/team5499/pre-commit-hooks',
    version='0.3.5',

    packages=find_packages(exclude=('tests*', 'testing*')),
    extras_require={':python_version<"3.5"': ['typing']},
    entry_points={
        'console_scripts': [
            'ktlint-wrapper = team5499-hooks.ktlint-wrapper:main',
            'detekt-wrapper = team5499-hooks.detekt-wrapper:main'
        ],
    },
)
