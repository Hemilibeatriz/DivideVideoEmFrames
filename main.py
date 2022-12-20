import cv2
import os

def video_to_frames(video, path_output_dir):
    # extrai os frames de um video(parametro) e os salva no diretório path_output_dir(parametro), nomeando os frames para "x.png" 
    # x é o index do frame
    vidcap = cv2.VideoCapture(video)
    count = 0
    while vidcap.isOpened():
        success, image = vidcap.read()
        if success:
            cv2.imwrite(os.path.join(path_output_dir, '%d.png') % count, image)
            count += 1
        else:
            break
    cv2.destroyAllWindows()
    vidcap.release()

video_to_frames('C:\\Users\\hemili\\Desktop\\TCC\\teste.mp4', 'C:\\Users\\hemili\\Desktop\\TCC\\frames')