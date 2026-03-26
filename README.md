# Binance Futures Testnet Trading Bot

## Setup

1. Create Binance Testnet account
2. Generate API Key & Secret
3. Create .env file:

API_KEY=D2DAHLmkJejCrekhse1o7xupgiHSLeFrfilOUHxOGShiwmJauPX3TTBcF2PRfBg1
API_SECRET=QdwwIdr81qzhFYTweVv2tlKW4IchjFLZTrPKL6UnZ7qeMZIVeCmQw3i05q2h6324

4. Install requirements:
pip install -r requirements.txt

## Run

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 30000

## Features
- Market & Limit Orders
- CLI input
- Logging
- Error handling