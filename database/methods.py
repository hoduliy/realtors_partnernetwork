# Модуль с методами для работы с БД

# Для взаимодействия с БД Postgres
import asyncpg
# Для разбора полученных json
import json

# Создание пула соединений для подключения к БД
async def create_pool(dbConfig):
    return await asyncpg.create_pool(
        host = dbConfig.db_host,
        user = dbConfig.db_user,
        password = dbConfig.db_password,
        database = dbConfig.database,

        min_size=1,
        max_size=2
    )

async def execute_db_func(pool, name: str, params: dict):
    func_info = await pool.fetchrow("SELECT CALL_TYPE, SQL, PARAMS FROM core.db_funcs WHERE UPPER(name) = UPPER($1)", name);

    json_params = json.loads(func_info['params'])

    sql = func_info['sql']

    res = {}

    for el_in in json_params['IN']:
        sql = sql.replace(':' + el_in['name'], str(params[el_in['name']]))
    for el_out in json_params['OUT']:
        res[el_out['name']] = None

    print(sql)
    res_row = await pool.fetchrow(sql)
    for out_param in res_row.items():
        res[out_param[0].upper()] = out_param[1]

    if len(res) == 1:
        print(res[json_params['OUT'][0]['name']])
        return res[json_params['OUT'][0]['name']]
    else:
        return res
    #return False
