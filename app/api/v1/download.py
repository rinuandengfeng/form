import os

from flask import request, Blueprint, send_from_directory

from app.utils.main import exe_docx

download_db = Blueprint('download_db', __name__)


@download_db.route('/admin/download', methods=['GET'])
def file_download():
    name = request.args.get('name')
    exe_docx(name)
    from biaodan import app
    dirpath = os.path.join(app.root_path, '../')  # 这里是下在目录，从工程的根目录写起，比如你要下载static/js里面的js文件，这里就要写“static/js”
    return send_from_directory(dirpath, name + '常务委员推荐表.docx', as_attachment=True,
                               mimetype='doc/docx')  # as_attachment=True 一定要写，不然会变成打开，而不是下载
