import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='anvil-parser-d2',
    version='1.0.2',
    author='SyndiShanX',
    description='A Minecraft Anvil File Format Parser - Fixes for 1.18+ - Dungeons II Support',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SyndiShanX/Anvil-Parser-Dungeons-II',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'nbt',
        'frozendict',
    ],
    include_package_data=True
)
