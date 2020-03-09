# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


bl_info = {
    "name": "RedTools",
    "author": "Nick Redpath",
    "description": "Addon containing a suite of personal.",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "View3D",
    "warning": "",
    "category": "3D"
}

# Check if this add-on is being reloaded
if "bpy" in locals():
    # reloading .py files
    import importlib
    from .floorsnap import OT_Operator  # addon_props.py (properties are created here)
    importlib.reload(floorsnap)  # does this file need a def register() / def unregister() for the classes inside?

    from .panel import PT_Panel  # addon_panel.py (panel interface classes are created here)
    importlib.reload(panel)

    from .dynacyl import OBJECT_OT_add_object
    from .dynacyl import add_object_manual_map
    from .dynacyl import add_object_button
    importlib.reload(dynacyl)

    from .utilities import MakeHPOperator
    importlib.reload(utilities)

# or if this is the first load of this add-on
else:
    print("importing .py files")
    import bpy
    from .floorsnap import OT_Operator
    from .panel import PT_Panel
    from .dynacyl import OBJECT_OT_add_object
    from .dynacyl import add_object_manual_map
    from .dynacyl import add_object_button
    from .utilities import MakeHPOperator
    from .utilities import MakeCurveAOperator

def register():

    bpy.utils.register_class(OT_Operator)
    bpy.utils.register_class(PT_Panel)
    bpy.utils.register_class(OBJECT_OT_add_object)
    bpy.utils.register_class(MakeHPOperator)
    bpy.utils.register_class(MakeCurveAOperator)

    bpy.utils.register_manual_map(add_object_manual_map)
    bpy.types.VIEW3D_MT_mesh_add.append(add_object_button)


def unregister():

    bpy.utils.unregister_class(OT_Operator)
    bpy.utils.unregister_class(PT_Panel)
    bpy.utils.unregister_class(OBJECT_OT_add_object)
    bpy.utils.unregister_class(MakeHPOperator)
    bpy.utils.unregister_class(MakeCurveAOperator)

    bpy.utils.unregister_manual_map(add_object_manual_map)
    bpy.types.VIEW3D_MT_mesh_add.remove(add_object_button)


"""
import bpy
from .floorsnap import OT_Operator
from .panel import PT_Panel

classes = (OT_Operator, PT_Panel)

register, unregister = bpy.utils.register_classes_factory(classes)
"""
