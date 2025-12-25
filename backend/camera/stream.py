import cv2

class CameraStream:
    """
    CameraStream encapsulates video stream access.
    """

    def __init__(self,stream_url:str):
        self.stream_url = stream_url
        self.cap = None

    def start(self):
        self.cap = cv2.VideoCapture(self.stream_url)
        if not self.cap.isOpened():
            raise RuntimeError("Unnable to open camera stream")
        
        return self
    
    def read(self):
        if self.cap is None:
            return None

        ret, frame = self.cap.read()
        if not ret or frame is None:
            return None

        return frame

    
    def stop(self):

        if self.cap is not None:
            self.cap.release()
            self.cap = None