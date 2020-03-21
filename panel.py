import bpy


class PT_RTPanel(bpy.types.Panel):
    bl_idname = "RT_PT_MainPanel"
    bl_label = "RedTools"
    bl_category = "RedTools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('redtools.floorsnap', text="FloorSnap")

        row = layout.row()
        row.operator('redtools.make_hp', text="Make HighPoly")

        row = layout.row()
        row.operator('redtools.make_cage', text="Make Cage")

        col = layout.column()
        col.label(text="Add Object")

        row = col.row()
        row.operator('redtools.add_dynacyl', text="Add Dynacyl")
        row = col.row()
        row.operator('redtools.add_curve_array', text="Add Curve Array")
        row = col.row()
        row.operator('redtools.add_ninetile', text="Add NineTile")


