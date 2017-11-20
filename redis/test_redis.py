#coding: utf-8

import redis

r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    password='')

r.set('foo', 'bar')
value = r.get('foo')
print(value)

r.set('counter', 5)
r.incr('counter')
r.incr('counter')
r.decr('counter')
value = r.get('counter')
print(value)

rc = r.rpush('numeros', 'um')
rc = r.rpush('numeros', 'dois')
rc = r.rpush('numeros', 'três')
rc = r.rpush('numeros', 'quatro')
print(r.llen('numeros'))
print(r.lindex('numeros', 3))

print(r.keys())
rc = r.delete('foo')
rc = r.delete('counter')
rc = r.delete('numeros')
print(r.keys())










