
# Example Configuration Files

This document provides example configuration files to help you set up your trading bot. 

## Default Configuration

The default configuration file (`config/default.json`) contains general settings that apply to most environments. Below is an example of a default configuration file:

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

### Explanation of Default Configuration

- **API Keys**: Contains the API keys for Binance and Coinbase. Replace `"your_binance_api_key"` and `"your_binance_secret_key"` with your actual Binance API credentials, and do the same for Coinbase.
- **Trading Settings**:
  - `max_risk_per_trade`: Maximum risk per trade as a fraction of the portfolio.
  - `max_daily_risk`: Maximum total risk per day.
  - `volatility_threshold`: Threshold for adjusting trading parameters based on market volatility.
  - `base_currency`: The currency used for trading (e.g., "USD").
  - `quote_currency`: The currency being traded (e.g., "BTC").
- **Notifications**:
  - **Email Settings**: Configure the SMTP settings for sending email notifications. Replace with your email provider's settings.
- **Logging**:
  - `level`: The logging level (e.g., "INFO").
  - `file`: The log file path.

## Production Configuration

The production configuration file (`config/production.json`) contains settings optimized for a production environment. Below is an example of a production configuration file:

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
    "max_risk_per_trade": 0.005,
    "max_daily_risk": 0.03,
    "volatility_threshold": 0.015,
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
    "level": "ERROR",
    "file": "logs/production.log"
  },
  "database": {
    "url": "sqlite:///trading_bot.db"
  }
}
```

### Explanation of Production Configuration

- **API Keys**: Same as the default configuration, but ensure they are set for a secure production environment.
- **Trading Settings**:
  - `max_risk_per_trade`: Lower risk per trade compared to default for a more conservative approach.
  - `max_daily_risk`: Lower daily risk limit.
  - `volatility_threshold`: Adjusted for production to react to market conditions more conservatively.
- **Notifications**: Same as the default configuration.
- **Logging**:
  - `level`: Set to "ERROR" to reduce log verbosity in production.
  - `file`: Log file path for production logs.
- **Database**:
  - `url`: Database URL for connecting to the production database.

## Custom Configuration

You can create custom configurations for different environments or testing purposes. Below is an example of a custom configuration file (`config/custom.json`):

```json
{
  "api_keys": {
    "binance": {
      "api_key": "custom_binance_api_key",
      "secret_key": "custom_binance_secret_key"
    },
    "coinbase": {
      "api_key": "custom_coinbase_api_key",
      "secret_key": "custom_coinbase_secret_key"
    }
  },
  "trading": {
    "max_risk_per_trade": 0.02,
    "max_daily_risk": 0.07,
    "volatility_threshold": 0.03,
    "base_currency": "USD",
    "quote_currency": "ETH"
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
    "level": "DEBUG",
    "file": "logs/custom.log"
  },
  "database": {
    "url": "sqlite:///custom_trading_bot.db"
  }
}
```

### Explanation of Custom Configuration

- **API Keys**: Custom API keys for different environments or testing.
- **Trading Settings**: Adjusted trading parameters for custom scenarios.
- **Notifications**: Same as the default configuration.
- **Logging**:
  - `level`: Set to "DEBUG" for more detailed logs during testing.
  - `file`: Log file path for custom logs.
- **Database**: Custom database URL for testing or different environments.

## Conclusion

Use these example configurations as a starting point and adjust the settings to fit your specific requirements. Ensure that sensitive information such as API keys and email credentials are kept secure.

Refer to the [setup guide](setup.md) for detailed instructions on how to use these configuration files and get your trading bot up and running.
