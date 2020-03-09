import bpy


class PT_Panel(bpy.types.Panel):
    bl_idname = "RedTools_Panel"
    bl_label = "RedTools"
    bl_category = "RedTools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('view3d.floorsnap', text="FloorSnap")
        row = layout.row()
        row.operator('mesh.add_dynacyl', text="Add Dynacyl")
        row = layout.row()
        row.operator('view3d.make_hp', text="Make HighPoly")
        row = layout.row()
        row.operator('view3d.make_curve_array', text="Make Curve Array")

