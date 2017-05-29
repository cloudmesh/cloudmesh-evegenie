"""
evegenie setup.

Provided by Gregor von Laszewski
laszewski@gmail.com

"""
from setuptools import find_packages, setup
import io


def readfile(filename):
    """
    Read a file
    :param filename: name of the file
    :return: returns the content of the file as string
    """
    with io.open(filename, encoding="utf-8") as stream:
        return stream.read().split()


requiers = """
cloudmesh.common
eve
docopt
""".split("\n")

# dependency_links = ['http://github.com/nicolaiarocci/eve.git@develop']

version = readfile("VERSION")[0].strip()
readme = readfile('README.md')

NAME = "cloudmesh.evegenie"
DESCRIPTION = "A dynamic extensible CMD based command shell"
AUTHOR = "frodopwns, ultimateboy, nicolaiarocci, laszewsk"
AUTHOR_EMAIL = "laszewski@gmail.com" # replace with yours
URL = "https://github.com/cloudmesh/evegenie" # replace with yours
LONG_DESCRIPTION = "\n".join(readme)

setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    version=version,
    license="Apache 2.0",
    url=URL,
    packages=find_packages(),
    include_package_data=True,
    #package_data={
    #    "evegenie": [
    #        "templates/settings.py.j2",
    #    ]
    #},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    install_requires=requiers,
    tests_require=[
        "flake8",
        "coverage",
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'evegenie = cloudmesh.geneve:main',
        ],
    },
    namespace_packages=['cloudmesh'],
)
