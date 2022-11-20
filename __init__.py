# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Save_DXF
                                 A QGIS plugin
 This plugin exports a laye to DXF file
                             -------------------
        begin                : 2022-11-20
        copyright            : (C) 2022 by Belal Magdy
        email                : belal.magdy.mahmoud@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Save_DXF class from file Save_DXF.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Save_DXF import Save_DXF
    return Save_DXF(iface)
