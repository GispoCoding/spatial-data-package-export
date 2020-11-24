#  Gispo Ltd., hereby disclaims all copyright interest in the program SpatialDataPackageExport
#  Copyright (C) 2020 Gispo Ltd (https://www.gispo.fi/).
#
#
#  This file is part of SpatialDataPackageExport.
#
#  SpatialDataPackageExport is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  SpatialDataPackageExport is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with SpatialDataPackageExport.  If not, see <https://www.gnu.org/licenses/>.
import enum
from typing import Union, List

from ..qgis_plugin_tools.tools.exceptions import QgsPluginException
from ..qgis_plugin_tools.tools.i18n import tr
from ..qgis_plugin_tools.tools.resources import resources_path
from ..qgis_plugin_tools.tools.settings import get_setting, set_setting


@enum.unique
class Settings(enum.Enum):
    extent_precision = 8
    export_config_template = resources_path('templates', 'export-config.json')
    snapshot_template = resources_path('templates', 'snapshot-template.json')
    layer_format = 'memory'

    _options = {'layer_format': ['memory', 'geojson', 'none']}

    def get(self, typehint: type = str) -> any:
        """Gets the value of the setting"""
        return get_setting(self.name, self.value, typehint)

    def set(self, value: Union[str, int, float, bool]) -> None:
        """Sets the value of the setting"""
        options = self.get_options()
        if options and value not in options:
            raise QgsPluginException(tr('Invalid option. Choose something from values {}', options))
        set_setting(self.name, value)

    def get_options(self) -> List[any]:
        """Get options for the setting"""
        return Settings._options.value.get(self.name, [])
