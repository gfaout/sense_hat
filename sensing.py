from sense_hat import SenseHat

sense = SenseHat()

while True:
	t = sense.get_temperature() * 9/5 + 32 #convert to Fahrenheit
	p = sense.get_pressure()
	h = sense.get_humidity()
	t = round(t,1)
	p = round(p,1)
	h = round(h,1)
#	msg = "Temp = %s, Pressure = %s, Humidity = %s " % (t,p,h)
	msg = "Temp = %s, RH = %s " % (t,h)
	if t <= 65:
		textcolor = [0,0,255]				#set text to blue
	elif t > 65 and t <= 85:
		textcolor = [0,255,0]				#set text to green
	else:
		textcolor = [255,0,0]				#set text to red
	sense.show_message(msg,scroll_speed=0.1, text_colour=textcolor, back_colour=[0,0,0])
