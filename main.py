import time
import os
from sanic import Sanic
from sanic.response import json
from hazm import Normalizer

app = Sanic()

normalizer = Normalizer()

def normalize(text):
    start_time = time.time()
    normalized = normalizer.normalize(text)
    took = round(time.time() - start_time, 4)
    return took, normalized

@app.route('/')
async def index_handler():
    return json({'hello': 'world'})

@app.route('/normalize')
async def normalize_handler(request):
    text = request.args.get('text')
    if not text:
        return json({
            'error': 'no "text" querystring parameter passed'
        }, 406)

    took, normalized = normalize(text)

    return json({
        'took': took,
        'normalized': normalized
    })

if __name__ == '__main__':
    app.run(host=os.getenv('HOST', '0.0.0.0'), port=os.getenv('PORT', 8000))
