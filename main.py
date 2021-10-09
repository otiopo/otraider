from kahoot import client

bot = client()

import flask, threading

app = flask.Flask(__name__)

@app.route("/", methods=["GET"])
def index():
  return flask.render_template("index.html")

@app.route("/raidSuccess", methods=["GET"])
def raidSuccess():
  return flask.render_template("successraid.html")

def join(id, name):
  bot.join(id, name)

@app.route("/raidApi", methods=["GET"])
def raidApi():
  server = int(flask.request.args.get("id"))
  name = flask.request.args.get("name")

  for i in range(int(flask.request.args.get("limit")) + 1):
    threading.Thread(target=join, args=(server, name + str(i))).start()
  return "<script>location.href = \"https://website url here/raidSuccess\"</script>"

@app.route("/bg")
def bg():
  return flask.send_file("bg.jpg")

@app.route("/css")
def css():
  with open("cock.css", "r") as file:
    return file.read()
    file.close()

if __name__ == "__main__":  
  app.run("0.0.0.0", port=80)
