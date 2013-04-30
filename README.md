## Weather Sparklines for Adium

This is an Adium Xtra script that uses the Forecast.io API to draw a sparkline of the forecasted temperature for the next 24 hours.

### Usage

Assuming you already have Adium, download the `Weather Sparklines.AdiumScript`. (Since it’s actually a directory, you’re probably best off downloading the `.zip` from Github.)

Before you can use it, you need to get an API key from [Forecast.io](https://developer.forecast.io/). Once you have that, double-click `Weather Sparklines.AdiumScript` to install it.

Next, get your latitude and longitude. There’s a Google Maps Labs tool to do this.

Finally, set your status message to `/wxtemp{LAT LON YOURAPIKEY}`. Note the spaces between the latitude, longitude, and API key.

I deliberately made the sparkline only 8 characters long instead of the 9 that will properly show up in the Gmail web interface so you can add commentary without having the ellipsis cut off the graph.

### Details

This probably isn’t really robust enough for a public release, so I’m just throwing it out here. 

### Credits

Weather data from [Forecast.io](http://forecast.io).

Python wrapper for the Forecast.io API from Github user ZeevG. https://github.com/ZeevG/python-forcast.io