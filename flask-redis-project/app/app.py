from flask import flask 
import REDIS_HOST

APP =FLASK(_name_)
r = redis.Redis(host='redis' , port=6379)

@app.route('/')
def welcome(): 
    return 'welcome to your mo to your first container compose'

@app.route('/count')
def count():
    count = r.incr('visits')
    return f'this page has been visited {count} times.'

if __name__ == "_main_":
    app.run(host='0.0.0.0', port 5002)