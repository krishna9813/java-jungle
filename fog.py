class FogNode:
    def __init__(self,id,latitude,longitude,cpuFog):
        self.id=id
        self.latitude=latitude
        self.longitude=longitude
        self.cpuFog=cpuFog
    def getCoordinates(self):
        return [self.latitude, self.longitude]