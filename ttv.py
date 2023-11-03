# ChatGPT
import speech_recognition as sr
import cv2
import stt


# Function to get video for sign language
def get_video_for_sign_language(sign_language):
    video = cv2.VideoCapture(f"PATH\\TO\\{sign_language}.mp4")
    return video

# Function to play video
def play_video(video):

    while True:
        ret, frame = video.read()
      
        if not ret:
            break

        # Resize the frame to a specific resolution (e.g., 640x480)
        target_resolution = (500,685)
        frame = cv2.resize(frame, target_resolution)

        # flips the videos y-axis
        frame = cv2.flip(frame, 1)


        cv2.imshow("Video", frame)
        
        if cv2.waitKey(15) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

# Function to handle video playback based on input words
def videoPlayer(lis):
    nonowords = ["fuck","madrachod","bahan chod","ass hole","bitch"]
    masterlist = ["hello","hi","i love you"]

    if lis in masterlist:
        video = get_video_for_sign_language(lis)
        play_video(video)
        quit()
    lis = lis.split()
    for i in lis:
        if i in nonowords:
            video = get_video_for_sign_language("curse")
            play_video(video)
        elif i in masterlist:
            video = get_video_for_sign_language(i)
            play_video(video)
        else:
            for p in i:
                video = get_video_for_sign_language(p)
                play_video(video)


# Function to run the model
def run_model():
    text = stt.convt()
    return text
