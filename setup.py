
from setuptools import setup, find_packages

setup(
    name='ghasedak_sms',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    description='Python package for Ghasedak SMS API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ghasedak Developers Team',
    author_email='hasheminasab97@gmail.com',
    url='sms.ghasedak.me',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.6',
    include_package_data=True,
    package_data={
        '': ['README.md'],
    },
    # project_urls={
    #     'Documentation': 'https://github.com/yourusername/ghasedak_sms#readme',
    #     'Source': 'https://github.com/yourusername/ghasedak_sms',
    #     'Tracker': 'https://github.com/yourusername/ghasedak_sms/issues',
    # },
)
