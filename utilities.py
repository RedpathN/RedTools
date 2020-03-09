import bpy
import bmesh


# FUNC----------------------------------------------------
class MakeHPOperator(bpy.types.Operator):
    bl_idname = "view3d.make_hp"
    bl_label = "Make HighPoly"
    bl_description = "Add bevel mod + subdiv"
    

    def execute(self, context):
        # Get the active mesh
        ob = bpy.context.object

        #Add subDiv
        make_hp(ob)
        return {'FINISHED'}



def make_hp(ob):

    set_smooth(ob)
    
    bpy.ops.object.modifier_add(type='BEVEL')
    bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
    bpy.context.object.modifiers["Bevel"].angle_limit = 0.53058
    bpy.context.object.modifiers["Bevel"].segments = 3
    bpy.context.object.modifiers["Bevel"].profile = 0.7
    bpy.context.object.modifiers["Bevel"].offset_type = 'PERCENT'
    bpy.context.object.modifiers["Bevel"].width_pct = 3.5
    bpy.context.object.modifiers["Bevel"].miter_outer = 'MITER_PATCH'


        
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.context.object.modifiers["Subdivision"].levels = 2

def set_smooth(ob):

    bpy.context.view_layer.objects.active = ob
    bpy.ops.object.shade_smooth()
    ob.data.use_auto_smooth = True
    ob.data.auto_smooth_angle = 1.13446
    

class MakeCurveAOperator(bpy.types.Operator):
    
    bl_idname = "view3d.make_curve_array"
    bl_label = "Make Curve Array"
    bl_description = "Create array object, assign to curve"
    

    def execute(self, context):

        #Make curve array
        make_curve_array()
        return {'FINISHED'}

def make_curve():
    
    curve = bpy.ops.curve.primitive_nurbs_path_add(enter_editmode=False, location=(0, 0, 0))
    
    return bpy.context.active_object

def make_cube():
    
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
    
    return bpy.context.active_object


def set_parent(a, b):
    
    a.parent = b
    
def make_curve_array():

    curve = make_curve()
    cube = make_cube()

    set_parent(curve, cube)
    set_smooth(cube)
    bpy.ops.object.modifier_add(type='ARRAY')
    bpy.context.object.modifiers["Array"].fit_type = 'FIT_CURVE'
    bpy.context.object.modifiers["Array"].use_merge_vertices = True
    bpy.ops.object.modifier_add(type='CURVE')
    bpy.context.object.modifiers["Curve"].object = curve
    bpy.context.object.modifiers["Array"].curve = curve

