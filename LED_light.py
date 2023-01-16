#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 23:41:10 2022

@author: ihpc
"""

import subprocess
from cgsensor import BME280

bme280 = BME280(0x77)

while bme280.forced():
    print('気温: {}℃'.format(bme280.temperature))
    
    if (bme280.temperature > 26):
        print('赤外線送信')
        subprocess.run(['cgir', 'send', 'tv_power'])

else:
    print('気温:{}℃'.format(bme280.temperature))
    subprocess.run(['cgir', 'send', 'tv_off'])
    