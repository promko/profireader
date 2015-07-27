from flask import Blueprint

general_bp = Blueprint('general', __name__)
user_bp = Blueprint('user', __name__)
article_bp = Blueprint('articles', __name__)
filemanager_bp = Blueprint('filemanager', __name__)
static_bp = Blueprint('static', __name__, static_url_path='')
#static_bp = Blueprint('static', __name__)