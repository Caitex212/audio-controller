import AudioController

ac = AudioController.AudioController()
print(ac.getDefaultDevices())
print(ac.getVolume(ac.getDefaultDevices()[0]))
print(ac.getVolume(ac.getDefaultDevices()[1]))
print(ac.getApplications())

for app in ac.getApplications():
    print(app)
    print(type(app))
    if app.name == "Spotify":
        print(ac.getVolume(app))