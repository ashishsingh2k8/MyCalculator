from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from api.myCalculator_V1 import mycalc_blueprint_v1

# Enable swagger integration
SWAGGER_API_URL = '/swagger'
SWAGGER_CONFIG_FILE_PATH = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_API_URL,
    SWAGGER_CONFIG_FILE_PATH,
    config={
        'app_name': "My calculator"
    }
)


app = Flask(__name__)
app.register_blueprint(mycalc_blueprint_v1)
app.register_blueprint(swaggerui_blueprint,
                       url_prefix=SWAGGER_API_URL)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
