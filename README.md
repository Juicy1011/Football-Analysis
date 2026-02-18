# Football Match Analysis using YOLOv8 and Computer Vision

This project is a computer vision-based football match analysis tool. It uses **YOLOv8** for object detection (players, referees, and the ball), **ByteTrack** for robust tracking, and **K-Means Clustering** for automated team assignment based on jersey colors.

## ⚽ Features
- **Object Detection & Tracking:** Detects and tracks players, referees, and the ball across video frames.
- **Team Assignment:** Automatically classifies players into teams using color segmentation and K-Means clustering on their jerseys.
- **Ball Possession Analysis:** Calculates which player and team has possession of the ball at any given time.
- **Ball Interpolation:** Smooths out ball movement by interpolating positions when the ball is occluded or moving too fast for detection.
- **Annotation Overlay:** Draws ellipses for players, triangles for ball possession, and a dynamic team possession statistics dashboard.

## 🛠️ Tech Stack
- **AI Model:** YOLOv8 (Ultralytics)
- **Tracking:** ByteTrack (Supervision)
- **Processing:** OpenCV, NumPy, Pandas
- **Machine Learning:** Scikit-learn (K-Means)

## 📁 Project Structure
```text
├── .qodo/                  # Inference tests
├── player_ball_assigner/   # Logic for player-ball proximity
├── team_assigner/          # Team color identification logic
├── trackers/               # Main tracking class and drawing utilities
├── utils/                  # Helper functions for BBoxes and Video IO
├── training/               # Training configurations
└── main.py                 # Project entry point
🚀 Getting Started
1. Prerequisites
Ensure you have Python 3.8+ installed.
2. Install Dependencies
code
Bash
pip install ultralytics supervision opencv-python numpy pandas scikit-learn
3. Model Weights
The project requires a YOLOv8 model trained on football data.
Place your trained model in a models/ folder.
Name it best.pt (or update the path in main.py).
4. Running the Analysis
Place your input video in an input_video/ folder and run:
code
Bash
python main.py
The output will be saved in the output_videos/ directory.
📊 How it Works
Tracking: The Tracker class initializes the YOLO model and wraps around ByteTrack to maintain consistent IDs for players across frames.
Team Identification: We crop the player's jersey area, apply K-Means clustering to find the dominant color, and then group these colors into two team clusters.
Possession Logic: We measure the distance between the ball and the players' feet. If a player is within a certain pixel threshold, they are assigned ball control.
Interpolation: Since the ball is small and fast, detection sometimes drops. We use Pandas interpolation to fill in those missing frames for a smooth visual experience.
📝 Note on Large Files
Large files such as .pt (model weights), .mp4/.avi (videos), and .pk1 (stubs) are excluded from this repository to keep it lightweight.
Developed as part of a Football Analysis AI project.
code
Code
### To add this to your GitHub:
1. Save the file as `README.md`.
2. Run these commands:
   ```cmd
   git add README.md
   git commit -m "Add professional README"
   git push origin main
