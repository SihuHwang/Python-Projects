from PIL import Image
from PIL.ExifTags import TAGS
import webbrowser

image = Image.open("20200120_202301092.jpg")
info = image._getexif()
image.close()

# print(info)

taglabel = {}

for tag, value in info.items():
    decode = TAGS.get(tag, tag)
    taglabel[decode] = value

# print(taglable)

# print(taglabel['DateTimeOriginal'])
# print(taglabel['DateTimeDigitized'])
# print(taglabel['DateTime'])
# print(taglabel['GPSInfo'])

exifGPS = taglabel['GPSInfo']
latData = exifGPS[2]
lonData = exifGPS[4]

latDeg = latData[0][0] / float(latData[0][1])
latMin = latData[1][0] / float(latData[1][1])
latSec = latData[2][0] / float(latData[2][1])

lonDeg = lonData[0][0] / float(lonData[0][1])
lonMin = lonData[1][0] / float(lonData[1][1])
lonSec = lonData[2][0] / float(lonData[2][1])


Lat = str(int(latDeg)) + "°" + str(int(latMin)) + "'" + str(latSec) + "\"" + exifGPS[1]
Lon = str(int(lonDeg)) + "°" + str(int(lonMin)) + "'" + str(lonSec) + "\"" + exifGPS[3]

print(Lat, Lon)

webbrowser.open_new("https://www.google.com/maps/place/"+Lat+"+"+Lon)

Lat = (latDeg + (latMin + latSec / 60.0) / 60.0)
if exifGPS[1] == 'S': Lat = Lat * -1
Lon = (lonDeg + (lonMin + lonSec / 60.0) / 60.0)
if exifGPS[3] == 'W': Lon = Lon * -1

print(Lat, ",", Lon)








