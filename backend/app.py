from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Task Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500))
    status = db.Column(db.String(50), default="pending")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status
        }


# Create database
with app.app_context():
    db.create_all()


# Home API
@app.route("/")
def home():
    return jsonify({
        "message": "TaskFlow API is running!"
    })


# Health Check
@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


# CREATE TASK
@app.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or not data.get("title"):
        return jsonify({
            "error": "Title is required"
        }), 400

    task = Task(
        title=data["title"],
        description=data.get("description", ""),
        status=data.get("status", "pending")
    )

    db.session.add(task)
    db.session.commit()

    return jsonify(task.to_dict()), 201


# READ ALL TASKS
@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()

    return jsonify([
        task.to_dict()
        for task in tasks
    ])


# READ SINGLE TASK
@app.route("/api/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = db.session.get(Task, task_id)

    if not task:
        return jsonify({
            "error": "Task not found"
        }), 404

    return jsonify(task.to_dict())


# UPDATE TASK
@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = db.session.get(Task, task_id)

    if not task:
        return jsonify({
            "error": "Task not found"
        }), 404

    data = request.get_json()

    if "title" in data:
        task.title = data["title"]

    if "description" in data:
        task.description = data["description"]

    if "status" in data:
        task.status = data["status"]

    db.session.commit()

    return jsonify(task.to_dict())


# DELETE TASK
@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = db.session.get(Task, task_id)

    if not task:
        return jsonify({
            "error": "Task not found"
        }), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({
        "message": "Task deleted successfully"
    })


if __name__ == "__main__":
    app.run(debug=True)
