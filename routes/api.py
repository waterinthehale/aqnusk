from flask import Blueprint, jsonify, request
from models import TeamMember, Event, GalleryImage
from extensions import db

api_bp = Blueprint('api', __name__)

@api_bp.route('/team-members', methods=['GET'])
def get_team_members():
    members = TeamMember.query.filter_by(is_active=True).all()
    return jsonify([{
        'id': member.id,
        'name': member.name,
        'position': member.position,
        'bio': member.bio,
        'image': member.image
    } for member in members])

@api_bp.route('/events', methods=['GET'])
def get_events():
    events = Event.query.filter_by(is_published=True).all()
    return jsonify([{
        'id': event.id,
        'title': event.title,
        'description': event.description,
        'location': event.location,
        'start_time': event.start_time.isoformat(),
        'end_time': event.end_time.isoformat() if event.end_time else None,
        'image': event.image
    } for event in events])

@api_bp.route('/gallery', methods=['GET'])
def get_gallery_images():
    images = GalleryImage.query.filter_by(is_featured=True).all()
    return jsonify([{
        'id': image.id,
        'title': image.title,
        'description': image.description,
        'image_path': image.image_path
    } for image in images])

@api_bp.route('/contact', methods=['POST'])
def handle_contact():
    data = request.get_json()
    # 这里可以添加处理联系表单的逻辑
    return jsonify({'message': '感谢您的留言，我们会尽快与您联系！'}), 200