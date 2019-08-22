import os
import re
from setuptools import find_packages, setup


pkgname = 'ffmpeg_rpc'


def get_version(dirname=pkgname):
    filepath = os.path.join(dirname, 'version.py')
    with open(filepath, 'r') as fp:
        __version__, = re.findall('__version__ = "(.*)"', fp.read())

    return __version__


def package_files(directories):
    if isinstance(directories, str):
        directories = [directories]
    paths = []
    for directory in directories:
        for (path, directories, filenames) in os.walk(directory):
            for filename in filenames:
                paths.append(os.path.join('..', path, filename))
    return paths

data_files = [
]

package_data = [
]


# Currently using symlinks to make directory structure look more like a package
# since package_dir is not behaving properly with pip -e.
packages = find_packages(exclude=['src', 'src.*'])
print('<Packages>:', packages)

# common dependencies
# todo: fully test unified dependencies
deps = [
    'grpcio>=1.22',
    'protobuf',
    'spaghetr'
]


setup(
    name=pkgname,
    version=get_version(),
    script_name='setup.py',
    python_requires='>3.5',
    install_requires=deps,
    zip_safe=False,
    packages=[pkgname],
    data_files=data_files,
    include_package_data=True,
    extras_require={
    }
)
