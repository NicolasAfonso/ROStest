#!/usr/bin/env python

import nxt.locator
from nxt.sensor import *

b = nxt.locator.find_one_brick()

while (1):
	if Ultrasonic(b, PORT_4).get_sample() < 30:
		b.play_tone_and_wait(FREQ_E, 500)
		b.play_tone_and_wait(FREQ_D, 500)
		b.play_tone_and_wait(FREQ_C, 500)
		b.play_tone_and_wait(FREQ_D, 500)
		b.play_tone_and_wait(FREQ_E, 500)
		b.play_tone_and_wait(FREQ_E, 500)
		b.play_tone_and_wait(FREQ_E, 500)
