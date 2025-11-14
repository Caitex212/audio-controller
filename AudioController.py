import pulsectl

class AudioController:

    pulse = pulsectl.Pulse('AudioController')
    master = None # Default output device
    source = None # Default input device

    def __init__(self):
        default_sink_name = self.pulse.server_info().default_sink_name
        default_source_name = self.pulse.server_info().default_source_name
        for sink in self.pulse.sink_list():
            if sink.name == default_sink_name:
                self.master = sink
        for source in self.pulse.source_list():
            if source.name == default_source_name:
                self.source = source
    
    def refreshDefaults(self):
        default_sink_name = self.pulse.server_info().default_sink_name
        default_source_name = self.pulse.server_info().default_source_name
        for sink in self.pulse.sink_list():
            if sink.name == default_sink_name:
                self.master = sink
        for source in self.pulse.source_list():
            if source.name == default_source_name:
                self.source = source

        return default_sink_name, default_source_name

    def getDefaultDevices(self):
        return self.master, self.source
    
    def getApplications(self):
        return self.pulse.sink_input_list()
    
    def getVolume(self, device): # get the device with getDefaultDevice or getApplications
        return self.pulse.volume_get_all_chans(device)
    
    def setVolume(self, volume: float, device): # get the device with getDefaultDevice or getApplications
        self.pulse.volume_set_all_chans(device, volume)

    def setMute(self, mute: bool, device): # get the device with getDefaultDevice or getApplications
        self.pulse.mute(device, mute)