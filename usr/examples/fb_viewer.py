import sensor, time
sensor.reset()
# Set sensor parameters
sensor.set_contrast(1)
sensor.set_gainceiling(8)

# Set sensor pixel format
sensor.set_framesize(sensor.QVGA)
sensor.set_pixformat(sensor.JPEG)
sensor.set_quality(95)

clock = time.clock()

while (True):
  clock.tick()
  image = sensor.snapshot()
  time.sleep(1)
  print(clock.fps())
