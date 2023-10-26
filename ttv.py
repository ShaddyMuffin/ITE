import speech_recognition as sr
import cv2
import stt

def get_video_for_sign_language(sign_language):
    video = cv2.VideoCapture(f"PATH TO MP4 files")
    return video
  
def play_video(video):
    while True:
        ret, frame = video.read()
      
        if not ret:
            break
      
        cv2.imshow("Video", frame)
        
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

def run_model():
    # audio = sr.Recognizer().record(sr.Microphone())
    text = stt.convt()
    video = get_video_for_sign_language(text)
    play_video(video)

if __name__ == "__main__":
    run_model()
