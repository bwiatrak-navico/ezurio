from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo


#telemetry = {"temperature": 41.9, "enabled": False, "currentFirmwareVersion": "v1.2.2"}
telemetry = {"latitude": "41.654976233333336", "longitude": "-88.16709098333334", "speed":  50, "fuel":  5, "status": "On route"}
client = TBDeviceMqttClient("thingsboard.cloud", username="xdseb5xnnohvo2k7eieu")
# Connect to ThingsBoard
client.connect()
# Sending telemetry without checking the delivery status
client.send_telemetry(telemetry) 
# Sending telemetry and checking the delivery status (QoS = 1 by default)
result = client.send_telemetry(telemetry)
# get is a blocking call that awaits delivery status  
success = result.get() == TBPublishInfo.TB_ERR_SUCCESS
# Disconnect from ThingsBoard
client.disconnect()


