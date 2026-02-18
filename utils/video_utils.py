import cv2

def read_video(video_path):
    """
    Read video file and return list of frames
    """
    cap = cv2.VideoCapture(video_path)
    frames = []
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)  # Store frames (careful with large files!)
    
    cap.release()
    return frames

def save_video(frames, output_path, fps=30.0):
    """
    Save list of frames as video file
    """
    if not frames:
        print("No frames to save!")
        return
    
    height, width = frames[0].shape[:2]
    
    # Choose codec based on file extension
    fourcc = cv2.VideoWriter_fourcc(*'XVID') if output_path.endswith(".avi") else cv2.VideoWriter_fourcc(*'mp4v')

    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    for frame in frames:
        if frame is None:
            continue  # Avoid writing invalid frames
        out.write(frame)

    out.release()
    print(f"Video saved to {output_path}")
