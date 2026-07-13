from flask import Flask, request, jsonify
from tasks import send_email

app = Flask(__name__)

@app.route("/send-email", methods=["POST"])
def email():

    data = request.get_json()

    task = send_email.delay(
        data["email"]
    )

    return jsonify({
        "message": "Task Queued",
        "task_id": task.id
    })

@app.route("/status/<task_id>")
def status(task_id):

    task = send_email.AsyncResult(task_id)

    return jsonify({
        "task_id": task.id,
        "status": task.status,
        "result": task.result
    })

@app.route("/health")
def health():

    return jsonify({
        "status": "healthy"
    })

if __name__ == "__main__":
    app.run(debug=True)
