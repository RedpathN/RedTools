import bpy
import bmesh
from bpy.types import Operator
from bpy.props import IntProperty
from bpy.props import FloatProperty
from bpy.props import BoolProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector


def add_object(self, context):
    scale_x = self.radius
    scale_z = self.height
    
    if self.floored == False:        
        if self.endCaps == True:
            verts = [
                
                Vector((0 * scale_x, 0, 1 * (scale_z*0.5))),
                Vector((1 * scale_x, 0, 1 * (scale_z*0.5))),
                Vector((1 * scale_x, 0, -1 * (scale_z*0.5))),            
                Vector((0 * scale_x, 0, -1 * (scale_z*0.5))),
                
            ]

            edges = [[0, 1],[1, 2],[2, 3]]
            faces = []
        else:
            verts = [
                
                Vector((1 * scale_x, 0, 1 * (scale_z*0.5))),
                Vector((1 * scale_x, 0, -1 * (scale_z*0.5))),            
                
            ]
            edges = [[0, 1]]
            faces = []
    else:    
        if self.endCaps == True:
            verts = [
                
                Vector((0 * scale_x, 0, 1 * scale_z)),
                Vector((1 * scale_x, 0, 1 * scale_z)),
                Vector((1 * scale_x, 0, 0)),            
                Vector((0 * scale_x, 0, 0)),
                
            ]

            edges = [[0, 1],[1, 2],[2, 3]]
            faces = []
        else:
            verts = [
                
                Vector((1 * scale_x, 0, 1 * scale_z)),
                Vector((1 * scale_x, 0, 0)),            
                
            ]
            edges = [[0, 1]]
            faces = []

    mesh = bpy.data.meshes.new(name="DynaCyl")
    mesh.from_pydata(verts, edges, faces)
    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)
    object_data_add(context, mesh, operator=self)
    
    return mesh
    
def add_modifiers(self, context):

    bpy.ops.object.modifier_add(type='SCREW')
    bpy.context.object.modifiers["Screw"].steps = self.sideNum
    bpy.context.object.data.use_auto_smooth = True
    bpy.context.object.data.auto_smooth_angle = 1.13446

    
    if self.thickness != 0.0:
        bpy.ops.object.modifier_add(type='SOLIDIFY')
        bpy.context.object.modifiers["Solidify"].thickness = self.thickness
        bpy.context.object.modifiers["Solidify"].use_even_offset = True


    if self.subDiv == True:
        
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
        bpy.context.object.modifiers["Bevel"].angle_limit = 1.48353
        bpy.context.object.modifiers["Bevel"].segments = 2
        bpy.context.object.modifiers["Bevel"].profile = 1
        bpy.context.object.modifiers["Bevel"].offset_type = 'PERCENT'
        bpy.context.object.modifiers["Bevel"].width_pct = 5

        
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subdivision"].levels = 2
    
        if self.sideNum < 5:
            self.faceted = True
            
        if self.faceted == True:
            bpy.context.object.modifiers["Bevel"].miter_outer = 'MITER_ARC'
            if self.thickness != 0.0:
                bpy.context.object.modifiers["Bevel"].limit_method = 'NONE'
            else:
                bpy.context.object.modifiers["Bevel"].angle_limit = 0.174533
    else:
        
        self.faceted = False;

        

class OBJECT_OT_add_object(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_dynacyl"
    bl_label = "Add DynaCyl"
    bl_options = {'REGISTER', 'UNDO'}

    radius: FloatProperty(
        name="Radius",
        default=(1.0),
        subtype='NONE',
        description="Radius",
    )
    
    height: FloatProperty(
        name="Height",
        default=(2.0),
        subtype='NONE',
        description="Height",
    )
    
    sideNum: IntProperty(
        name="Sides",
        default=(16),
        min=(3),
        subtype='NONE',
        description="Number of sides",
    )
    
    floored: BoolProperty(
        name="Floored",
        default=(False),
        subtype='NONE',
        description="Set cyl base to floor",
    )
    
    endCaps: BoolProperty(
        name="End Caps",
        default=(True),
        subtype='NONE',
        description="Add/remove endcaps",
    )
    
    thickness: FloatProperty(
        name="Thickness",
        default=(0.0),
        subtype='NONE',
        description="Add thickness to cylinder. 0 = none",
    )
    
    subDiv: BoolProperty(
        name="SubDiv",
        default=(False),
        subtype='NONE',
        description="Add support loops + SubDiv",
    )
    
    faceted: BoolProperty(
        name="Faceting",
        default=(False),
        subtype='NONE',
        description="Adds fixes for faceted cyls using thickness",
    )
    

    def execute(self, context):

        mesh = add_object(self, context)
        add_modifiers(self, context)
        return {'FINISHED'}


# Registration

def add_object_button(self, context):
    self.layout.operator(
        OBJECT_OT_add_object.bl_idname,
        text="DynaCyl",
        icon='SURFACE_NCYLINDER')


# This allows you to right click on a button and link to documentation
def add_object_manual_map():
    url_manual_prefix = "https://docs.blender.org/manual/en/latest/"
    url_manual_mapping = (
        ("bpy.ops.mesh.add_object", "scene_layout/object/types.html"),
    )
    return url_manual_prefix, url_manual_mapping
