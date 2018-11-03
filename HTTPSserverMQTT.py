from flask import Flask
import paho.mqtt.client as mqtt
app = Flask(__name__)
topic = "teknobyen/doors/front/open"

username = ""
password = ""
def on_connect(client, userdate, flags, rc):
    print("publishing teknobyen/doors/front/open")
    client.publish(topic, payload=1)


@app.route("/")
def open_door():


    print("creating new instance")
    client = mqtt.Client()
    client.username_pw_set(username, password)
    client.tls_set()
    print("connecting")
    client.on_connect = on_connect
    client.connect("mqttbroker.tk", 8883)
    client.loop_forever()



if __name__ == '__main__':
    app.run()



