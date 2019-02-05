import os

from setuptools import find_packages, setup

if __name__ == '__main__':
    this_directory = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(this_directory, 'docs', 'README.md')) as f:
        long_description = f.read()
    tests_require = ['pytest-sugar', 'pytest-cov', 'pytest-localserver']
    setup(
        name='ecnunetwork',
        description='A script to connect to Internet at East China Normal University (ECNU).',
        keywords="ecnu", url='https://github.com/njzjz/ecnunetwork',
        author='Jinzhe Zeng', author_email='jzzeng@stu.ecnu.edu.cn',
        packages=find_packages(),
        install_requires=['requests'],
        entry_points={
            'console_scripts':
            ['ecnunetwork=ecnunetwork.commandline:main',
             'network=ecnunetwork.commandline:main']},
        setup_requires=['setuptools_scm', 'pytest-runner'],
        use_scm_version=True,
        classifiers=[
            "Natural Language :: English",
            "Operating System :: POSIX :: Linux",
            "Operating System :: Microsoft :: Windows",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Software Development :: Version Control :: Git",
        ],
        zip_safe=True,
        long_description=long_description,
        long_description_content_type='text/markdown',
        tests_require=tests_require,
        extras_require={
            "test": tests_require,
        },
    )
