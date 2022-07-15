import json
import requests
from pathlib import Path

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
    
    '''set pins up for Mohawk'''
    @property
    def pins_up(self):
        pinsObj = [{'row': 1,'column': 1},{'row': 3,'column': 3}]
        return requests.post(self.__constructUrl('pins_up'),json=pinsObj).json()

    '''configure reader for Mohawk'''
    @property
    def configure_reader(self):
        readerObj = {"type": "ZIATH"}
        return requests.post(self.__constructUrl('reader'),json=readerObj).json()

    '''read barcode from Mohawk'''
    @property
    def read_barcode(self):
        return requests.post(self.__constructUrl('read_barcode')).json()

    '''set rack barcode for Mohawk'''
    @property
    def set_rack_barcode(self):
        rackLoaderObj = {"rack_barcode": "001","reset_pins": True}
        return requests.post(self.__constructUrl('set_rack_barcode'),json=rackLoaderObj).json()
    
    '''set load worklist for Mohawk'''
    @property
    def load_worklist(self):
        worklistObj = [{"rack_barcode": "001","row": 1, "column": 1},{"rack_barcode": "002","row": 3,"column": 1},{"rack_barcode": "002","row": 1,"column": 4},{"rack_barcode": "001","row": 3,"column": 3}]
        return requests.post(self.__constructUrl('worklist/load_json'),json=worklistObj).json()
        
    '''set load worklist for Mohawk'''
    @property
    def load_worklist_excel(self):
        script_dir=Path(__file__).parent 
        template_path=(script_dir/'picklistSample.xlsx').resolve()
        with open(template_path, 'rb') as f:
            data = f.read()
        return requests.post(self.__constructUrl('worklist/load_excel'),data = data,headers={'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'}).json()

    '''set load worklist for Mohawk'''
    @property
    def load_worklist_xml(self):
        script_dir=Path(__file__).parent 
        template_path=(script_dir/'picklistSample.xml').resolve()
        with open(template_path, 'rb') as f:
            data = f.read()
        return requests.post(self.__constructUrl('worklist/load_xml'),data = data,headers={'Content-Type': 'application/xml'}).json()

    '''set load worklist for Mohawk'''
    @property
    def load_worklist_csv(self):
        script_dir=Path(__file__).parent 
        template_path=(script_dir/'picklistSample.csv').resolve()
        with open(template_path, 'rb') as f:
            data = f.read()
        return requests.post(self.__constructUrl('worklist/load_csv'),data = data,headers={'Content-Type': 'text/csv'}).json()


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
    print ('pins up = ' + str(mohawkWebServer.pins_up))
    print ('Configure Reader = ' + str(mohawkWebServer.configure_reader))
    print ('Read Barcode = ' + str(mohawkWebServer.read_barcode))
    print ('Set Rack Barcode = ' + str(mohawkWebServer.set_rack_barcode))
    print ('Load Worklist Json = ' + str(mohawkWebServer.load_worklist))
    print ('Load Worklist Excel = ' + str(mohawkWebServer.load_worklist_excel))
    print ('Load Worklist Xml = ' + str(mohawkWebServer.load_worklist_xml))
    print ('Load Worklist Csv = ' + str(mohawkWebServer.load_worklist_csv))

    
    