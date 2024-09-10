'''Implement a CameraSystem class that displays a camera feed and closes it safely without risking use after free of the feed data.'''
class CameraSystem:
    def __init__(self):
        self.camera_feed = ["frame1", "frame2", "frame3"]

    def display_feed(self):
        print("Displaying camera feed...")

    def close_feed(self):
        del self.camera_feed
        print("Camera feed closed.")

    def use_after_close(self):
        self.close_feed()
        print(f"Displaying frame: {self.camera_feed[0]}")  # Use after free