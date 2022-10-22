nclcmaps Python Package
-----------------------

Use NCL color tables in Python.

The recommended way to install nclcmaps is in a [conda](https://docs.conda.io/en/latest/index.html) environment:
```
conda create -n nclcmaps_env
conda activate nclcmaps_env
```
Then, install all dependencies:
```
conda install matplotlib
```
To install the current development version of the package, first clone the repository or download the zip archive.
In the root directory of the package (i.e. the directory containing the ``setup.py`` file), running
```
python -m pip install .
```
will install the package.
If you want to modify or extend the package, you can install it in develop mode by running
```
python -m pip install -e .
```
instead.

![cmap_list](https://github.com/akvas/nclcmaps/blob/main/nclcmaps/data/cmap_list.png)

All currently supported colormaps can be listed by
```
>>> import nclcmaps
>>> nclcmaps.cm.colormaps()
['3gauss', '3saw', 'amwg', 'amwg256', 'amwg_blueyellowred', 'BkBlAqGrYeOrReViWh200', 'BlAqGrYeOrRe', 'BlAqGrYeOrReVi200', 'BlGrYeOrReVi200', 'BlRe', 'BlueDarkOrange18', 'BlueDarkRed18', 'BlueGreen14', 'BlueRed', 'BlueRedGray', 'BlueWhiteOrangeRed', 'BlueYellowRed', 'BlWhRe', 'BrownBlue12', 'Cat12', 'cb_9step', 'cb_rainbow', 'cb_rainbow_inv', 'CBR_coldhot', 'CBR_drywet', 'CBR_set3', 'CBR_wet', 'cmp_b2r', 'cmp_flux', 'cmp_haxby', 'cosam', 'cosam12', 'cyclic', 'default', 'detail', 'example', 'extrema', 'GHRSST_anomaly', 'GMT_cool', 'GMT_copper', 'GMT_drywet', 'GMT_gebco', 'GMT_globe', 'GMT_gray', 'GMT_haxby', 'GMT_hot', 'GMT_jet', 'GMT_nighttime', 'GMT_no_green', 'GMT_ocean', 'GMT_paired', 'GMT_panoply', 'GMT_polar', 'GMT_red2green', 'GMT_relief', 'GMT_relief_oceanonly', 'GMT_seis', 'GMT_split', 'GMT_topo', 'GMT_wysiwyg', 'GMT_wysiwygcont', 'grads_default', 'grads_rainbow', 'GrayWhiteGray', 'GreenMagenta16', 'GreenYellow', 'gscyclic', 'gsdtol', 'gsltod', 'gui_default', 'helix', 'helix1', 'hlu_default', 'hotcold_18lev', 'hotcolr_19lev', 'hotres', 'lithology', 'matlab_hot', 'matlab_hsv', 'matlab_jet', 'matlab_lines', 'mch_default', 'MPL_Accent', 'MPL_afmhot', 'MPL_autumn', 'MPL_Blues', 'MPL_bone', 'MPL_BrBG', 'MPL_brg', 'MPL_BuGn', 'MPL_BuPu', 'MPL_bwr', 'MPL_cool', 'MPL_coolwarm', 'MPL_copper', 'MPL_cubehelix', 'MPL_Dark2', 'MPL_flag', 'MPL_gist_earth', 'MPL_gist_gray', 'MPL_gist_heat', 'MPL_gist_ncar', 'MPL_gist_rainbow', 'MPL_gist_stern', 'MPL_gist_yarg', 'MPL_GnBu', 'MPL_gnuplot', 'MPL_gnuplot2', 'MPL_Greens', 'MPL_Greys', 'MPL_hot', 'MPL_hsv', 'MPL_jet', 'MPL_ocean', 'MPL_Oranges', 'MPL_OrRd', 'MPL_Paired', 'MPL_Pastel1', 'MPL_Pastel2', 'MPL_pink', 'MPL_PiYG', 'MPL_PRGn', 'MPL_prism', 'MPL_PuBu', 'MPL_PuBuGn', 'MPL_PuOr', 'MPL_PuRd', 'MPL_Purples', 'MPL_rainbow', 'MPL_RdBu', 'MPL_RdGy', 'MPL_RdPu', 'MPL_RdYlBu', 'MPL_RdYlGn', 'MPL_Reds', 'MPL_s3pcpn', 'MPL_s3pcpn_l', 'MPL_seismic', 'MPL_Set1', 'MPL_Set2', 'MPL_Set3', 'MPL_Spectral', 'MPL_spring', 'MPL_sstanom', 'MPL_StepSeq', 'MPL_summer', 'MPL_terrain', 'MPL_winter', 'MPL_YlGn', 'MPL_YlGnBu', 'MPL_YlOrBr', 'MPL_YlOrRd', 'ncl_default', 'NCV_banded', 'NCV_blu_red', 'NCV_blue_red', 'NCV_bright', 'NCV_gebco', 'NCV_jaisnd', 'NCV_jet', 'NCV_manga', 'NCV_rainbow2', 'NCV_roullet', 'ncview_default', 'nice_gfdl', 'nrl_sirkes', 'nrl_sirkes_nowhite', 'OceanLakeLandSnow', 'perc2_9lev', 'percent_11lev', 'posneg_1', 'posneg_2', 'prcp_1', 'prcp_2', 'prcp_3', 'precip2_15lev', 'precip2_17lev', 'precip3_16lev', 'precip4_11lev', 'precip4_diff_19lev', 'precip_11lev', 'precip_diff_12lev', 'precip_diff_1lev', 'psgcap', 'radar', 'radar_1', 'rainbow+gray', 'rainbow+white+gray', 'rainbow+white', 'rainbow', 'rh_19lev', 'seaice_1', 'seaice_2', 'so4_21', 'so4_23', 'spread_15lev', 'StepSeq25', 'sunshine_9lev', 'sunshine_diff_12lev', 'SVG_bhw3_22', 'SVG_es_landscape_79', 'SVG_feb_sunrise', 'SVG_foggy_sunrise', 'SVG_fs2006', 'SVG_Gallet13', 'SVG_Lindaa06', 'SVG_Lindaa07', 't2m_29lev', 'tbr_240-300', 'tbr_stdev_0-30', 'tbr_var_0-500', 'tbrAvg1', 'tbrStd1', 'tbrVar1', 'temp1', 'temp_19lev', 'temp_diff_18lev', 'temp_diff_1lev', 'testcmap', 'thelix', 'topo_15lev', 'uniform', 'ViBlGrWhYeOrRe', 'wgne15', 'wh-bl-gr-ye-re', 'WhBlGrYeRe', 'WhBlReWh', 'WhiteBlue', 'WhiteBlueGreenYellowRed', 'WhiteGreen', 'WhiteYellowOrangeRed', 'WhViBlGrYeOrRe', 'WhViBlGrYeOrReWh', 'wind_17lev', 'wxpEnIR']
```

License
-------

grates a free Open Source software released under MIT license.
See [License](LICENSE) for details.
