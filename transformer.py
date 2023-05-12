import cv2
import os

def video2image(filepath, outputpath):
    video = cv2.VideoCapture(filepath)

    if not video.isOpened():
        print("Could not open :", filepath)
        exit(0)

    length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)

    print("length :", length)
    print("width :", width)
    print("height :", height)
    print("fps :", fps)

    try:
        if not os.path.exists(outputpath):
            os.makedirs(outputpath)
    except OSError:
        print ('Error: Creating directory. ' +  outputpath)

    count = 0

    while(video.isOpened()):
        ret, image = video.read()
        if(not ret):
            break;        
        cv2.imwrite(outputpath + "/frame%s.jpg" % str(count).zfill(6), image)
        print('Saved frame number :', str(int(video.get(1))))
        count += 1
            
    video.release()

def image2video(filepath, outputfile, fps):
    print("Start image to video file")
    frame_array = []
    paths = [os.path.join(filepath , img ) for img in os.listdir(filepath)]
    for idx , path in enumerate(paths) : 
        img = cv2.imread(path)
        height, width, layers = img.shape
        size = (width,height)
        frame_array.append(img)

    out = cv2.VideoWriter(outputfile, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()

if __name__ == '__main__':
    video2image("./mp4/transformer.mp4", "./images")
    image2video("./images", "./mp4/transformer2.mp4", 30)
    print("test")
