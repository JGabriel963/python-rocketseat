from src.data.product_finder import ProductFinder
from src.models.redis.repository.redis_repository import RedisRepository
from src.models.redis.settings.connection import redis_connection_handler
from src.models.sqlite.repository.products_repository import ProductsRepository
from src.models.sqlite.settings.connection import db_connection_handler


def product_finder_composer():
    redis_conn = redis_connection_handler.get_connection()
    sqlite_conn = db_connection_handler.get_connection()

    redis_repo = RedisRepository(redis_conn)
    products_repo = ProductsRepository(sqlite_conn)

    product_finder = ProductFinder(redis_repo, products_repo)
    return product_finder
