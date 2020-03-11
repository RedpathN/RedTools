import bpy

class NineTile_Operator(bpy.types.Operator):
    bl_idname = "view3d.add_ninetile"
    bl_label = "Add NineTile"
    bl_description = "Adds a 3x3 tiling plane for baking tileables"

    def execute(self, context):
        # Get the active mesh
        make_ninetile()

        return {'FINISHED'}

class MakeCage_Operator(bpy.types.Operator):
    bl_idname = "view3d.make_cage"
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

    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked": False, "mode": 'TRANSLATION'},
                                  TRANSFORM_OT_translate={"value": (0, -0, 0)})
    bpy.ops.object.modifier_add(type='DISPLACE')
    bpy.context.object.modifiers["Displace"].strength = 0.2
    bpy.context.object.display_type = 'WIRE'





