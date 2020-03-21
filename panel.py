import bpy
from bpy.types import PropertyGroup

from . import baketools
from bpy.props import BoolProperty
# CLS---------------------------------------------------

class PT_RTPanel(bpy.types.Panel):
    bl_idname = "RT_PT_MainPanel"
    bl_label = "RedTools"
    bl_category = "RedTools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    @classmethod
    def poll(self, context):
        return True

    def draw(self, context):
        layout = self.layout
        props = bpy.context.scene.BoolProps

        col = layout.box()
        col.label(text="Utility")

        box = col.box()
        box.operator('redtools.floorsnap', text="FloorSnap")

        box = col.box()
        box.operator('redtools.make_hp', text="Make HighPoly")

        box = col.box()
        box.operator('redtools.make_wn', text="Make Weighted Normals")

        box = col.box()
        cage = box.operator('redtools.make_cage', text="Make Cage")
        box.prop(props, 'cage_renamelow', text="Add suffix to LowPoly")


        layout.separator()

        col = layout.box()
        col.label(text="Add Object")
        col.separator(factor=1.0)

        box = col.box()
        box.operator('redtools.add_dynacyl', text="Add Dynacyl")
        box = col.box()
        box.operator('redtools.add_curve_array', text="Add Curve Array")
        box.prop(props, 'curvearray_use_active', text="Use active for curve array")
        box = col.box()
        box.operator('redtools.add_ninetile', text="Add NineTile")



#   PROP---------------------------------------------
class BoolProps(bpy.types.PropertyGroup):

    cage_renamelow: BoolProperty(
        name="Add LowPoly suffix",
        description="Renames lowpoly from Obj to Obj_low",
        default=(True),
    )

    curvearray_use_active: BoolProperty(
        name="CurveArray, use active object",
        description="Uses the active object or creates a cube",
        default=(True),
    )