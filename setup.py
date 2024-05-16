from setuptools import setup, find_packages

setup(
    name='CryptoTradingBot',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'requests',
        'apscheduler',
        'dash',
        'plotly',
        'pymongo',
        'flask',
        'sqlalchemy'
    ],
    entry_points={
        'console_scripts': [
            'run-trading-bot=src.main:main',
        ],
    },
    python_requires='>=3.6',
    author='Your Name',
    author_email='your.email@example.com',
    description='A sophisticated crypto trading bot capable of trading multiple cryptocurrencies.',
    keywords='crypto trading bot',
    url='http://example.com/YourProjectHomePage',
    project_urls={
        'Documentation': 'http://example.com/YourProjectDocumentation',
        'Source': 'http://github.com/yourusername/yourproject',
        'Tracker': 'http://github.com/yourusername/yourproject/issues',
    }
)
