import json
import requests

'''This class details some baic functions of the MohawkWebServer API using Python.  There is a swagger page for further documentation
at http://<host>:<port>/swagger-ui.html.

Note that this uses the external requests module so install that by executing 'pip install reqeusts' before running the code'''
class MohawkWebServer:

    def __init__(self):
        self.__host = 'localhost'
        self.__port = 8556

    @property
    def __stub(self):
        return f'http://{self.__host}:{self.__port}/mohawk/api/v1'

    def __constructUrl(self, path):
        url = f'{self.__stub}/{path}'
        print ('URL = ' + url)
        return url

    '''This is the host where Mohawk is running'''
    @property
    def host(self, host):
        return self.__host
    
    @host.setter
    def host(self, host):
        self.__host__ = host

    '''This is the port where Mohawk is running'''
    @property
    def port(self, port):
        return self.__port
    
    @host.setter
    def host(self, port):
        self.__host__ = port

    '''Status of the Lid'''
    @property
    def lid_status(self):
        return requests.get(self.__constructUrl('lid_status')).json()

    '''Current Status of Mohawk'''
    @property
    def mohawk_status(self):
        return requests.get(self.__constructUrl('mohawk_status')).json()

    '''Current Fan Speed of Mohawk'''
    @property
    def fan_speed(self):
        return requests.get(self.__constructUrl('fan_speed')).json()
    
    '''Current version of Mohawk'''
    @property
    def version(self):
        return requests.get(self.__constructUrl('version')).json()
    
    '''Current format of Mohawk'''
    @property
    def format(self):
        return requests.get(self.__constructUrl('format')).json()
    
    '''Current temperature of Mohawk'''
    @property
    def temperature(self):
        return requests.get(self.__constructUrl('temperature')).json()
    
    '''pins status of Mohawk'''
    @property
    def pins_status(self):
        return requests.get(self.__constructUrl('pins_status')).json()

    '''reset pins of Mohawk'''
    @property
    def reset_pins(self):
        return requests.post(self.__constructUrl('reset_pins')).json()
    
    
    #def scan_container(self, container_id, 
    #                   retrieve_raw_image=False, 
    #                   retrieve_annotated_image=False, 
    #                  retrieve_1dr2_image=False):
    #    params = {'container_uid' : container_id, 
    #              'raw_image' : str(retrieve_raw_image).lower(),
    #              'annotated_image' : str(retrieve_raw_image).lower(),
    #              '1dr2_image' : str(retrieve_1dr2_image).lower()}
    #    return requests.post(self.__constructUrl('scan'), params=params).json()

if __name__ == '__main__':
    
    #Create the MohawkWebServer object, note that this expects the Mohawk service to be running
    #(assuming you are on English language windows and using a default install location)
    mohawkWebServer = MohawkWebServer()
    
    #obtain some basic information from the system
    print ('lid status = ' + str(mohawkWebServer.lid_status))
    print ('mohawk status = ' + str(mohawkWebServer.mohawk_status))
    print ('fan speed = ' + str(mohawkWebServer.fan_speed))
    print ('version = ' + str(mohawkWebServer.version))
    print ('format = ' + str(mohawkWebServer.format))
    print ('temperature = ' + str(mohawkWebServer.temperature))
    print ('pins status = ' + str(mohawkWebServer.pins_status))
    print ('reset pins = ' + str(mohawkWebServer.reset_pins))

    
    