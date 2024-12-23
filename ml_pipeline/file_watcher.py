from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import subprocess

class NewDataHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_file:
            print(f"New data file detected: {event.src_path}")
            subprocess.run(["python", "retrain.py", event.src_path])

if __name__ == "__main__":
    path = "./data/new_data"
    event_handler = NewDataHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()