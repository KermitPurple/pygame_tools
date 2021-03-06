from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name="pygame-tools",
    version='0.0.2',
    author="KermitPurple (Shane McDonough)",
    description='A package to make creating pygame applications much easier',
    long_description_content_type="text/markdown",
    long_description=long_description,
    py_modules=['pygame_tools'],
    package_dir={'': 'src'},
    install_requires=['pygame', 'recordclass'],
    keywords='pygame 2d-game video-game',
    url="https://github.com/KermitPurple/pygame_tools",
    license='MIT',
)
