import os
import zipfile
from flask import request, Blueprint, send_from_directory, Response

from app.models.data import Data
from app.utils.main import exe_docx

download_bp = Blueprint('download_db', __name__)
download_all_bp = Blueprint('download_all_bp', __name__)
download_page_bp = Blueprint('download_page_bp', __name__)


@download_bp.route('/admin/download', methods=['GET', 'POST'])
def file_download():
    id = request.args.get('id')
    mes = Data.query.filter_by(id=id).first()
    exe_docx(id)
    from biaodan import app
    dirpath = os.path.join(app.root_path, '../')  # 这里是下在目录，从工程的根目录写起，比如你要下载static/js里面的js文件，这里就要写“static/js”
    return send_from_directory(dirpath, str(id) + str(mes.name) + '.docx', as_attachment=True,
                               mimetype='doc/docx')  # as_attachment=True 一定要写，不然会变成打开，而不是下载


@download_page_bp.route('/admin/all', methods=['POST'], endpoint='zipball')
def download_page():
    info = []
    data = request.args
    page = data['page']
    all = Data.query.filter().paginate(int(page), int(10))
    # all = Data.query.all()
    all_items = all.items
    file_list = []
    for i in all_items:
        info.append(str(i.id))
    for a in info:
        exe_docx(a)
    for b in all_items:
        file_list.append(str(b.id) + str(b.name) + '.docx')
    with zipfile.ZipFile('第' + page + '页.zip', 'w') as zipobj:
        for file in file_list:
            zipobj.write(file)
    from biaodan import app
    dirpath = os.path.join(app.root_path, '../')  # 这里是下在目录，从工程的根目录写起，比如你要下载static/js里面的js文件，这里就要写“static/js”
    return send_from_directory(dirpath, '第' + page + '页.zip', as_attachment=True, mimetype='zip')

# 下载所有的文件
@download_all_bp.route('/admin/download_all', methods=['POST'])
def downlocd_all():

    from biaodan import app
    dirpath = os.path.join(app.root_path, '../')  # 这里是下在目录，从工程的根目录写起，比如你要下载static/js里面的js文件，这里就要写“static/js”
    return send_from_directory(dirpath, 'all.zip', as_attachment=True, mimetype='zip')
