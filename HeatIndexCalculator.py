# HeatIndexCalculator.py
# Your job is to write a function in HeatIndexCalculator.py (call
# it **calculateHeatIndex()** that calculates the heat index
# factor based on the Heat Index Calculator from
# Calculator.net (http://www.calculator.net/heat-index-calculator.html)

# Define Function below
# be sure to return an integer
import HeatIndexCalculator

def calculateHeatIndex(relativeHumidity, temperature):
    RH = relativeHumidity
    T = temperature

        # using the formula from http://www.wpc.ncep.noaa.gov/html/heatindex_equation.shtml
    return round(-42.379 + 2.04901523*T + 10.14333127*RH - .22475541*T*RH - .00683783*T*T - .05481717*RH*RH + .00122874*T*T*RH + .00085282*T*RH*RH - .00000199*T*T*RH*RH)

if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    pass # remove or comment out this line if you wish to test the function
