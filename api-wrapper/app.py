from chalice import Chalice, Response
from urllib import request
app = Chalice(app_name='api-wrapper')

EC2_IP = 'xxx.xxx.xxx.xxx'
HEADERS = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'
}

@app.route('/index', methods=['GET'], cors=False)
def roi_attrs():    
    e = app.current_request.to_dict()
    params = e.get('query_params')
    param = params.get('param')
    url = 'http://%s/api/index?param=%s' %(EC2_IP, param)
    with request.urlopen(url) as response:
        res = response.read()
    return Response(body=res,
            headers=HEADERS,
            status_code=200)