1.模型类使用sqlalchemy
2.aiomysql可能还有很对问题有待官方解决，不支持多DictCursor...
3.aiomysql的result,返回的结果不支持async for row in conn.execute(tbl.select()) **可能换成aiopg会是完美使用pg数据库
4.orm迁移使用的是alembic     
    *4.1 alembic init 'script name'  初始化一个迁移脚本
    *4.2 alembic revision --autogenerate -m "Added account table" 自动生成迁移文件
    *4.3 alembic upgrade +1/-1 迁移/回滚 
    *4.4 alembic upgrade head   指定版本迁移/回滚