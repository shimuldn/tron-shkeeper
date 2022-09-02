import os
from decimal import Decimal

config = {

    'DEBUG': os.environ.get('DEBUG', False),
    'DATABASE': os.environ.get('DATABASE', 'data/database.db'),

    'REDIS_HOST': os.environ.get('REDIS_HOST', 'localhost'),
    'EVENT_SERVER_HOST': os.environ.get('EVENT_SERVER_HOST', 'events.tron.shkeeper.io'),
    'FULLNODE_URL': os.environ.get('FULLNODE_URL', 'http://fullnode.tron.shkeeper.io'),
    'SOLIDITYNODE_URL': os.environ.get('SOLIDITYNODE_URL', 'http://soliditynode.tron.shkeeper.io'),
    'TRON_NODE_USERNAME': os.environ.get('TRON_NODE_USERNAME', 'shkeeper'),
    'TRON_NODE_PASSWORD': os.environ.get('TRON_NODE_PASSWORD', 'tron'),

    'API_USERNAME': os.environ.get('BTC_USERNAME', 'shkeeper'),
    'API_PASSWORD': os.environ.get('BTC_PASSWORD', 'shkeeper'),
    'SHKEEPER_KEY': os.environ.get('SHKEEPER_BACKEND_KEY', 'shkeeper'),
    'SHKEEPER_HOST': os.environ.get('SHKEEPER_HOST', 'localhost:5000'),

    'TX_FEE': Decimal(os.environ.get('TX_FEE', 10)),
    'TX_FEE_LIMIT': Decimal(os.environ.get('TX_FEE_LIMIT', 5)),

    'TOKENS': {
        'USDT': {'contract_address': 'TXLAQ63Xg1NAzckPwKHvzw7CSEmLMEqcdj'},
    },

}
