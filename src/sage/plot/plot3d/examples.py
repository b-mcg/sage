r"""
Introduction

EXAMPLES::

    sage: x, y = var('x y')
    sage: W = plot3d(sin(pi*((x)^2+(y)^2))/2,(x,-1,1),(y,-1,1), frame=False, color='purple', opacity=0.8)
    sage: S = sphere((0,0,0),size=0.3, color='red', aspect_ratio=[1,1,1])
    sage: show(W + S, figsize=8)

    sage: plot3d(sin(sqrt(x^2 + y^2))/sqrt(x^2 + y^2), (x, -2*pi, 2*pi), (y, -2*pi, 2*pi), label3d=True, label_opts={'color':'red'})
    Graphics3d Object
    sage: plot3d(x^2 - y^2, (x, -5, 5), (y, -5, 5), label3d=True, axes_labels=['X-label', 'Y-label', 'Z-label']) 
    Graphics3d Object
"""



