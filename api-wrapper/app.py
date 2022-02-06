from chalice import Chalice, Response, CORSConfig
from urllib import request
app = Chalice(app_name='api-wrapper')

EC2_IP = '127.0.0.1:8000' # local
HEADERS = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'
}

cors_config = CORSConfig(
    allow_origin='*',
    allow_headers=['*'],
    max_age=3600,
    expose_headers=['*'],
    allow_credentials=True
)

@app.route('/index', methods=['GET'], cors=cors_config)
def roi_attrs():    
    e = app.current_request.to_dict()
    params = e.get('query_params')
    data = params.get('data')
    url = 'http://%s/index?data=%s' %(EC2_IP, data)
    print(url)
    with request.urlopen(url) as response:
        res = response.read()
    return Response(body=res,
            status_code=200)