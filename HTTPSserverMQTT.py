from flask import Flask, request
import paho.mqtt.client as mqtt
app = Flask(__name__)
topic = "teknobyen/doors/front/open"
client = mqtt.Client()

def on_connect(client, userdate, flags, rc):
    client.publish(topic, payload=1)
    client.loop_stop(force=False)


@app.route("/")
def open_door():
    username = request.args.get("username")
    password = request.args.get("password")
    print("creating new instance")

    client.username_pw_set(username, password)
    client.tls_set()
    print("connecting")
    client.on_connect = on_connect
    client.connect("mqttbroker.tk", 8883)
    client.loop_start()

    return "Opening door!"



if __name__ == '__main__':
    app.run()



