
#2021-08-28_Python_Earsketch_Taurus Utkarsh_Remix

#Ernie_pybeats

#		python code
#		script_name: Ernie Sampke_Earsketch August 2021
#
#		author: Ernie Douyin
#		description: House Music_EDM
#

# 1.SET UP

from earsketch import *

init()
setTempo(120)

#2. MUSIC CREATION
chord =RD_UK_HOUSE__5THCHORD_2
secondaryBeat = HIPHOP_BASSSUB_001
mainBeat = HOUSE_MAIN_BEAT_003


# fitMedia(trackName,trackNumber,startLocation, endLocation)
fitMedia(chord,1,1,16)

#3. ADDING SOUND EFFECTS: Between  Measures :1  and 16  moving from 60db to  5db and backdown

#SIMPLFIED :setEffect(trackNumber,effectName,effectParameter,effectValue)
#EXPANDED: setEffect(trackNumber,effectName,effectParameter,effectStartValue,effectStartLocation,EffectEndValue,EffectEndLocation)

setEffect = (1, VOLUME,GAIN,-60,1,5,12)
setEffect = (1, VOLUME,GAIN,5,12,-60,16)

fitMedia(secondaryBeat,2,1,12)

#Adding More Sound Effects

setEffect = (2, DELAY,DELAY_TIME,500)
fitMedia(mainBeat,3,1,8)

# Adding More Sound Effects
setEffect = (3,REVERB,REVERB_TIME,200)

#FINISH






finish()
