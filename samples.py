from sense_hat import SenseHat
import socketio
import json
sense = SenseHat()
sio = socketio.Client()
sio.connect('http://ec2-18-234-69-212.compute-1.amazonaws.com')

def main():
	while True:
		if sense._read_imu():
			output = {
				'data': [
					{
						"sensor" : "Accelerometer", 
						"time": sense._imu.getIMUData()['timestamp'],
						"x": sense._imu.getIMUData()['accel'][0], 
						"y": sense._imu.getIMUData()['accel'][1], 
						"z": sense._imu.getIMUData()['accel'][2]
					},
					{
						"sensor": "Gyroscope", 
						"time": sense._imu.getIMUData()['timestamp'],
						"x": sense._imu.getIMUData()['gyro'][0], 
						"y": sense._imu.getIMUData()['gyro'][1], 
						"z": sense._imu.getIMUData()['gyro'][2]
					}
				]
			}
			
			sio.emit('sensors', output)








if __name__ == '__main__':
    main()
