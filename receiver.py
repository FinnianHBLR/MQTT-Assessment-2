 #You need a cert.pem for this to work.
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    # Connects to Broker
    print("Connected to Server: Code-" + str(rc))
    # Subscribes to topics
    client.subscribe("CPU/1")
    client.subscribe("CPU/2")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

    # Do some things here


 #TLS SSL STUFF. This refrences the generated encryption file.

client = mqtt.Client("Client", transport="tcp")
client.tls_set("ca-cert.pem")
client.on_connect = on_connect
client.on_message = on_message



client.connect("127.0.0.1", 8883, 60)

client.loop_forever()

