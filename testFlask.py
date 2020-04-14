from flask import Flask
#
app = Flask(__name__)

# route装饰器可以用于将URL绑定到指定的函数
@app.route('/abc')
def hello_world():
    return 'abc!'

# route装饰器可以用于将URL绑定到指定的函数
@app.route('/abc/<name>')
def hello_string(name):
    return 'abc %s!' % name

# route装饰器可以用于将URL绑定到指定的函数
@app.route('/abc/<int:postID>')
def hello_postID(postID):
    return 'abc %d!' % postID

# route装饰器可以用于将URL绑定到指定的函数
@app.route('/abc/<float:revNo>')
def hello_revNo(revNo):
    return 'abc %f!' % revNo


# app.add_url_rule()也可以用于将URL绑定到指定的函数
app.add_url_rule('/wq', 'hello', hello_world)

# host可设置为0.0.0.0，以使得服务器在外部可用
if __name__ == '__main__':
    app.run('127.0.0.1', 5000, True)  # host,port,debug,options
