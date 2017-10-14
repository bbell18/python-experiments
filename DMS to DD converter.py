print 'Convert longitude and latitude from degrees, minutes, seconds to decimal degrees.'
print 'This converter can only handle minutes values at 119 and below or seconds at value 60 or below. If your values are different, please convert before placing them into this converter or the calculations will be inaccurate.' 
print 'Negative longitude values are for the western hemisphere for this converter.'
print 'Decimal values can be inserted into D, M, and S fields.'
dmsLongDegrees = float(raw_input('Degrees of longitude: '))
dmsLongMinutes = float(raw_input('Minutes of longitude: '))
dmsLongSeconds = float(raw_input('Seconds of longitude: '))
dmsLongEorW = raw_input('Degrees W or E?: ')

dmsLatDegrees = float(raw_input('Degrees of latitude: '))
dmsLatMinutes = float(raw_input('Minutes of latitude: '))
dmsLatSeconds = float(raw_input('Seconds of latitude: '))
dmsLatNorS = raw_input('Degrees N or S?: ')


# Convert longitude DMS -> DD

if (dmsLongMinutes <= 60):
    ddLongMinutes = float(dmsLongMinutes / 60)
    ddLongSeconds = float(dmsLongSeconds / 3600)
    ddLongDegrees = float(dmsLongDegrees + ddLongMinutes + ddLongSeconds)
else:
    ddLongMinutes = float(1 - (dmsLongMinutes / 60))
    ddLongSeconds = float(1 - (dmsLongMinutes / 3600))
    ddLongDegrees = float(1 + (dmsLongDegrees + ddLongMinutes + ddLongSeconds))
    
if (dmsLongEorW == 'E'):
    ddLongSign = ''
elif (dmsLongEorW == 'W'):
    ddLongSign = '-'
else:
    print 'Insert only E or W with no spaces for Degrees W or E question.'

print 'Longitude: ', ddLongDegrees, ' degrees'
print '   Calculation check:', ddLongMinutes, ' minutes', ddLongSeconds, ' seconds'

# Convert latitude DMS -> DD

if (dmsLatMinutes <= 60):
    ddLatMinutes = float(dmsLatMinutes / 60)
    ddLatSeconds = float(dmsLatSeconds / 3600)
    ddLatDegrees = float(dmsLatDegrees + ddLatMinutes + ddLatSeconds)
else:
    ddLatMinutes = float(1 - (dmsLatMinutes / 60))
    ddLatSeconds = float(1 - (dmsLateconds / 60))
    ddLatDegrees = float(1 + (dmsLatDegrees + ddLatMinutes + ddLatSeconds))


if (dmsLatNorS == 'N'):
    ddLatSign = ''
elif (dmsLatNorS == 'S'):
    ddLatSign = '-'
else:
    print 'Insert only N or S with no spaces for Degrees N or S question.'

print 'Latitude: ', ddLatSign, ddLatDegrees, ' degrees'
print '   Calculation check:', ddLatMinutes, ' minutes', ddLatSeconds, ' seconds'

    
