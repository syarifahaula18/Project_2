import dht
import network
import ntptime
import ujson
import utime

from machine import RTC
from machine import Pin
from time import sleep
from third_party import rd_jwt

from umqtt.simple import MQTTClient


# Konstanta-konstanta aplikasi

# WiFi AP Information
AP_SSID = "V2027"
AP_PASSWORD = "lonbeh11"

# Decoded Private Key
PRIVATE_KEY = (22799514201220815352785031162413187901123136268649316437571691175360710984144022457271074870136521886462322087160691156470601424637033729840540113426772147744202654053830975695563274545193117388650369677552636689194328990018377802192993330128624332096218473742719341456131249883143041122613206405934488098576199627763031596427535126756032681080800767484599740008109519552382045850310022236912064713958540528540689511283220054546159186573742573977265805018109015775529391202274006348331530255060953668710687366097734609396998871540792025624189700629274326506030589247129985353748378106303553979109899738665835836372063, 65537, 14484651010605152326602645184830484939059812040244181747634693894705564223809764240519683130033480709595270494850581152491111294630323883846387966532448619001138619469693554847803111203803357425482502889887873738366038754114548700308336821844689300565453901959989967512511721930124107911273379341707559797859316148317177562408735348863220002211007661587833602865161820403648737693323280904234506556528640950872177831826830722830273857052013578928326784268404091127459445278167921811140310103898078201794184098663418402248855845762248383611040930318970318267322626814697929628338591239422979864126081433388067482611393, 167995210219811409214560646506802154198956847979196854278671829307928542365664278845474786150732453818141372943852291178143389232224157998832747897837161208086106493407419170069607292714381910986068638183756289542038010833743546173924112863633127170070951867865132662131489368029143994703255189881955326408103, 135715263377979955843657702165678981774999283900521274348903641175584254641258221761064512416859328509897581983449685691782303018869412178218039813172255177004489791120139591156953626215138596254125806545344161237820271704251084966722753432027073380403796435013286401569183529847475808327506329455564182557321)


#Project ID of IoT Core
PROJECT_ID = "hsc2020-05"
# Location of server
REGION_ID = "asia-east1"
# ID of IoT registry
REGISTRY_ID = "NPM_1704111010021"
# ID of this device
DEVICE_ID = "esp32"

# MQTT Information
MQTT_BRIDGE_HOSTNAME = "mqtt.googleapis.com"
MQTT_BRIDGE_PORT = 8883


dht22_obj = dht.DHT22(Pin(4))
led_obj = Pin(5, Pin.OUT)

def read_dht22():
    # Read temperature from DHT 22
    #
    # Return
    #    * List (temperature, humidity)
    #    * None if failed to read from sensor
    
    try:
        dht22_obj.measure()
        return dht22_obj.temperature(), dht22_obj.humidity()
    except:
        return None
    
    

def connect():
    # Connect to WiFi
    print("Connecting to WiFi...")
    
    # Activate WiFi Radio
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    # If not connected, try tp connect
    if not wlan.isconnected():
        # Connect to AP_SSID using AP_PASSWORD
        wlan.connect(AP_SSID, AP_PASSWORD)
        # Loop until connected
        while not wlan.isconnected():
            pass
    
    # Connected
    print("  Connected:", wlan.ifconfig())


def set_time():
    # Update machine with NTP server
    print("Updating machine time...")

    # Loop until connected to NTP Server
    while True:
        try:
            # Connect to NTP server and set machine time
            ntptime.settime()
            # Success, break out off loop
            break
        except OSError as err:
            # Fail to connect to NTP Server
            print("  Fail to connect to NTP server, retrying (Error: {})....".format(err))
            # Wait before reattempting. Note: Better approach exponential instead of fix wiat time
            utime.sleep(0.5)
    
    # Succeeded in updating machine time
    print("  Time set to:", RTC().datetime())


def on_message(topic, message):
    print((topic,message))


def get_client(jwt):
    #Create our MQTT client.
    #
    # The client_id is a unique string that identifies this device.
    # For Google Cloud IoT Core, it must be in the format below.
    #
    client_id = 'projects/{}/locations/{}/registries/{}/devices/{}'.format(PROJECT_ID, REGION_ID, REGISTRY_ID, DEVICE_ID)
    client = MQTTClient(client_id.encode('utf-8'),
                        server=MQTT_BRIDGE_HOSTNAME,
                        port=MQTT_BRIDGE_PORT,
                        user=b'ignored',
                        password=jwt.encode('utf-8'),
                        ssl=True)
    client.set_callback(on_message)

    try:
        client.connect()
    except Exception as err:
        print(err)
        raise(err)

    return client


def publish(client, payload):
    # Publish an event
    
    # Where to send
    mqtt_topic = '/devices/{}/{}'.format(DEVICE_ID, 'events')
    
    # What to send
    payload = ujson.dumps(payload).encode('utf-8')
    
    # Send    
    client.publish(mqtt_topic.encode('utf-8'),
                   payload,
                   qos=1)

    # Subscribe to the config topic.
    

    
def subscribe_command1():
    print("Sending command to device")
    client_id = 'projects/{}/locations/{}/registries/{}/devices/{}'.format(PROJECT_ID, REGION_ID, REGISTRY_ID, DEVICE_ID)
    command = 'PING!'
    data = command.encode("utf-8")
    while True:
        led_obj.value(0)
        sleep(.5)
        led_obj.value(1)
        sleep(.5)
        led_obj.value(0)
        sleep(.5)
        led_obj.value(1)
        sleep(.5)
        led_obj.value(0)
        sleep(.5)
        led_obj.value(1)
        sleep(.5)
        led_obj.value(0)
        sleep(.5)
        led_obj.value(1)
        sleep(.5)
        led_obj.value(0)
        sleep(.5)
        led_obj.value(1)
        sleep(.5)
        led_obj.value(0)
        sleep(.5)
        led_obj.value(1)
        sleep(.5)
        led_obj.value(0)
        sleep(.5)
        led_obj.value(1)
        sleep(.5)
        led_obj.value(0)
        sleep(.5)
        led_obj.value(1)
        sleep(.5)
        led_obj.value(0)
        sleep(.5)
        led_obj.value(1)
        sleep(.5)
        led_obj.value(0)
        sleep(.5)
        led_obj.value(1)
        sleep(.5)
        led_obj.value(0)
        sleep(.5)
        led_obj.value(1)
        sleep(.5)
        led_obj.value(0)
        sleep(.5)
        led_obj.value(1)
        sleep(.5)
        led_obj.value(0)
        sleep(.5)
        led_obj.value(1)
        sleep(.5)
        led_obj.value(0)
        sleep(.5)
        led_obj.value(1)
        sleep(.5)
        break


#publish_events()
#publish_state()
#subscribe_config()
#subscribe_command()
subscribe_command1()
#subscribe_command2()
#subscribe_command3()
   

# Connect to Wifi
connect()
# Set machine time to now
set_time()

# Create JWT Token
print("Creating JWT token.")
start_time = utime.time()
jwt = rd_jwt.create_jwt(PRIVATE_KEY, PROJECT_ID)
end_time = utime.time()
print("  Created token in", end_time - start_time, "seconds.")

# Connect to MQTT Server
print("Connecting to MQTT broker...")
start_time = utime.time()
client = get_client(jwt)
end_time = utime.time()
print("  Connected in", end_time - start_time, "seconds.")

# Read from DHT22
#print("Reading from DHT22")
#result = read_dht22()
#print("  Temperature & humidity :", result)

# Publish a message
#print("Publishing message...")
#if result == None:
 #   result = "Fail to read sensor...."
#publish(client, result)
# Need to wait because command not blocking
#utime.sleep(1)

# Disconnect from client
client.disconnect()

