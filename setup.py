from setuptools import setup, find_packages

setup(
    name='myusps',
    version='1.3.2',
    description='Python 3 API for USPS Informed Delivery, a way to track packages and mailpieces.',
    url='https://github.com/happyleavesaoc/python-myusps/',
    license='MIT',
    author='happyleaves',
    author_email='happyleaves.tfr@gmail.com',
    packages=find_packages(),
    install_requires=['lxml==5.2.2', 'python-dateutil==2.9.0.post0', 'requests>=2.32.3', 'requests-cache==1.2.1',
                      'playwright==1.44.0'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ]
)
