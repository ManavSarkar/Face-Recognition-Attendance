import cv2
import face_recognition
# Video class to return frames
class Video:
    def __init__(self) -> None:
        self.video = cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()
    def get_frame(self):
        ret,frame=self.video.read()
        faces = face_recognition.face_locations(frame)
        for y1,x2,y2,x1 in faces:
            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
        ret,jpg = cv2.imencode('.jpg',frame)
        return jpg.tobytes()