"""
Installation:
    pip install git+https://github.com/alpha-xone/xzero.git

Pypi:
    # Presetup
    pip install requirements-parser
"""

from setuptools import setup, find_packages
from os import path
from io import open

CUR_PATH = path.abspath(path.dirname(__file__))


def parse_version(package):

    init_file = path.join(CUR_PATH, package, '__init__.py')
    with open(init_file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            if '__version__' in line:
                return line.split('=')[1].strip().replace("'", '')
    return ''


def parse_description():
    """
    Parse the description in the README file
    """
    readme_file = path.join(CUR_PATH, 'README.md')
    if path.exists(readme_file):
        with open(readme_file, 'r', encoding='utf-8') as f:
            long_description = f.read()
        return long_description
    return ''


def parse_requirements(file_name):
    """
    pip install requirements-parser
    fname='requirements.txt'
    """
    import requirements

    from os.path import dirname, join, exists
    require_path = join(dirname(__file__), file_name)
    if exists(require_path):
        with open(require_path, 'r') as file:
            requires = list(requirements.parse(file))
            return [r.name for r in requires]
    return []


version = parse_version('xzero')

if __name__ == '__main__':

    setup(
        name='xzero',
        version=version,
        license='Apache 2',
        description='python backtest toolkit',
        long_description=parse_description(),
        long_description_content_type='text/markdown',
        url='https://github.com/alpha-xone/xzero',
        author='Alpha',
        keywords='python backtest trading',
        packages=find_packages(exclude=['contrib', 'docs', 'tests']),
        install_requires=parse_requirements('requirements.txt'),
        extras_require=dict(
            all=parse_requirements('optional-requirements.txt')
        ),
        # extras_require=dict(dev=[], test=[],),
        # package_data=dict(sample=[]),
        # data_files=[('my_data', ['data/data_file'])],
        # entry_points=dict(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
        ],
    )
