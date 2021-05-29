import os

from flask import request, Blueprint, send_from_directory, send_file, make_response

download_db = Blueprint('download_db', __name__)


@download_db.route('/admin/download', methods=['POST', 'GET'])
def file_download():
    filename = request.args.get('filename')
    # filename = '常务委员推荐表.doc'
    from biaodan import app
    dirpath = os.path.join(app.root_path, '../')  # 这里是下在目录，从工程的根目录写起，比如你要下载static/js里面的js文件，这里就要写“static/js”
    return send_from_directory(dirpath, filename, as_attachment=True,
                               mimetype='doc/docx/text')  # as_attachment=True 一定要写，不然会变成打开，而不是下载

# def file_download():
#     filename = request.args.get('filename')
#     dirpath = os.path.join(app.root_path, '../')
#     filename = dirpath + filename
#     response = make_response(send_file(filename))
#     basename = os.path.basename(filename)
#     utf_filename = quote(basename.encode('utf-8'))
#     response.headers["Content-Disposition"] = "attachment;filename*=UTF-8{}".format(utf_filename)
#     response.headers['Content-Type'] = "doc/docx; charset=UTF-8"
#     return response
