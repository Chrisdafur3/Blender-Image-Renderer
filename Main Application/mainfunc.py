import os
import sys
from math import radians

argv = sys.argv 
# argv = argv[argv.index('--') + 1:]

args = " ".join(argv[argv.index('--') + 1:]).replace('--', '  ').split('    ')

def rotate_and_render(output_dir, sub_dir, name ,output_file_pattern_string, rotation_steps, rotation_angle):
    import bpy
    try:
        subject = bpy.context.scene.objects[name]
        original_rotation = subject.rotation_euler 
        for step in range(0, int(rotation_steps)):
            subject.rotation_euler[2] = radians(step * (int(rotation_angle) / int(rotation_steps)))
            current_path = os.path.join(output_dir, sub_dir)
            bpy.context.scene.render.filepath = os.path.join(current_path, (output_file_pattern_string + f'_{step}'))
            bpy.ops.render.render(write_still = True)
        subject.rotation_euler = original_rotation
    except Exception as e:
        print(e)
        

rotate_and_render(args[0], args[1], args[2], args[3], args[4], args[5])