# Real-Time Car Counting Based on Digital Image Processing

---

## Project Overview
This project implements a **real-time car counting system** using **Digital Image Processing**. The system monitors parking lots, identifies changes in regions of interest (ROIs), and dynamically counts vehicles. It is designed for efficiency, scalability, and ease of use in real-world applications.
- **Real-Time Counting**: Dynamically displays car counts on video frames.
- **ROI Monitoring**: Customizable grid-based ROI for flexible setups.
- **Logging**: Logs detected changes to a file for tracking and analysis.
- **Visual Overlays**: Displays ROI boundaries and car counts in real-time.

---

## Prerequisites
- Python 3.8 or higher
- Libraries: OpenCV, NumPy
Install the required libraries:
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
- **Grid and Cell Size**: Update `GRID_SIZE` and `CELL_SIZE` for your parking lot layout.
- **Threshold**: Adjust the `THRESHOLD` value to fine-tune sensitivity for detecting changes.
