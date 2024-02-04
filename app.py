import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
  cpu_metric = psutil.cpu_percent(interval=0.1)
  mem_metric = psutil.virtual_memory().percent
  Message = None

  if cpu_metric > 80 or mem_metric > 80:
    Message = "High CPU or Memory Utilization detected. Please Scale up"

  return render_template("index.html", cpu_percent=cpu_metric, mem_percent=mem_metric, message=Message)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')