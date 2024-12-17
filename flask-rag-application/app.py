from flask import Flask
from ingestion import ingestion_blueprint
from qa import qa_blueprint
from selection import selection_blueprint

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(ingestion_blueprint, url_prefix='/ingestion')
    app.register_blueprint(qa_blueprint, url_prefix='/qa')
    app.register_blueprint(selection_blueprint, url_prefix='/selection')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
