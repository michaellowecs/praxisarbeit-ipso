import os

from flask import Flask, redirect
from flask_admin import Admin
from flask_basicauth import BasicAuth
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///tenants'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy()
migrate = Migrate(compare_type=True)

# Database init
db.init_app(app)
migrate.init_app(app, db)

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = 'admin'
app.config['BASIC_AUTH_FORCE'] = True

admin = Admin(app, name='Tenant Management', template_mode='bootstrap3')
from apps.admin.views import load_admin_views

load_admin_views()

basic_auth = BasicAuth(app)
config_settings = os.environ.get(
    'APP_SETTINGS', 'apps.config.DevelopmentConfig'
)
app.config.from_object(config_settings)  # imports instance.config
app.config['APP_SETTINGS'] = config_settings
app.config.update(
    SQLALCHEMY_DATABASE_URI=(
        "postgresql://"
        f"{app.config['POSTGRES']['user']}"
        f":{app.config['POSTGRES']['pwd']}"
        f"@{app.config['POSTGRES']['host']}:{app.config['POSTGRES']['port']}"
        f"/{app.config['POSTGRES']['db']}"
    )
)


@app.route('/')
def hello_world():
    return redirect('/admin')


@app.route('/admin')
@basic_auth.required
def admin_view():
    return


if __name__ == '__main__':
    app.run()
