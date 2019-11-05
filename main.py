# import geopandas
import numpy
import pandas
import scipy
import sklearn
import shapely
import pyproj
import fiona
import geopandas

def main(dict):
    return {
        "pandas": pandas.__version__,
        "sklearn": sklearn.__version__,
        "scipy": scipy.__version__,
    	"numpy": numpy.__version__,
		"pandas": pandas.__version__,
		"scipy": scipy.__version__,
		"sklearn": sklearn.__version__,
		"shapely": shapely.__version__,
		"pyproj": pyproj.__version__,
		"fiona": fiona.__version__,
		"geopandas": geopandas.__version__
    }
