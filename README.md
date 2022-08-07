# WiFi Motor Controller Board and Python Control

![](https://github.com/byronin/WiFi-MotorDriver/blob/main/Hardware/images/Robot_PNG.png)
## Contents
- PCB [Hardware](https://github.com/byronin/WiFi-MotorDriver/tree/main/Hardware "Hardware") files prepared for WiFi Motor Controller Board.
- [Arduino example](https://github.com/byronin/WiFi-MotorDriver/tree/main/Software/Arduino "Arduino example")  for WiFi Motor Controller Board.
- [Python sample](https://github.com/byronin/WiFi-MotorDriver/tree/main/Software/ws_joystick "Python sample")  for webspcket with using WiFi Motor Controller.
## Sponsor
[![](https://github.com/byronin/WiFi-MotorDriver/blob/main/Hardware/images/PCBWay_logo.png)](https://www.pcbway.com/project/shareproject/P10_Display_DMD_Text_Box_with_ESP8266_MQTT_P10_Display_Wi_Fi_Controller_4e9eb7f1.html)
#### Thanks to PCBWay for handling PCB production.
<a href="https://www.pcbway.com/project/shareproject/P10_Display_DMD_Text_Box_with_ESP8266_MQTT_P10_Display_Wi_Fi_Controller_4e9eb7f1.html"><img src="https://www.pcbway.com/project/img/images/frompcbway-1220.png" alt="PCB from PCBWay" /></a>
## Hardware & BOM
![PCBs](https://github.com/byronin/WiFi-MotorDriver/blob/main/Hardware/images/PCB_product.JPG "PCBs")
 [![This PCB Desing with Eagle ](https://www.snapeda.com/static/img/eda/eagle.png "PCB Desing with Eagle ")](https://www.autodesk.com/products/eagle/free-download "This PCB Desing with Eagle ") 
  ##### This PCB Desing with Eagle  
  
  ## Schematic
[![](https://github.com/byronin/WiFi-MotorDriver/blob/main/Hardware/schematic.png)

  
| PCB Components  | Package |Piece || PCB Components  | Package |Piece |  
| ------------- | ------------- |------------- |---------| ------------- | ------------- |------------- |
| ESP8266 Wi-Fi Module  | 12E | 1 pcs  || LM1117-3v3 | SOT-223  | 1 pcs |
| AON7401  | DFN 3x3_EP | 1 pcs || DRV8848  | SOP65P640X120-17N | 2 pcs |
| 10uf Cap mlcc | 0805  | 2 pcs  || 100uf Cap mlcc | 1210   | 2 pcs |
| 100nf Cap mlcc | 0603  | 8 pcs || 2.2uf Cap mlcc  | 0805  | 2 pcs  |
| 1K Resistor | 0603  | 1 pcs || 10K Resistor  | 0603  | 12 pcs  |
| 200mR Resistor | 1206  | 4 pcs || BLUE LED  | 0603  | 4 pcs  |
| GREEN LED  | 0603  | 4 pcs  || RED LED  | 0603  | 1 pcs |
| Header 1x4 ML  | 2.54-180  | 1 pcs  || Header 1x2 ML  | 2.54-180  | 2 pcs  |
| JUMPER 1x2   | 2.54  | 1 pcs  || jst 1x2 FML | 2.54-180  | 4 pcs  |  

[You can look BOM.txt for details.](https://github.com/byronin/WiFi-MotorDriver/blob/main/Hardware/BOM.txt "You can look BOM.txt")  

## Robot 
[![](https://github.com/byronin/WiFi-MotorDriver/blob/main/Robot/images/3D.png)](https://github.com/byronin/WiFi-MotorDriver/blob/main/Robot)
[You can look Robot 3D file for print.](https://github.com/byronin/WiFi-MotorDriver/tree/main/Robot "You can look Robot 3D file")
#### Shopping List

| Product  | Link || Product  | Link |
| ------------- | -------------|------------- | ------------- | ------------- |
|12mm Motor|[ Link](https://www.sumozade.com/product/micro-metal-gearmotor-hp-6v-650rpm " Link")||3.7V 450mAh Battery|[ Link](https://www.sumozade.com/product/profuse-1s-3-7v-450mah-25c-lipo-battery " Link")|

## Software 
[![](https://github.com/byronin/WiFi-MotorDriver/blob/main/Software/ws_joystick/images/main_py_exe.png)](https://github.com/byronin/WiFi-MotorDriver/blob/main/Software/ws_joystick)

[You can look main.py.](https://github.com/byronin/WiFi-MotorDriver/tree/main/Software/ws_joystick "You can look main.py") 

[![](https://github.com/byronin/WiFi-MotorDriver/blob/main/Software/ws_joystick/images/sender_py_exe.png)](https://github.com/byronin/WiFi-MotorDriver/blob/main/Software/ws_joystick)

[You can look sender.py.](https://github.com/byronin/WiFi-MotorDriver/tree/main/Software/ws_joystick "You can look sender.py") 

[You can use directly .exe in without build.](https://github.com/byronin/WiFi-MotorDriver/tree/main/Software/ws_joystick/dist "you can use directly .exe in without build") 
