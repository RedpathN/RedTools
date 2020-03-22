import bpy
from . import utilities
from bpy.props import BoolProperty
from bpy.props import IntProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from bpy.types import Operator
from mathutils import Vector


# CLS----------------------------------------------------
class AddCurveAOperator(Operator, AddObjectHelper):
    bl_idname = "redtools.add_curve_array"
    bl_label = "Add Curve Array"
    bl_description = "Create array object, assign to curve"



    def execute(self, context):
        # Make curve array
        make_curve_array(self, context)
        return {'FINISHED'}

class AddCurveMeshOperator(Operator, AddObjectHelper):
        bl_idname = "redtools.add_curve_mesh"
        bl_label = "Add Curve Meshs"
        bl_description = "Create mesh with no endcaps"



        def execute(self, context):
            # Make curve array
            make_curve_mesh(self, context)
            return {'FINISHED'}


# FUNC----------------------------------------------------

def make_curve():
    curve = bpy.ops.curve.primitive_nurbs_path_add(enter_editmode=False, location=(2, 0, 0))
    bpy.ops.object.transform_apply(location=True, rotation=False, scale=True)

    return bpy.context.active_object


def make_cube():
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))

    return bpy.context.active_object


def set_parent(a, b):
    a.parent = b


def make_curve_array(self, context):

    ob = bpy.context.active_object
    curve = make_curve()
    use_endcaps = bpy.context.scene.Props.curvearray_use_endcaps

    if( bpy.context.scene.Props.curvearray_use_active == True ):
        ob.location = (0, 0, 0)
    elif (use_endcaps == True):
        ob = make_cube()
    else:
        ob = make_curve_mesh(self, context)

    set_parent(curve, ob)
    utilities.set_smooth(ob)
    bpy.ops.object.modifier_add(type='ARRAY')
    bpy.context.object.modifiers["Array"].fit_type = 'FIT_CURVE'

    if( use_endcaps == False ):
        bpy.context.object.modifiers["Array"].use_merge_vertices = True

    bpy.ops.object.modifier_add(type='CURVE')
    bpy.context.object.modifiers["Curve"].object = curve
    bpy.context.object.modifiers["Array"].curve = curve

    return None


def make_curve_mesh(self, context):

    scale = bpy.context.scene.Props.curvearray_mesh_scale
    verts = [

        Vector((0, 0, 0)),
        Vector((0 , scale, 0)),
        Vector((scale, scale, 0)),
        Vector((scale, 0, 0)),

        Vector((0, 0, scale)),
        Vector((0, scale, scale)),
        Vector((scale, scale, scale)),
        Vector((scale, 0, scale)),

    ]

    edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 4], [1, 5], [2, 6], [3, 7], [4, 5], [5, 6], [6, 7], [7, 4]]
    faces = [[0, 1, 2 ,3], [4, 5, 6, 7], [0, 4, 7, 3], [1, 5, 6, 2]]

    mesh = bpy.data.meshes.new(name="CurveMesh_Test")
    mesh.from_pydata(verts, edges, faces)
    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)
    object_data_add(context, mesh, operator=self)
    ob = bpy.context.active_object

    return ob
