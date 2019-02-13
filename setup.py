from setuptools import find_packages
from setuptools import setup


setup(
    name='team5499_hooks',
    description='team5499 specific kotlin precommit hooks',
    url='https://github.com/team5499/pre-commit-hooks',
    version='0.3.10',

    packages=find_packages(),
    package_data={'team5499_hooks': ['team5499_hooks/detekt-wrapper.bat',
                                        'team5499_hooks/detekt-wrapper.sh'
                                        'team5499_hooks/ktlint-wrapper.bat'
                                        'team5499_hooks/ktlint-wrapper.sh']},
    include_package_data=True,
    extras_require={':python_version<"3.5"': ['typing']},
    entry_points={
        'console_scripts': [
            'ktlint_wrapper = team5499_hooks.ktlint_wrapper:main',
            'detekt_wrapper = team5499_hooks.detekt_wrapper:main'
        ],
    },
)
