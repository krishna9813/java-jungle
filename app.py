from flask import *
import json,time
from da import ServicePlacement
from device import Device
from fog import FogNode
app = Flask(__name__)
listOfDevices=[]
listOfFogNodes=[]
requestList=dict()
distanceMap=dict()
dummy=[]

def algo():
    
    for device in listOfDevices:
            
            listOfDistances=[]
            for fog in listOfFogNodes:
                
                distance=ServicePlacement.getDistance(device.getCoordinates(),fog.getCoordinates()) 
                listOfDistances.append(distance)
            priorityList=listOfDistances.copy()
            priorityList.sort()
            for i in range(len(priorityList)):
                for y in range(len(listOfDistances)):
                    if(priorityList[i]==listOfDistances[y]):
                        device.preferenceList.append(int(listOfFogNodes[y].id))
                
                distanceMap[int(device.id)]=device.preferenceList
                
   
    
    for k in range(len(listOfDevices)):
        currdevice=listOfDevices[k]
        
        for fg in range(len(listOfDevices[k].preferenceList)):
            for m in range(len(listOfFogNodes)):
                if(int(listOfDevices[k].preferenceList[fg])==int(listOfFogNodes[m].id)):
                    fog=listOfFogNodes[m]
                    break
            if currdevice.preferenceList[fg] not in requestList.keys():
                    requestList[currdevice.preferenceList[fg]]=[]

                
            
            if(float(currdevice.cpu)<float(fog.cpuFog)):
                    requestList[currdevice.preferenceList[fg]].append(int(currdevice.id))
                    fog.cpuFog=float(fog.cpuFog)-float(currdevice.cpu)
                    x=fog.cpuFog
                    dummy.append(x) 
                    break   
    
@app.route('/device/add/',methods=['GET'])
def addDevice():
    deviceid=str(request.args.get('id'))
    latitude=str(request.args.get('lat'))
    longitude=str(request.args.get('long'))
    cpu=str(request.args.get('cpuTime'))
    
    device=Device(deviceid,latitude,longitude,cpu)
    listOfDevices.append(device)
   
    return "Device Added Successfully"


@app.route('/fog/add/',methods=['GET'])
def addFogNode():
    fogid=str(request.args.get('id'))
    foglatitude=str(request.args.get('lat'))
    foglongitude=str(request.args.get('long'))
    fogcpu=str(request.args.get('cpuTime'))
    fog=FogNode(fogid,foglatitude,foglongitude,fogcpu)
    listOfFogNodes.append(fog)
    
    return "Fog Added Successfully"

@app.route('/getPreferenceList/',methods=['GET'])
def getPreferenceList():
    [device.preferenceList.clear() for device in listOfDevices]

    algo()
    n=int(request.args.get('no'))   
    return listOfDevices[n].preferenceList
@app.route('/getRequestList/',methods=['GET'])
def getRequestList():
    ServicePlacement.requestList.clear()
    algo()
    return requestList

if __name__=="__main__":
    app.run(host=0.0.0.0, debug=True)