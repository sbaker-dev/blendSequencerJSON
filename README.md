# blendSequencerJSON
This script extract the video sequencer strips from a blend file into a json database. Each strip will be given its own
entry within the json structure that follows the example as shown below. 

```json
{"strip_name.001": {
    "Duration": 100,
    "End": 200,
    "Path": "Path/to/clip.mp4",
    "Start": 100
    }
}
```

## How to install

Download the script from this repository, then go into edit -> blender Preferences -> Add-ons. From there you can then
press the install button in the top right. Navigate to the location you saved this file and then select it to install
the script. Once you have done this you should now find an add on under Generic called StripsToJson which you can enable
via using the tick box next to its name/

## How to use

Once you have installed it, the in the video editing tab of blender you will find a new tab in the sequencer called
stripsToJson. Navigate to this location, and then press the button to write out the json of this file. Note, you 
**must** save the blend file before running as it will save the json to the same directory and same name as your blend 
file just as a .txt rather than .blend.