import savefoto
import savef2

resultado = ''
#resultado = savefoto.save_frame_camera_key(0, 'images', 'screen')
#resultado = savefoto.save_frame_camera_key(0,1, 'images', 'screen',200,1,700,400,200,450)
#resultado = savefoto.save_frame_camera_key('rtsp://admin:Piedras3980@10.128.10.250:554',0, 'images', 'screen',200,1,600,400,200,450)
resultado = savef2.save_frame_camera_key('rtsp://admin:Piedras3980@10.128.10.250:554',0, 'images', 'screen',200,1,600,400,200,450)
#resultado = savef2.save_frame_camera_key(0,1, 'images', 'screen',200,1,600,400,200,450)
print(resultado)
