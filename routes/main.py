from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import Post, Comment, TeamMember, Event, GalleryImage
from extensions import db
from datetime import datetime

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/team')
def team():
    members = TeamMember.query.filter_by(is_active=True).all()
    return render_template('team.html', members=members)

@main_bp.route('/events')
def events():
    page = request.args.get('page', 1, type=int)
    events = Event.query.filter_by(is_published=True)\
        .order_by(Event.start_time.desc())\
        .paginate(page=page, per_page=6)
    return render_template('events.html', events=events)

@main_bp.route('/event/<int:event_id>')
def event_detail(event_id):
    event = Event.query.get_or_404(event_id)
    return render_template('event_detail.html', event=event)

@main_bp.route('/gallery')
def gallery():
    images = GalleryImage.query.filter_by(is_featured=True).all()
    return render_template('gallery.html', images=images)

@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # 处理联系表单提交
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # 这里可以添加发送邮件的逻辑
        flash('感谢您的留言，我们会尽快与您联系！', 'success')
        return redirect(url_for('main.contact'))
    
    return render_template('contact.html')

# 管理员路由
@main_bp.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash('您没有访问此页面的权限', 'danger')
        return redirect(url_for('main.index'))
    
    return render_template('admin/dashboard.html')