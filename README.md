rhinoscripts
============

####Various utilities written in Rhinoscript and RhinoPython for 3d modeling and fabrication.

"RhinoScript is a scripting tool based on Microsoft's VBScript language. With RhinoScript, you can quickly add functionality to Rhino, or automate repetitive tasks."

See [http://wiki.mcneel.com/developer/rhinoscript]()

Also see [http://www.rhino3d.com/]()

####delunay.rvb

Calculates the delunay triangulation for a set of points.

See [http://en.wikipedia.org/wiki/Delaunay_triangulation]()

####minimal_spanning_tree.rvb

Calculates the minimal spanning tree for a set of points.

See [http://en.wikipedia.org/wiki/Minimum_spanning_tree]()

####recursive_cracking.rvb

Recursive Cracking triangulates a surface through a feedback loop which recursively divides itself according to the mean curvature of the surface at its position. Shallow areas of curvature on the surface are divided less and tighter areas of curvature are divided more creating a more accurate articulation of the surface being processed. this experiment serves as a tool for discretizing a curved surface into planar elements with dynamic geometric relationships.

####robo_cutsheet.rvb

While many cutsheet generating rhinoscripts exist none seem to tackle the problem of thickness in a model. This cutsheet script goes the extra mile allowing one to select a series of poly surfaces then generating a cutsheet from them with matching lables from model polysurfaces to cutsheet curves

####rotate_render.rvb

This simple script rotates the viewport at a desired interval and renders it, it is very useful when inserted into other rhinoscripts to produce an animation of the script being executed.

####score_to_perf.rvb

This is simple script exists to tackle the common problem in fabrication when one wants to bend or fold a material but creating a score line is not possible, it thus transforms selected lines in a model representing scores into a chain of holes whose diameter and spacing can be adjusted to create desired perforations for folding.

####surface_weave.rvb

TODO


####For more information you can check out my old site for now.

[http://code.robincwillis.com]()