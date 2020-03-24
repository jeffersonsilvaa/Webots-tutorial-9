# **************************************************************
# Project 09 - Disciplina de robótica Móvel UFC / IFCE / LAPISCO
#       Simulação 09 com Drone Mavic 2 Pro - Webots R2020a
#              Veículo BMW X5 - controles básicos
#        Python 3.5 na IDE Pycharm - controller <extern>
#                By: Jefferson Silva Almeida
#                       Data: 23/03/2020
# **************************************************************

from controller import Robot
from vehicle import Driver

TIME_STEP = 64 # ms
MAX_SPEED = 80 # km/h

driver = Driver()

speedFoward = 10 # km/h
speedBrake = 0 # km/h
cont = 0

while driver.step() != -1:

    if cont < 1000:
        driver.setCruisingSpeed(speedFoward) # acelerador (velocidade)
        driver.setSteeringAngle(-0.7) # volante (giro)
        # print('speed up %d' % cont)
        driver.setDippedBeams(True) # farol ligado
        driver.setIndicator(2) # 0 -> OFF  1 -> Right   2 -> Left
    elif cont > 1000 and cont < 1100:
        driver.setCruisingSpeed(speedBrake)
        driver.setBrakeIntensity(1.0) # intensidade (0.0 a 1.0)
        driver.setDippedBeams(False) # farol apagado
        # print('braked %d' % cont)
    elif cont > 1100 and cont < 1400:
        driver.setCruisingSpeed(-speedFoward)
        driver.setSteeringAngle(-0.7)
        # print('speed up %d' % cont)
    elif cont > 1400 and cont < 1500:
        driver.setCruisingSpeed(speedBrake)
        driver.setBrakeIntensity(1.0)
        driver.setDippedBeams(False) # farol apagado
        # print('braked %d' % cont)
    elif cont > 1500:
        cont = 0

    print('speed (km/h) %0.2f' % driver.getCurrentSpeed())

    cont += 1
