import threading
import tkinter as tk


class BarcodeListThread(threading.Thread):
    def __init__(self, server, manager):
        super().__init__()
        self._stop_event = threading.Event()
        self.server = server
        self.manager = manager


    def stop(self):
        self._stop_event.set()

    def run(self):
        while not self._stop_event.is_set():
            # ここにスレッドの処理を記述します
            self.server.socket_accept()
            while True:
                data = self.server.recv_data()
                if not data:
                    break
                inventory = self.manager.create_inventory(inv_id=data.decode('utf-8'))
                if not inventory.name:
                    self.create_error_widget()

                else:
                    tk.listBox.insert(tk.END, inventory.id + " | " + inventory.name)
                    tk.inv_list.append(inventory)

thread = BarcodeListThread()