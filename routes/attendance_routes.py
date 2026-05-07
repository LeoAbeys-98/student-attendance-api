from flask import Blueprint
from controllers.attendance_controller import get_attendance, mark_attendance

attendance_bp = Blueprint('attendance', __name__)

attendance_bp.route('/mark', methods=['POST'])(mark_attendance)
attendance_bp.route('/report', methods=['GET'])(get_attendance)