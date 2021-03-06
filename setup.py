from setuptools import setup

setup(
    name='PerSAK',
    version='0.2.0',
    packages=[],
    url='https://github.com/enrico-laboratory/PerSAK',
    license='MIT',
    author='Enrico Ruggieri',
    author_email='',
    description='A collection of scripts which are executed via this CLI app',
    install_requires=[
        'click','libvirt-python', 'python-dotenv'
    ],
    entry_points='''
        [console_scripts]
        persak=persak:cli
    '''
)
