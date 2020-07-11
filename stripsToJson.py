import bpy
import json 
import os

bl_info = {
    "name": "stripsToJson",
    "Author": "Samuel Baker",
    "Description": "Extract strips from a video sequencer and write the information to a json file",
    "blender": (2, 83, 0),
    "location": "SEQUENCE_EDITOR",
    "warning": "",
    "category": "Generic"
}


class SquencerExtraction(bpy.types.Operator):
    bl_idname = "bpt.sequencerextraction_op"
    bl_label = "Extract sequencer strips"
    bl_description = "Extract strips from a video sequencer and write the information to a json file"
    
    def execute(self, context):
        print(bpy.data.is_saved)
        if bpy.data.is_saved:
            
            file_path = bpy.data.filepath
            write_dir = os.path.dirname(file_path)
            
            file_name = bpy.path.basename(bpy.context.blend_data.filepath).split('.')[0]
            write_file_name = os.path.join(write_dir, f"{file_name}.txt")  
                  
            with open(write_file_name, "w", encoding="utf-8") as json_saver:
                json.dump(self.extract_timeline_strips(), json_saver, ensure_ascii=False, indent=4, sort_keys=True)  
        else:
            self.report({"ERROR"}, "You must save the blend file before running this script!")
        return {'FINISHED'}  

    def extract_timeline_strips(self):
        """
        This extracts strips from the video editing scenes sequence editor, extracting the path of strip, the start and the end frames
        for each strip within the video sequence editor.
        
        It uses the bpy MoveSequence Object found here: 
            
            https://docs.blender.org/api/current/bpy.types.MovieSequence.html
            
        With the original information on how to get to the MovieSequence object found here: 
            
            https://blender.stackexchange.com/questions/72332/get-all-sequencer-strips-in-python
        """
        json_holder = {}
        for scene in bpy.data.scenes:
            if scene.sequence_editor is not None:
                strip_list = scene.sequence_editor.sequences_all
                if strip_list is not None:
                    self.set_json_strips(json_holder, strip_list)

        return json_holder     

    def set_json_strips(self, json_dict, list_of_strips):
        """
        This sets a given entry in the json file to be equal to the strip name, so that duplicates of the same strip don't overide itself,
        being assigned the start, end, duration and path of the given strip
        
        """
        for strip in list_of_strips:
            json_dict[strip.name] = {
            
            "Start": strip.frame_start,
            "End": (strip.frame_start + strip.frame_duration) - 1,
            "Duration": strip.frame_duration,
            "Path": strip.filepath
            
             }
             
             
class SquencerExtractionPanel(bpy.types.Panel):
    bl_idname = "SE_PT_Panel"
    bl_label = "Squencer Extraction"
    bl_category = "stripsToJson"
    bl_space_type = "SEQUENCE_EDITOR"
    bl_region_type = "UI"
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("bpt.sequencerextraction_op", text="Write Json")

             
classes = (SquencerExtractionPanel, SquencerExtraction)

register, unregister = bpy.utils.register_classes_factory(classes)