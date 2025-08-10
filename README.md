# Real-Time Car Counting Using Digital Image Processing

---

## Project Overview

This project presents a **real-time vehicle counting system** based on **digital image processing** techniques. Designed for monitoring parking lots and similar environments, the system detects changes within defined regions of interest (ROIs) and dynamically counts the number of cars present.

Key features include:  
- **Real-Time Counting:** Continuously updates and displays vehicle counts on live video frames.  
- **Customizable ROI:** Grid-based ROI configuration allows flexible adaptation to different parking layouts.  
- **Event Logging:** Records detected changes with timestamps for tracking and analysis.  
- **Visual Overlays:** Highlights ROI boundaries and vehicle counts directly on the video stream.

---

## Prerequisites

- Python 3.8 or newer  
- Required Python libraries:  
  - OpenCV  
  - NumPy  

Install dependencies via pip:

```bash
pip install opencv-python numpy
```

---

## Usage
1. **Setup the Environment**:
   - Connect a camera or use a video file by modifying `cv2.VideoCapture(0)`.

2. **Adjust Grid and Cell Size**:
   - Configure `GRID_SIZE` (e.g., `(3, 3)`) and `CELL_SIZE` (e.g., `100`) to match your parking layout.

3. **Run the Script**:
   ```bash
   python car_counting.py
   ```

4. **Real-Time Monitoring**:
   - The car count is displayed on the video, and detected changes are logged to `car_counting_logs.log`.

---

## Example Output
- **Real-Time Display**:
  - Car count and ROI borders displayed on the video feed.
- **Log Example**:
  ```
  2024-01-01 12:00:00 - Change detected in region 3
  2024-01-01 12:01:15 - Change detected in region 7
  ```

---

## Customization
- **Grid Configuration**: Adjust GRID_SIZE and CELL_SIZE to align with your environment.
- **Detection Sensitivity**: Modify the THRESHOLD parameter to control sensitivity for detecting changes in ROI.
