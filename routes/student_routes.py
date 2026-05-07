from flask import Blueprint
from controllers.student_controller import add_student

student_bp = Blueprint('student', __name__)

student_bp.route('/add', methods=['POST'])(add_student)