from flask import Flask
from config import Config
from .extensions import db, migrate, login_manager, mail
import os

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # 初始化扩展
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)
    
    # 确保上传文件夹存在
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # 注册蓝图
    from routes.auth import auth_bp
    from routes.main import main_bp
    from routes.api import api_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # 上下文处理器
    @app.context_processor
    def inject_variables():
        from models import TeamMember, Event
        members = TeamMember.query.filter_by(is_active=True).all()
        upcoming_events = Event.query.filter(
            Event.is_published == True,
            Event.start_time >= datetime.utcnow()
        ).order_by(Event.start_time.asc()).limit(3).all()
        return dict(
            team_members=members,
            upcoming_events=upcoming_events
        )
    
    # 错误处理
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('errors/500.html'), 500
    
    return app