import bpy

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



def make_plane():

    bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, location=(-2, -2, 0))

    return bpy.context.active_object


def make_ninetile():

    ob = make_plane()
    bpy.ops.object.modifier_add(type='ARRAY')
    bpy.context.object.modifiers["Array"].count = 3
    bpy.ops.object.modifier_add(type='ARRAY')
    bpy.context.object.modifiers["Array.001"].relative_offset_displace[1] = 1
    bpy.context.object.modifiers["Array.001"].use_relative_offset = False
    bpy.context.object.modifiers["Array.001"].use_relative_offset = True
    bpy.context.object.modifiers["Array.001"].relative_offset_displace[0] = 0
    bpy.context.object.modifiers["Array.001"].count = 3
    bpy.context.object.modifiers["Array"].use_merge_vertices = True
    bpy.context.object.modifiers["Array.001"].use_merge_vertices = True
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Array")
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Array.001")
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
    bpy.context.object.show_wire = True


def make_cage():
    ob = bpy.context.active_object

    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked": True, "mode": 'TRANSLATION'},
                                  TRANSFORM_OT_translate={"value": (0, -0, 0)})
    ob2 = bpy.context.active_object
    if (ob.name.endswith("_low") == True):
        ob.name = ob.name[:-4]
    ob2.name = ob.name + "_cage"
    if (ob.name.endswith("_low") == False):
        ob.name += "_low"

    cagemod = ob2.modifiers.new("RT_Cage", 'DISPLACE')
    cagemod.strength = 0.2
    ob2.display_type = 'WIRE'





