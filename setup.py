from setuptools import setup, find_packages

setup(
    name='CTA',
    version='1.0.0',
    description='Crypto Trading Agent',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests==2.25.1',
        'pandas==1.2.4',
        'SQLAlchemy==1.4.15',
        'APScheduler==3.6.3',
        'ccxt==1.42.75',
        'pytest==6.2.4',
        'python-dotenv==0.17.0',
        'loguru==0.5.3',
        'websocket-client==0.59.0',
        'ujson==4.0.2'
    ],
    entry_points={
        'console_scripts': [
            'start-bot=src.main:main',
        ],
    },
)
