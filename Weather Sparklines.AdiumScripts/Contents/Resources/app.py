import math
import argparse
import forecastio

# Get your own API key at https://developer.forecast.io/
parser = argparse.ArgumentParser()
parser.add_argument("lat", type=float)
parser.add_argument("lon", type=float)
parser.add_argument("apikey", type=str)
args = parser.parse_args()
lat = args.lat
lon = args.lon
apikey = args.apikey

forecast = forecastio.Forecastio(apikey)
result = forecast.loadForecast(lat, lon)
byHour = forecast.getHourly()
hourtemps = []
for h, hourlyData in enumerate(byHour.data):
	# print hourlyData
	if h < 24:
	    hourtemps.append(hourlyData.temperature)
	else:
		break

# for debugging, use some hardcoded data to save API calls
# hourtemps = [71.82, 69.12, 67.16, 65.01, 63.57, 62.57, 60.72, 60.17, 59.24, 58.6, 57.73, 56.94, 55.71, 54.82, 55.95, 58, 60.94, 65.46, 68.08, 70.24, 72.29, 73.29, 73.97, 74.2]

# divide into 8 segments (length of gchat status - 1)
nsegs = 8
lendata = len(hourtemps)
segsize = int(math.ceil(float(len(hourtemps))/nsegs))
# print segsize
segdata = [[] for i in range(0,nsegs)]
segmeans = []

for i,temp in enumerate(hourtemps):
	segdata[int(math.floor(i/(lendata/(nsegs))))].append(temp)

# 3 happens to go into 24 evenly, but with longer data, chop them off
while len(segdata) > nsegs:
	segdata.pop()

for seg in segdata:
	segmeans.append(sum(seg)/len(seg))

minscale = int(min(segmeans))/10*10
maxscale = int(max(segmeans))/10*10+10

# ticks = {1: u'\u2581', 2: u'\u2582', 3: u'\u2583', 4: u'\u2584', 5: u'\u2585', 6: u'\u2586', 7: u'\u2587', 8: u'\u2588'}
ticks = {1: u'\u2581', 2: u'\u2582', 3: u'\u2583', 4: u'\u2585', 5: u'\u2586', 6: u'\u2587'}

binsize = float(maxscale-minscale)/len(ticks)
point = minscale
bins = []

for mean in segmeans:
	for i in range(1,len(ticks)+1):
		point += binsize
		if mean < point:
			bins.append(i)
			point = minscale
			break

out = ""
for i in bins:
	out += ticks[i].encode("utf8")
print out