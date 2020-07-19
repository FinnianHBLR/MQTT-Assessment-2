import wmi
from time import sleep
import paho.mqtt.publish as publish

def publishData(cpu1, cpu2):
    # A method that publishes data to the mosquito. This explains it a bit more https://github.com/rethinkdb/docs/issues/1057#issuecomment-200515848
    publish.single("CPU/1", cpu1, hostname="127.0.0.1", port=8883, tls={"ca_certs": "ca-cert.pem"})
    publish.single("CPU/2", cpu2, hostname="127.0.0.1", port=8883, tls={"ca_certs": "ca-cert.pem"})


# Sets up the code that collects CPU data from Open Hardware Monitor
w = wmi.WMI(namespace="root\OpenHardwareMonitor")
temperature_infos = w.Sensor()

while True:
    for sensor in temperature_infos:
        if sensor.SensorType==u'Load':
            # My Laptop cannot log temperature so this will log load instead.
            if sensor.Name == "CPU Core #1" or sensor.Name == "CPU Core #2":
                cpu1 = (sensor.Name)
                # Format string
                cpu2 = "Load: " + f"{int(sensor.Value)}%"
                publishData(cpu1, cpu2)
                print("Sending")
    # waits 3 seconds to send the next data
    sleep(30)


