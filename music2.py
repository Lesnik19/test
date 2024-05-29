from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))


volume.SetMasterVolumeLevelScalar(0.12, None)  #Где 0.2 это 20% громкость

current_volume = volume.GetMasterVolumeLevelScalar()  # Получить текущий уровень звука
