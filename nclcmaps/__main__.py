# Copyright (c) 2022 Andreas Kvas
# See LICENSE for copyright/license details.

import nclcmaps
import matplotlib.pyplot as plt
import numpy as np


def main():
    cmap_names = nclcmaps.cm.colormaps()
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))

    nrows = len(cmap_names)
    figh = 0.35 + 0.15 + (nrows + (nrows - 1) * 0.1) * 0.22
    fig, axs = plt.subplots(nrows=nrows + 1, figsize=(6.4, figh))
    fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh,left=0.2, right=0.99)

    for ax, name in zip(axs, cmap_names):
        ax.imshow(gradient, aspect='auto', cmap=nclcmaps.cm.get_cmap(name))
        ax.text(-0.01, 0.5, name, va='center', ha='right', fontsize=10,transform=ax.transAxes)

    for ax in axs:
        ax.set_axis_off()

    plt.savefig('cmap_list.png', bbox_inches='tight', dpi=300)

if __name__ == "__main__":
    main()
