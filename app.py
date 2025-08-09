from flask import Flask, render_template, request
from mindbloom import app as mental_health_graph # This should be your LangGraph compiled app

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    agent_reply = ""
    cmd_response = ""
    smi_response = ""
    developmental_response = ""

    if request.method == "POST":
        user_input = request.form["user_input"]
        state = {"user_input": user_input}
        response = mental_health_graph.invoke(state)

        cmd_response = response.get("cmd_response", "")
        smi_response = response.get("smi_response", "")
        developmental_response = response.get("developmental_response", "")

        # Combine responses for display (optional)
        agent_reply = cmd_response or smi_response or developmental_response or "No specific match."

    return render_template(
        "index.html",
        agent_reply=agent_reply,
        cmd_response=cmd_response,
        smi_response=smi_response,
        developmental_response=developmental_response
    )

if __name__ == "__main__":
    app.run(debug=True)


