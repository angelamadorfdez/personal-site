import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    DIRECTORY_TO_WATCH = "/"  # Asegúrate de cambiar esto por la ruta correcta de tu directorio

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
            os.system('git add .')
            print("Intentando commitear cambios.")
            # Ejecutamos git commit y verificamos si fue exitoso
            commit_status = os.system('git commit -m "Auto-commit"')
            if commit_status == 0:
                print("Commit exitoso, realizando push a repositorio remoto.")
                os.system('git push')
            else:
                print("No se realizó commit, probablemente porque no hay cambios que commitear.")

if __name__ == '__main__':
    w = Watcher()
    w.run()
