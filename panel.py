import bpy
from bpy.types import PropertyGroup

from . import baketools
from bpy.props import BoolProperty
from bpy.props import IntProperty


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
        props = bpy.context.scene.PanelProps

        col = layout.box()
        col.label(text="Utility")

        box = col.box()
        box.operator('redtools.floorsnap', text="FloorSnap")
        box.prop(props, 'floorsnap_target_front', text="Floorsnap to frontmost")
        box.prop(props, 'floorsnap_target_left', text="Floorsnap to leftmost")
        #box.prop(props, 'floorsnap_worldorigin', text="Move to World Origin")
        box = col.box()
        box.operator('redtools.make_hp', text="Make HighPoly")

        box = col.box()
        box.operator('redtools.make_wn', text="Make Weighted Normals")

        box = col.box()
        box.operator('redtools.make_cage', text="Make Cage")
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
        if( props.curvearray_use_active == False ):
            box.prop(props, 'curvearray_use_endcaps', text="Use EndCaps")
            box.prop(props, 'curvearray_mesh_scale', text="Mesh Scale:")

        #box.operator('redtools.add_curve_mesh', text="Add Curve Mesh")
        box = col.box()
        box.operator('redtools.add_ninetile', text="Add NineTile")



#   PROP---------------------------------------------
class PanelProps(bpy.types.PropertyGroup):

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

    curvearray_use_endcaps: BoolProperty(
        name="CurveArray Mesh Endcaps",
        description="Add endcaps to mesh",
        default=(False),
    )

    curvearray_mesh_scale: IntProperty(
        name="CurveArray Mesh Scale",
        default = 2,
        description="Starting scale of the curve object",
    )

    floorsnap_target_front: BoolProperty(
        name="FloorSnap Front",
        default=True,
        description="Target front-most vertices",
    )

    floorsnap_target_left: BoolProperty(
        name="FloorSnap Left",
        default=True,
        description="Target front-most vertices",
    )

    floorsnap_worldorigin: BoolProperty(
        name="FloorSnap WorldOrigin",
        default=True,
        description="Move location to world origin",
    )