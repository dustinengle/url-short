
import random
import string

from flask import Flask, request
from redis import Redis

app = Flask(__name__)
# Cache is name of docker-compose service
r = Redis(host='cache', port=6379)

# Generate a random string using letters and digits of defined length
def gen_id(len=6, chars=string.ascii_letters+string.digits):
    return ''.join(random.choices(chars, k=len))

# Take in the provided id and return the URL from Redis
@app.route('/<id>', methods=['GET'])
def get_url(id):
    url = r.get(id)
    return url

# Take in the URL query parameter, make a random id, and set in Redis
# Return the resulting shortened URL
@app.route('/n', methods=['GET'])
def post_url():
    id = gen_id()
    r.set(id, request.args.get('url'))
    host = request.base_url.replace('/n', '')
    return f'{host}/{id}'

# Run the Flask server if the script has been executed.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
