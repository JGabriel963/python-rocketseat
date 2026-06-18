import redis

redis_conn = redis.Redis(host="localhost", port=6379, db=0)

redis_conn.set("chave_1", "algum_valor")

meu_valor = redis_conn.get("chave_1").decode("utf-8")

# delete de dados
redis_conn.delete("chave_1")

## commands para hash
redis_conn.hset("meu_hash", "nome", "joao")

meu_hash = {  # chave de exemploe
    "nome": "joao",  # field: values
    "idade": 30,
    "cidade": "sao paulo",
}
redis_conn.hset("meu_hash", "nome", "joao")
redis_conn.hset("meu_hash", "idade", "30")
redis_conn.hset("meu_hash", "cidade", "curitiba")

valor_1 = redis_conn.hget("meu_hash", "nome").decode("utf-8")

redis_conn.hdel("meu_hash", "cidade")

# buscas por existência
elem = redis_conn.exists("chave_1")
print(elem)

elem2 = redis_conn.hexists("meu_hash", "nome")
print(elem2)

## dados -> TTL -> Time To Live [segundos]
## Expiração de dados
redis_conn.set("cheve_del", "valor_del", 12)
redis_conn.expire("meu_hash", 30)
