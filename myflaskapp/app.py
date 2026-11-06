from flask import Flask, jsonify, request
from config import config_by_name

def create_app(config_name: str = 'default') -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    register_routes(app)
    return app

def register_routes(app: Flask):
    @app.route('/')
    def index():
        return "<h1>Вітаємо у Flask-додатку!</h1><p><a href='/about'>Про додаток</a> | <a href='/api/info'>API Info</a></p>"

    @app.route('/about')
    def about():
        return "<h1>Про додаток Flask</h1><p>Практична робота №5</p>"

    @app.route('/api/info')
    def api_info():
        routes = [rule.rule for rule in app.url_map.iter_rules() if not rule.rule.startswith('/static')]
        return jsonify({
            'framework': 'Flask',
            'version': '3.x',
            'debug': app.config['DEBUG'],
            'registered_routes': routes
        })

    @app.route('/greet')
    @app.route('/greet/<name>')
    def greet(name=None):
        if not name:
            name = request.args.get('name', 'Гість')
        return f"<h1>Вітаємо, {name}!</h1>"

if __name__ == '__main__':
    application = create_app('development')
    application.run(debug=True, port=5000)