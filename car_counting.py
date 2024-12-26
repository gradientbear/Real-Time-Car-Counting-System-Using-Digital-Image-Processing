import cv2
import time
import numpy as np
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename="car_counting_logs.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Constants for ROI (Regions of Interest) grid
GRID_SIZE = (3, 3)  # Grid of 3x3
CELL_SIZE = 100  # Each cell is 100x100 pixels
THRESHOLD = 40  # Threshold for detecting changes

def draw_borders_of_roi(frame, grid_size, cell_size):
    """Draw borders of regions of interest on the frame."""
    temp_frame = frame.copy()
    rows, cols = grid_size
    for i in range(rows):
        for j in range(cols):
            start_row, end_row = i * cell_size, (i + 1) * cell_size
            start_col, end_col = j * cell_size, (j + 1) * cell_size
            cv2.rectangle(temp_frame, (start_col, start_row), (end_col, end_row), (255, 255, 255), 2)
    return temp_frame

def initialize_regions(frame, grid_size, cell_size):
    """Initialize regions and calculate their reference mean intensities."""
    rows, cols = grid_size
    regions = []
    ref_means = []
    for i in range(rows):
        for j in range(cols):
            region = frame[i * cell_size:(i + 1) * cell_size, j * cell_size:(j + 1) * cell_size]
            regions.append(region)
            ref_means.append(np.mean(region))
    return regions, ref_means

def process_frame(frame, grid_size, cell_size, ref_means, threshold):
    """Process the frame, detect changes, and update reference means."""
    rows, cols = grid_size
    new_regions = []
    means = []
    changes = []
    for i in range(rows):
        for j in range(cols):
            region = frame[i * cell_size:(i + 1) * cell_size, j * cell_size:(j + 1) * cell_size]
            new_regions.append(region)
            means.append(np.mean(region))
    
    for idx, mean in enumerate(means):
        diff = abs(ref_means[idx] - mean)
        if diff > threshold:
            ref_means[idx] = mean
            changes.append(idx)
            logging.info(f"Change detected in region {idx}")
    
    return changes

def main():
    # Configure video capture
    video = cv2.VideoCapture(0)
    if not video.isOpened():
        print("Error: Could not open video stream.")
        return

    # Read the first frame and preprocess
    check, frame1 = video.read()
    if not check:
        print("Error: Could not read from video stream.")
        return

    frame1 = cv2.cvtColor(frame1, cv2.COLOR_RGB2GRAY)
    frame1 = cv2.flip(frame1, 1)
    frame1 = cv2.resize(frame1, (CELL_SIZE * GRID_SIZE[1], CELL_SIZE * GRID_SIZE[0]))

    # Initialize regions and reference means
    regions, ref_means = initialize_regions(frame1, GRID_SIZE, CELL_SIZE)

    # Initialize frame counter and car count
    frame_count = 0
    car_count = 0

    while True:
        frame_count += 1
        check, frame2 = video.read()
        if not check:
            print("Error: Could not read from video stream.")
            break

        frame2 = cv2.cvtColor(frame2, cv2.COLOR_RGB2GRAY)
        frame2 = cv2.flip(frame2, 1)
        frame2 = cv2.resize(frame2, (CELL_SIZE * GRID_SIZE[1], CELL_SIZE * GRID_SIZE[0]))

        # Detect changes in regions
        changes = process_frame(frame2, GRID_SIZE, CELL_SIZE, ref_means, THRESHOLD)
        if changes:
            car_count += len(changes)

        # Draw ROI borders and display car count
        display_frame = draw_borders_of_roi(frame2, GRID_SIZE, CELL_SIZE)
        cv2.putText(display_frame, f"Car Count: {car_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow("Parking Lot Monitoring", display_frame)

        # Break loop on 'q' key press
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    # Release resources
    video.release()
    cv2.destroyAllWindows()
    print("Video stream stopped.")

if __name__ == "__main__":
    main()
