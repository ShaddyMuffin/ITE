import cv2
import os


# Function to get video for sign language
def get_video_for_sign_language(sign_language):
    video = cv2.VideoCapture(f"D:\\COding\\project ITE\\Suchet 2\\{sign_language}.mp4")
    return video

# Function to play video
def play_video(video):

    while True:
        ret, frame = video.read()
        # ret is storing boolean value where it indicates if it is getting frames to display or not
        if not ret:
            break

        # Resize the frame to a specific resolution (e.g., 640x480)
        target_resolution = (500,685)
        frame = cv2.resize(frame, target_resolution)

        cv2.imshow("Video", frame)
        
        # when pressed q it quits the video playing
        if cv2.waitKey(15) & 0xFF == ord('q'):
            break
    
    # Frees up all the resource which were used up
    video.release()

    cv2.destroyAllWindows()

# Function to handle video playback based on input words
def videoPlayer(lis):
    
    masterlist = ["hello", "whatsapp", "nice", "i", "learn", "sign", "whats", "your", "name", "where", "wheres", "your", "name", "please", "what", "favourite", "like", "you", "work", "time", "how", "sign", "meaning", "goodbye", "good", "morning", "night", "tired", "excited", "happy", "deaf", "hearing", "again", "slow", "yes", "not", "walk", "run", "food", "eat", "drink", "cook", "write", "draw", "read", "sing", "talk", "ride", "bath", "cry", "laugh", "play", "clean", "think", "listen", "dance", "finish", "forget", "go", "help", "more", "need", "right", "want", "scared", "bad", "busy", "sad", "same", "help", "father", "mother", "no", "cat", "afternoon", "milk", "like", "sorry", "interesting", "beautiful", "ugly", "big", "small", "hot", "cold", "fast", "loud", "quiet", "like", "friend", "enemy", "brother", "sister", "pride", "bicycle", "family", "eat", "breakfast", "lunch", "dinner", "hold", "hug", "human", "old", "new", "baby", "husband", "wife", "love", "you understand", "i dont understand", "whats wrong", "dont want", "see you later", "how are you", "i am fine", "excuse me", "meet you"]
    skipwords = []

    if lis in masterlist:
        video = get_video_for_sign_language(lis)
        play_video(video)
        return
    
    lis = lis.split()
    print("ASL :",end=" ")
    for i in lis:
        
        if i in skipwords:
            pass

        elif i in masterlist:
            video = get_video_for_sign_language(i)
            print(i,end=" ")
            play_video(video)

        
        else:
            for p in i:
                video = get_video_for_sign_language(p)
                print(p,end=" ")
                play_video(video)
    print()
    print()
    return
