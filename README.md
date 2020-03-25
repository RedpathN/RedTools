# RedTools

FloorSnap:
For modular kits, a convenient tool to snap the object origin to a lower vertice, and the object to world origin. Will prioritise lowest vertice in the model, and if multiple exist will search out the front-left most vertice to set as origin. Can be configured with options in the panel

Make HighPoly:
Adds angle-based bevel and subsurf modifiers with some preconfigured settings. Can be changed at any point via modifier panel.

Make Weighted Normals:
Adjusts bevel from MakeHighPoly (or creates if none found) bevel modifier to one segment, removes subsurf and adds a weighted normal modifier. Can be adjusted via modifiers.

Make Cage:
Duplicates current object at same location, renaming to ObjectName_cage and adds displaces verts on normals via Displace modifier. Can be adjusted via modifiers. Optionally, can toggle to rename original object to ObjectName_low to keep naming consistent.

Add DynaCyl:
Creates a cylindrical mesh out of a few spun vertices, allowing for later adjustment of face count. On creation, can use object creation panel to toggle end caps, add thickness, choose if floored or center origin, add HighPoly modifiers, and choose to keep faceting/make smooth aswell as change dimensions in the form of Height/Radius

Add Curve Array:
Parents active object to a curve, 0's object location and sets up array/curve modifiers to work by default on X. If no active selected it can create a new cube with appropriate modifiers or a custom cube with no endcaps for merging verts. 

Add NineTile:
Adds a 2x2 plane, tiled at 3x3, with overlapping UVs. Used as LP for painting tileables in substance etc. Works great with Make Cage, then just sandwich a trimsheet/tile mesh as a HP in the middle for easy baking.
