from flask import Flask
from flask import request
import json
import db

app = Flask(__name__)

@app.route('/health')
def health():
    '''
    @return http server health info
    '''
    return json.dumps({'code': 0,\
                       'msg': "server is ok",\
                       'data': {"version":"0.1", "update_date":"2019-12-10"}})


@app.route('/')
def hello_world():
    '''
    @return home page
    '''
    return 'welcome to Lockheed Corporation!'

@app.route('/query_airplane', methods=['POST'])
def query():
    '''
    @return airplane info
    '''
    datas = request.form.get("data", None)
    if not datas:
        datas = request.get_json(force=True)
    else:
        datas = json.loads(datas)
    app.logger.info('request params: {}'.format(json.dumps(datas, ensure_ascii=False)))
    aireplane_id = datas.get('aireplane_id', 0)

    # mock: search db get Lockheed Corporation aireplane info    
    airplane_name = db.search_db(aireplane_id)
    code = 1
    msg = "welcome to Lockheed Corporation!"
    data = {"aireplane_id":aireplane_id, "airplane_name":airplane_name}
    if airplane_name is None:
        code = 1
        msg = 'sorry, can not search ' + str(aireplane_id) +' airplane'
        data = {}
    
    app.logger.info('search db data is {}'.format(airplane_name))
    return json.dumps({'code': code,\
                       'msg': msg,\
                       'data': data})


if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')
