import AudioController

ac = AudioController.AudioController()
print(ac.getInputDevice())
print(ac.getOutputDevice())
print(ac.getVolume(ac.getInputDevice()))
print(ac.getVolume(ac.getOutputDevice()))