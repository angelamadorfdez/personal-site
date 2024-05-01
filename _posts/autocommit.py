import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    DIRECTORY_TO_WATCH = "/"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'modified' or event.event_type == 'created':
            print(f"Evento detectado: {event.event_type} en {event.src_path}")
            print("Ejecutando 'git add .'")
            os.system('git add .')
            print("Ejecutando 'git commit'.")
            commit_result = os.system('git commit -m "Auto-commit"')
            if commit_result != 0:
                print("Commit fallido, posiblemente no hay cambios para commitear.")
            print("Ejecutando 'git push'.")
            os.system('git push')


if __name__ == '__main__':
    w = Watcher()
    w.run()
