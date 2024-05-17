
# CTA Installation Guide

This guide provides step-by-step instructions to install and set up the crypto trading bot on an Ubuntu system.

## Prerequisites

- Python 3.8 or higher
- Git

## Step 1: Clone the Repository

First, clone the repository to your local machine:

```sh
git clone https://github.com/oracleagent/CTA.git
cd CTA
```

## Step 2: Set Up the Virtual Environment

Create a virtual environment to manage your dependencies:

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows, use \`venv\Scripts\activate\`
```

## Step 3: Create the `requirements.txt` File

Create the `requirements.txt` file with the following content:

```plaintext
requests==2.25.1
pandas==1.2.4
SQLAlchemy==1.4.15
APScheduler==3.6.3
ccxt==4.3.23
pytest==6.2.4
python-dotenv==0.17.0
loguru==0.5.3
websocket-client==0.59.0
ujson==4.0.2
web3==5.27.0
```

## Step 4: Install Dependencies

Install the required dependencies using `pip`:

```sh
pip install -r requirements.txt
```

## Step 5: Create the `setup.py` File

Create the `setup.py` file with the following content:

```python
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
        'ccxt==4.3.23',
        'pytest==6.2.4',
        'python-dotenv==0.17.0',
        'loguru==0.5.3',
        'websocket-client==0.59.0',
        'ujson==4.0.2'
        'web3==5.27.0'
    ],
    entry_points={
        'console_scripts': [
            'start-bot=src.main:main',
        ],
    },
)
```

## Step 6: Initialize the Database

Initialize the SQLite database:

```sh
python -m src.db.models
```

## Step 7: Set Up Environment Variables

Create a `.env` file in the root directory of the project and add your API keys and other sensitive information:

```plaintext
BINANCE_API_KEY=your_binance_api_key
BINANCE_SECRET_KEY=your_binance_secret_key
COINBASE_API_KEY=your_coinbase_api_key
COINBASE_SECRET_KEY=your_coinbase_secret_key
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_USER=your-email@example.com
EMAIL_PASSWORD=your-email-password
```

## Step 8: Configure the Bot

Edit the configuration files to suit your needs:

**config/default.json**

```json
{
  "api_keys": {
    "binance": {
      "api_key": "your_binance_api_key",
      "secret_key": "your_binance_secret_key"
    },
    "coinbase": {
      "api_key": "your_coinbase_api_key",
      "secret_key": "your_coinbase_secret_key"
    }
  },
  "trading": {
    "max_risk_per_trade": 0.01,
    "max_daily_risk": 0.05,
    "volatility_threshold": 0.02,
    "base_currency": "USD",
    "quote_currency": "BTC"
  },
  "notifications": {
    "email": {
      "host": "smtp.example.com",
      "port": 587,
      "user": "your-email@example.com",
      "password": "your-email-password",
      "recipient": "recipient@example.com"
    }
  },
  "logging": {
    "level": "INFO",
    "file": "logs/trading.log"
  }
}
```

## Step 9: Run the Bot

Start the bot by running the main script:

```sh
python -m src.main
```

## Optional - Using Docker

If you prefer to use Docker, you can build and run the bot using Docker.

### Create `Dockerfile`

```Dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "src.main"]
```

### Create `docker-compose.yml`

```yaml
version: '3'
services:
  trading-bot:
    build: .
    environment:
      - BINANCE_API_KEY=${BINANCE_API_KEY}
      - BINANCE_SECRET_KEY=${BINANCE_SECRET_KEY}
      - COINBASE_API_KEY=${COINBASE_API_KEY}
      - COINBASE_SECRET_KEY=${COINBASE_SECRET_KEY}
      - EMAIL_HOST=${EMAIL_HOST}
      - EMAIL_PORT=${EMAIL_PORT}
      - EMAIL_USER=${EMAIL_USER}
      - EMAIL_PASSWORD=${EMAIL_PASSWORD}
    volumes:
      - .:/app
    command: ["python", "-m", "src.main"]
```

### Build the Docker Image

```sh
docker build -t trading-bot .
```

### Run the Docker Container

```sh
docker-compose up -d
```

By following these steps, you'll have a properly configured and running crypto trading bot. If you encounter any issues, please let me know!
