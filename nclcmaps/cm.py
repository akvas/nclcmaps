# Copyright (c) 2021 Andreas Kvas
# See LICENSE for copyright/license details.

"""
Main functions for generating NCL color tables.
"""

import pkg_resources
import tarfile
import os.path
from matplotlib.colors import LinearSegmentedColormap, ListedColormap


def get_cmap(name, force_linear=False):
    """
    Return NCL color table as matplotlib colormap. Use nclcmaps.cm.colormaps() to list all available color tables.

    Parameters
    ----------
    name : str
        The name of the colormap. Append "_r" to reverse the color order.
    force_linear : bool
        If true, the color table is interpolated to yield a linear transition between the given colors

    Returns
    -------
    cmap : ListedColormap or LinearSegmentedColormap
        The color table as ListedColormap (or LinearSegmentedColormap if force_linear=True)

    Raises
    ------
    ValueError
        If the requested color table name is not found.
    """
    reverse = name.endswith('_r')
    if reverse:
        name = name[0:-2]

    with tarfile.open(pkg_resources.resource_filename('nclcmaps', 'data/ncl_colormaps.tar')) as f:
        file_names = f.getnames()
        for file_name in file_names:
            root, _ = os.path.splitext(file_name)
            cmap_name = os.path.split(root)[-1]
            if name.lower() == cmap_name.lower():
                target_file_name = None
                for ext in ('.ncmap', '.rgb', '.gp'):
                    target_file_name = root + ext
                    if target_file_name in file_names:
                        break

                is_unnormalized = False
                rgb = []
                for line in f.extractfile(target_file_name).readlines():
                    try:
                        color = tuple(float(v) for v in line.split()[0:3])
                    except ValueError:
                        continue

                    if len(color) < 3:
                        continue

                    is_unnormalized = True if is_unnormalized else color[0] > 1 or color[1] > 1 or color[2] > 1
                    rgb.append(color)

                if is_unnormalized:
                    for k in range(len(rgb)):
                        rgb[k] = tuple([c / 255 for c in rgb[k]])

                if force_linear:
                    cmap = LinearSegmentedColormap.from_list(name, rgb)
                else:
                    cmap = ListedColormap(rgb, name)

                return cmap.reversed() if reverse else cmap

    raise ValueError(f'Color table "{name}" not found. Use nclcmaps.cm.colormaps() to list all available colormaps.')


def colormaps():
    """
    Create a list of all available color tables.

    Returns
    -------
    colormap_list : list of str
        A list of all available color tables.
    """
    colormap_list = []
    with tarfile.open(pkg_resources.resource_filename('nclcmaps', 'data/ncl_colormaps.tar')) as f:
        for file_name in f.getnames():
            root, _ = os.path.splitext(file_name)
            cmap_name = os.path.split(root)[-1]
            if not cmap_name.startswith('.') and not cmap_name in colormap_list:
                colormap_list.append(cmap_name)

    return colormap_list
