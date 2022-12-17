from influxdb_client import InfluxDBClient, Point, Dialect
from influxdb_client.client.write_api import SYNCHRONOUS

def write(key, value):
    client = InfluxDBClient(url="http://localhost:8086", org="MyOrg")
    write_api = client.write_api(write_options=SYNCHRONOUS)
    point = Point("meterstanden").tag("Code", key).field("Value", value)
    write_api.write(bucket="smartmeter", record=[point])
