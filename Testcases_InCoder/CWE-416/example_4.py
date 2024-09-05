class CameraSystem:
    def __init__(self):
        self.camera_feed = ["frame1", "frame2", "frame3"]

    def display_feed(self):
        print("Displaying camera feed...")

    def close_feed(self):
        del self.camera_feed
        print("Camera feed closed.")

    def safe_display(self):
        self.close_feed()
        if hasattr(self, 'camera_feed'):
            print(f"Displaying frame: {self.camera_feed[0]}")
        else:
            print("Camera feed is no longer available.")