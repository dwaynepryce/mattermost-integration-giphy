import os
from setuptools import setup
from setuptools import find_packages


VERSION = "0.1.0"  # let's make this easier on ourselves to start with, shall we?
README = os.path.join(os.path.dirname(__file__), 'README.md')


setup(
    name='mattermost_giphy',
    version=VERSION,
    description="Giphy Integration Service for Mattermost.",
    long_description=README,
    classifiers=[],
    author='Dwayne',
    author_email='mattermost-giphy@dwayne.pryce.io',
    url='https://github.com/numberly/mattermost-integration-giphy',
    license='APLv2',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'requests',
    ]
)
