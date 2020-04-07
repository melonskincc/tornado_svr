from abc import ABC
from models.user_models import tbl_user
from tornado.web import RequestHandler
import logging

logger = logging.getLogger('abc')


class BaseHandler(RequestHandler, ABC):
    def initialize(self, mysql, redis):
        self.db = mysql
        self.redis = redis


class IndexHandler(BaseHandler, ABC):
    __endpoint__ = 'index'

    async def get(self):
        self.write('Index!!!')
        with await self.redis as redis_conn:
            print(await redis_conn.get('a'))
            print(await redis_conn.hset('s', 'b', 'y'))
        async with self.db.acquire() as conn:
            # tran = await conn.begin()
            # ret = await conn.execute(tbl_user.insert().values(name='a'))
            # ret = await conn.execute(tbl_user.insert().values(name='b'))
            # ret1 = await conn.execute(tbl_user.insert().values(name='c'))
            ret = await conn.execute(tbl_user.select())
            print(ret)
            ret = await ret.fetchall()
            for x in ret:
                print(x)

            # await tran.commit()
        return self.finish()
