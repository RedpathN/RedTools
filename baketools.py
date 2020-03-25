import bpy
from bpy.props import BoolProperty

# CLS----------------------------------------------------


class NineTile_Operator(bpy.types.Operator):

    bl_idname = "redtools.add_ninetile"
    bl_label = "Add NineTile"
    bl_description = "Adds a 3x3 tiling plane for baking tileables"

    def execute(self, context):
        # Get the active mesh
        make_ninetile()

        return {'FINISHED'}

class MakeCage_Operator(bpy.types.Operator):

    bl_idname = "redtools.make_cage"
    bl_label = "Make Cage"
    bl_description = "Duplicates active object and scales on normals"

    def execute(self, context):
        # Get the active mesh
        make_cage()

        return {'FINISHED'}



# FUNC----------------------------------------------------


def make_plane():

    bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, location=(-2, -2, 0))

    return bpy.context.active_object


def make_ninetile():

    ob = make_plane()
    array_x = ob.modifiers.new("RT_NineArrayX", 'ARRAY')
    array_x.count = 3
    array_x.use_merge_vertices = True

    array_y = ob.modifiers.new("RT_NineArrayY", 'ARRAY')
    array_y.relative_offset_displace[1] = 1
    array_y.use_relative_offset = False
    array_y.use_relative_offset = True
    array_y.relative_offset_displace[0] = 0
    array_y.count = 3
    array_y.use_merge_vertices = True

    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="RT_NineArrayX")
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="RT_NineArrayY")
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
    ob.show_wire = True

def get_name(ob):
    if (ob.name.endswith("_low") == True):
        name = ob.name[:-4]
    else:
        name = ob.name
    return name

def make_cage():
    ob = bpy.context.active_object

    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked": True, "mode": 'TRANSLATION'},
                                  TRANSFORM_OT_translate={"value": (0, -0, 0)})
    ob2 = bpy.context.active_object

    if(bpy.context.scene.PanelProps.cage_renamelow == True):
        ob.name = get_name(ob) + "_low"
    ob2.name = get_name(ob) + "_cage"

    cagemod = ob2.modifiers.new("RT_Cage", 'DISPLACE')
    cagemod.strength = 0.2
    ob2.display_type = 'WIRE'





