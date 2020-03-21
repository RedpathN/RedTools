import bpy
import bmesh
import mathutils


# FUNC----------------------------------------------------
class OT_Operator(bpy.types.Operator):
    bl_idname = "redtools.floorsnap"
    bl_label = "Floor Snap"
    bl_description = "Snap an object's origin to it's floor"

    def execute(self, context):
        # Get the active mesh
        me = bpy.context.object
        apply_move(me)
        bm = make_bmesh(me)
        verts = bm.verts  # assign bm verts

        # -------------------------------------------------------------

        zList = find_lowest(verts)
        xList = sort_x(zList)
        yList = sort_y(zList)

        update_obj(bm, me)
        move_obj(me, xList, yList, zList)
        apply_move(me)

        # debug(xList, yList, zList)

        bm.free()
        me.data.update()
        # Print debug text

        return {'FINISHED'}


def make_bmesh(me):
    bm = bmesh.new()  # create an empty BMesh
    bm.from_mesh(me.data)  # fill it in from a Mesh
    return bm


def find_lowest(verts):
    verts.ensure_lookup_table()
    l1 = []
    firstvert = verts[0]
    lowest = firstvert.co.z

    for v in verts:
        if v.co.z < lowest:
            l1.clear()
            lowest = v.co.z
            l1.append(v)
        elif v.co.z == lowest:
            l1.append(v)
    return l1


def get_x(v):
    return v.co.x


def get_y(v):
    return v.co.y


def get_z(v):
    return v.co.z


def sort_x(l1):
    l1 = sorted(l1, key=get_x)
    return l1


def sort_y(l1):
    l1 = sorted(l1, key=get_y)
    return l1


def to_seq(l1):
    l1 = list(l1)
    return l1


# Modify the BMesh, can do anything here...
def move_obj(me, xList, yList, zList):
    vec = mathutils.Vector((-get_x(xList[0]), -get_y(yList[0]), -get_z(zList[0])))
    me.location += vec


def apply_move(me):
    bpy.ops.object.transform_apply(location=True, rotation=False, scale=True)
    me.location = 0, 0, 0


def update_obj(bm, me):
    me.data.update()
    bm.to_mesh(me.data)


def debug(xList, yList, zList):
    print("============================NEW EXECUTE==============================")
    print("zList:")
    for v in zList:
        print(v.co)
    print_line_break()
    print("xList:")
    for v in xList:
        print(v.co)
    print_line_break()
    print("yList:")
    for v in yList:
        print(v.co)


def print_line_break():
    print("\n -----------------------------------")
