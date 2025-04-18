import os
from urllib.parse import quote_plus

def get_database_config():
    """
    Get database configuration from environment variables.
    Uses RDS Proxy for connection pooling.
    """
    DB_USER = os.environ.get('DATABASE_USER', 'admin')
    DB_PASSWORD = os.environ.get('DATABASE_PASSWORD', '')
    DB_HOST = os.environ.get('DATABASE_HOST')  # RDS Proxy endpoint
    DB_PORT = os.environ.get('DATABASE_PORT', '5432')
    DB_NAME = os.environ.get('DATABASE_NAME', 'product_management')

    # Encode special characters in password
    encoded_password = quote_plus(DB_PASSWORD)

    config = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': DB_NAME,
            'USER': DB_USER,
            'PASSWORD': encoded_password,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
            'OPTIONS': {
                'sslmode': 'require',  # Enforce SSL for RDS connections
            },
        }
    }

    return config
