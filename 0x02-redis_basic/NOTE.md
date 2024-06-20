## REDIS crash course


### Essential REDIS commands

```sh
SET key value
MSET key1 value1 . . . keyN valueN
APPEND key value  # Will append value to previous value of key
GET key
RENAME keyName newKeyName
DEL key
EXISTS key

KEYS *
FLUSHALL

QUIT/EXIT
```

### Increment/Decrement a number

```sh
INCR key  # For Integer values
DECR key  # For Integer values
```

### key expiration/persistency

```sh
TTL key
EXPIRE key duration
PERSIST key  # nullify expiration
SETEX key duration value
```

### set an expirable key

```sh
SETEX key duration value
```

### Working with Lists

```sh
LPUSH/RPUSH listName value
LINSERT listName BEFORE 'listMember' 'newMember'
LRANGE names 0 -1
LLEN listName

LPOP/RPOP listName
```

### Working with hash sets

```sh
SADD setName setMember
SMEMBERS setName
SISMEMBER setName key
SREM setName setMember
SMOVE setA setB key
SCLEAR
```


### Working with sorted set



### Working with hash maps

```sh
HSET hmapName key value
HGET hmapName key
HGETALL hmapName
HDEL hmapName KEY
HEXISTS hmapName key
```
