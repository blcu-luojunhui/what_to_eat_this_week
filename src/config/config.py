class Config:
    DEBUG = True

    JWT_SECRET = "my_secret_key"
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRE_SECONDS = 3600

    # MySQL
    MYSQL_DSN = "mysql+aiomysql://user:pass@127.0.0.1:3306/test"

    # Redis
    REDIS_URL = "redis://127.0.0.1:6379/0"

    # Elasticsearch
    ES_HOSTS = ["http://127.0.0.1:9200"]

    # Milvus
    MILVUS_HOST = "127.0.0.1"
    MILVUS_PORT = "19530"
