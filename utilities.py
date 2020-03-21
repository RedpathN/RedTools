import bpy


# CLS----------------------------------------------------

class MakeHPOperator(bpy.types.Operator):
    bl_idname = "redtools.make_hp"
    bl_label = "Make HighPoly"
    bl_description = "Add bevel mod + subdiv"
    

    def execute(self, context):
        # Get the active mesh
        ob = bpy.context.object

        #Add subDiv
        make_hp(ob)
        return {'FINISHED'}


class MakeWNOperator(bpy.types.Operator):
    bl_idname = "redtools.make_wn"
    bl_label = "Make Weighted Normals"
    bl_description = "Bevel to 1 segment and weight normals by face"

    def execute(self, context):
        # Get the active mesh
        ob = bpy.context.object

        # Add subDiv
        make_wn(ob)
        return {'FINISHED'}

# FUNC----------------------------------------------------


def get_hpsubsurf(ob):

    hpsubsurf = ob.modifiers.get("RT_HPSubSurf")


    return hpsubsurf

def get_hpbevel(ob):

    hpbevel = ob.modifiers.get("RT_HPBevel")

    return hpbevel

def make_hp(ob):

    set_smooth(ob)
    
    hpbevel = get_hpbevel(ob)
    if hpbevel is None:
        hpbevel = ob.modifiers.new("RT_HPBevel", 'BEVEL')

    hpbevel.limit_method = 'ANGLE'
    hpbevel.angle_limit = 0.436332
    hpbevel.segments = 3
    hpbevel.profile = 0.7
    hpbevel.offset_type = 'OFFSET'
    hpbevel.width = 0.04
    hpbevel.miter_outer = 'MITER_PATCH'

    hpsubsurf = get_hpsubsurf(ob)
    if hpsubsurf is None:
        hpsubsurf = ob.modifiers.new("RT_HPSubSurf", 'SUBSURF')

    hpsubsurf.levels = 2

def set_smooth(ob):

    bpy.context.view_layer.objects.active = ob
    bpy.ops.object.shade_smooth()
    ob.data.use_auto_smooth = True
    ob.data.auto_smooth_angle = 1.13446

def make_wn(ob):

    set_smooth(ob)

    hpbevel = get_hpbevel(ob)
    if hpbevel is None:
        hpbevel = ob.modifiers.new("RT_HPBevel", 'BEVEL')

    hpbevel.limit_method = 'ANGLE'
    hpbevel.angle_limit = 0.436332
    hpbevel.segments = 1
    hpbevel.profile = 0.7
    hpbevel.offset_type = 'OFFSET'
    hpbevel.width = 0.03
    hpbevel.miter_outer = 'MITER_PATCH'

    hpsubsurf = get_hpsubsurf(ob)
    if( hpsubsurf is not None ):
        ob.modifiers.remove(hpsubsurf)

    wn_mod = ob.modifiers.new("RT_Weighted Normals", 'WEIGHTED_NORMAL')

