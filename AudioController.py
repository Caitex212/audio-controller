import pulsectl

class AudioController:

    pulse = pulsectl.Pulse('AudioController')
    master = pulse.sink_list()[0]
    source = pulse.source_list()[0]

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

    def getDefaultDevice(self):
        return self.master, self.source
    
    def getVolume(self, device: pulsectl.pulsectl.PulseSourceInfo): # get the device with getDefaultDevice
        return self.pulse.volume_get_all_chans(device)
    
    def setVolume(self, volume: float, device: pulsectl.pulsectl.PulseSourceInfo): # get the device with getDefaultDevice
        self.pulse.volume_set_all_chans(device, volume)

    def setMute(self, mute: bool, device: pulsectl.pulsectl.PulseSourceInfo): # get the device with getDefaultDevice
        self.pulse.mute(device, mute)