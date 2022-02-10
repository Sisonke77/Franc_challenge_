import json
from flask import Flask, render_template, jsonify, Response, request


app = Flask(__name__)

@app.route('/')
def index_view():
    data_posts = {}
    data_users = {}
    username = request.args.get('username')
    with open('./posts.json','r') as f:
        data_posts = json.load(f)
        f.close()
    with open('./users.json','r') as f:
        data_users = json.load(f)
        f.close()
        
       
    return render_template('index.html', username = username, json_data_posts = data_posts, json_data_users = data_users)

@app.route('/users')
def users_view():
    with open('./users.json', 'r') as f:
        users = f.read()
    return Response(users, mimetype="application/json")

@app.route('/posts')
def posts_view():
    with open('./posts.json', 'r') as f:
        posts = f.read()
    return Response(posts, mimetype="application/json")



if __name__ == '__main__':
    app.run(host='127.0.0.1')