from earth_gravity import wgs72
from sgp4io import twoline2rv

line1 = ('1 43013U 17073A   19261.50913870  .00000008  00000-0  24702-4 0  9998')
line2 = ('2 43013  98.7245 198.2889 0001389  73.3480 286.7849 14.19543304 94932')

satellite = twoline2rv(line1, line2, wgs72)
position, velocity = satellite.propagate(2000, 6, 29, 12, 50, 19)

print(position)
print(velocity)
