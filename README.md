# Spatial Data Package Export
![](https://github.com/cividi/spatial-data-package-export/workflows/Tests/badge.svg)
[![codecov.io](https://codecov.io/github/cividi/spatial-data-package-export/coverage.svg?branch=master)](https://codecov.io/github/cividi/spatial-data-package-export?branch=master)
![](https://github.com/cividi/spatial-data-package-export/workflows/Release/badge.svg)

QGIS plugin to export data and styles to Spatial Data Packages that can be uploaded on the [Spatial Data Package Platform](https://github.com/cividi/spatial-data-package-platform), e.g. [gemeindescan.ch](https://gemeindescan.ch).

This tool exports spatial data packages. The data package specification is based on the [Frictionless Data toolkit](https://frictionlessdata.io/).
Main development by [Gispo Ltd](https://www.gispo.fi/en/home/).

### Minimum Requirements

| | |
|-|-|
| [QGIS](https://qgis.org/) | 3.10 |
| [Python](https://www.python.org/downloads/) | 3.6 |
| [Platform](https://github.com/cividi/spatial-data-package-platform/releases) | 0.2 |


### Installation instructions

The plugin can be installed by downloading a release from this
repository or a stable release from the [QGIS Plugin Repository](https://plugins.qgis.org/plugins/SpatialDataPackageExport/).

To download from GitHub:

1. Download the latest release from [Releases](https://github.com/cividi/spatial-data-package-export/releases).

    - [Latest stable version](https://github.com/cividi/spatial-data-package-export/releases/download/0.2.0/SpatialDataPackageExport.0.2.0.zip)

2. Launch QGIS and the plugins menu by selecting Plugins - Manage and Install Plugins from the top menu.

3. Select the Install from ZIP tab, browse to the zip file you just downloaded, and click Install Plugin!

#### Troubleshooting notes

> Unable to Install Plugin - No Python Support Detected

[Some versions of QGIS](https://github.com/qgis/QGIS/issues/32135) on some operating systems come without a working python environment. Seen on fresh installs on Fedora 33.

### Supported QGIS Symbol Types and Symbol Layer Types

**Geometry Types**
- Point / MultiPoint
- Linestring / MultiLinestring
- Polygon / MultiPolygon

**Symbol Types**
- Single Symbol
- Categorized Symbol
- Graduated Symbol

**Symbol Layer Types**
- Simple Fill (Polygon)
- Centroid Fill Circle (Polygon, Point)
- Outline: Simple Line (Polygon)
- Simple Line (Linestring)

**Styling Properties**
- Size (only circle and line layers)
- Fill color (color and opacity, only fill layers)
- Stroke color (color and opacity)
- Stroke width

### Development

Refer to [development](docs/development.md) to instructions for developing the plugin.

## License
This plugin is licenced with
[GNU Genereal Public License, version 3](https://www.gnu.org/licenses/gpl-3.0.html).
See [LICENSE](LICENSE) for more information.
