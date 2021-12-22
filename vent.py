#!/usr/bin/python3.7
from flask import jsonify
from flask import Flask, request
from smbus2 import SMBus
from mlx90614 import MLX90614
import time
import os

SLAVE_ADDRESS = 0x08
SENSOR_ADDRESS = 0x5a

app = Flask(__name__)
bus = SMBus(1)
arduino = MLX90614(bus, address = SLAVE_ADDRESS)
sensor = MLX90614(bus, address = SENSOR_ADDRESS)

@app.route('/api/led/')
def change_state():
 state = request.args.get('state')
 bus.write_byte(SLAVE_ADDRESS, int(state))
 return jsonify({ "state": state })

@app.route('/api/temp/')
def get_temp():
 sensorData = {}
 sensorData["object_1"] = round(float(sensor.get_object_1()), 2)
 sensorData["ambient"] = round(float(sensor.get_ambient()), 2)
 return jsonify(sensorData)

if __name__ == "__main__":

 app.run(host = "0.0.0.0", port = 9999)
