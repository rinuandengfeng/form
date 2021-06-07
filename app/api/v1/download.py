import os
import zipfile
from flask import request, Blueprint, send_from_directory, Response

from app.models.data import Data
from app.utils.main import exe_docx

download_bp = Blueprint('download_db', __name__)
download_all_bp = Blueprint('download_all_bp', __name__)


@download_bp.route('/admin/download', methods=['GET', 'POST'])
def file_download():
    id = request.args.get('id')
    name = id + '.docx'
    exe_docx(id)
    from biaodan import app
    dirpath = os.path.join(app.root_path, '../')  # 这里是下在目录，从工程的根目录写起，比如你要下载static/js里面的js文件，这里就要写“static/js”
    return send_from_directory(dirpath, id + '.docx', as_attachment=True,
                               mimetype='doc/docx')  # as_attachment=True 一定要写，不然会变成打开，而不是下载


@download_all_bp.route('/admin/all', methods=['GET'], endpoint='zipball')
def download_all():
    info = []
    limit = request.args.get('limit')
    page = request.args.get('page')
    all = Data.query.limit(limit).all()
    file_list = []
    for i in all:
        info.append(i.id)
    for a in info:
        exe_docx(str(a))
        file_list.append(str(a) + '.docx')
    with zipfile.ZipFile('第' + page + '页.zip', 'w') as zipobj:
        for file in file_list:
            zipobj.write(file)
    from biaodan import app
    dirpath = os.path.join(app.root_path, '../')  # 这里是下在目录，从工程的根目录写起，比如你要下载static/js里面的js文件，这里就要写“static/js”
    return send_from_directory(dirpath, '第' + page + '页.zip', as_attachment=True, mimetype='zip')

