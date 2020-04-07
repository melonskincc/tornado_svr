import asyncio
from logging.config import dictConfig
from conf.settings import *
import tornado.ioloop
import tornado.web
import uvloop, aioredis
from tornado.httpserver import HTTPServer
from aiomysql import sa
# from aiomysql.cursors import DictCursor
from handlers.user_handler import IndexHandler


async def init_engine():
    try:
        return await sa.create_engine(**DB, autocommit=True, echo=True,
                                      charset='utf8'), await aioredis.create_redis_pool(
            REDIS_ADDR, maxsize=20, encoding='utf-8')
    except Exception as e:
        print(repr(e))
        exit(1)


def init_log():
    dictConfig(LOGGING)


def make_app():
    mysql, redis = tornado.ioloop.IOLoop.current().run_sync(init_engine)
    return tornado.web.Application([
        (r'/', IndexHandler, dict(mysql=mysql, redis=redis))
    ],
        **SETTINGS
    )


def serve():
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    tornado.settings = SETTINGS
    init_log()
    app = make_app()
    server = HTTPServer(app)
    server.bind(port=PORT, address=HOST)
    server.start(1)  # forks one process per cpu,windows上无法fork,这里默认为1
    sys.stdout.write(f"Start server at:http://{HOST}:{PORT} \n")
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    serve()
