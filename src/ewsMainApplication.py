import time
import threading
from tkinter import messagebox
import tkinter as tk
import sys
from ewsDBManager import DBManager
from ewsTcpServer import Server
from ewsLogger import Logger
# TODO: add comments


class MainApplication(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Project Management System")
        self.master.geometry("1000x1000")

        self.user_name = ""
        self.admin_user_nmae = "admin"
        self.project_name = ""
        self.item_num = 0
        self.HOST = "192.168.1.90"
        self.PORT = 8080
        self.inv_list = []

        self.button_states = []
        self.spin_box_list = []
        
        self.server = Server(self.HOST, self.PORT)
        self.manager = DBManager()
        self.stop_event = threading.Event()

        self.recv_thread = threading.Thread(target=self.update_listbox)
        self.recv_thread.start()
        self.create_widgets()
        self.server.create_socket()
        


    def create_widgets(self): # next : confirm_username_project
        # Username and Project name Entry
        self.destroy_current_widgets()   
        self.username_label = tk.Label(self.master, text="Enter your Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack()
        
        self.project_label = tk.Label(self.master, text="Enter Project name:")
        self.project_label.pack()
        self.project_entry = tk.Entry(self.master)
        self.project_entry.pack()

        self.confirm_button = tk.Button(self.master, text="Confirm", command=self.confirm_username_project)
        self.confirm_button.pack()

    def confirm_username_project(self): # next : create_list_widgets
        self.user_name = self.username_entry.get()
        self.project_name = self.project_entry.get()
        # break if admin user
        if self.user_name.lower() == self.admin_user_nmae:
            self.server.clear_connection()
            self.stop_event.set()
            
            print(1)
            self.master.destroy()
            print(2)
            self.master.quit()
            print(3)
            time.sleep(5)
            self.recv_thread.join()
            print(4)
            sys.exit()

        if self.user_name and self.project_name:
            #TODO: add check user list method
            self.create_list_widgets()

    def create_list_widgets(self): # next : create_return_take_widget
        self.destroy_current_widgets()
        self.listBox = tk.Listbox(self.master, width=40, height=20)
        self.listBox.pack()

        self.del_button = tk.Button(self.master, text="Del", command=self.delete_item)
        self.del_button.pack()
        
        self.ok_button = tk.Button(self.master, text="OK", command=self.create_return_take_widget)
        self.ok_button.pack()

    def delete_item(self):
        self.selected_item_index = self.listBox.curselection()
        if not self.selected_item_index:
            return
        self.listBox.delete(self.selected_item_index)
        self.inv_list.pop(int(self.selected_item_index[0]))

    def update_listbox(self):
        while not self.stop_event.is_set():
            self.server.socket_accept()
            while True:
                data = self.server.recv_data()
                if not data:
                    break
                inventory = self.manager.create_inventory(inv_id=data.decode('utf-8'))
                if not inventory.name:
                    self.create_error_widget()

                else:
                    self.listBox.insert(tk.END, inventory.id + " | " + inventory.name)
                    self.inv_list.append(inventory)

    def create_return_take_widget(self):  # next : create_final_check_widget
        self.destroy_current_widgets()
        self.return_take_label = tk.Label(self.master, text="Do you want to return or take an item?")
        self.return_take_label.pack()

        for i, item in enumerate(self.inv_list):
            self.return_take_label = tk.Label(self.master, text=item.name)
            self.return_take_label.pack()
            
            button_state = tk.StringVar(value="Return")  # 初期値はReturnに設定
            button = tk.Button(self.master, textvariable=button_state, width=10, command=lambda i=i: self.toggle_button_state(i))
            self.button_states.append(button_state)  # ボタンの状態を管理するために、リストに追加する
            button.pack()

            spinbox = tk.Spinbox(self.master, from_=0, to=item.quantity)
            self.spin_box_list.append(spinbox)
            spinbox.pack()

        self.ok_button = tk.Button(self.master, text="OK", command=self.create_final_check_widget)
        self.ok_button.pack()

    def toggle_button_state(self, index):
        current_state = self.button_states[index].get()
        if current_state == "Return":
            self.button_states[index].set("Take")
        else:
            self.button_states[index].set("Return")

    def get_button_states(self):
        button_states = [button.get() for button in self.button_states]
        self.button_states = button_states

    def get_spinbox_state(self):
        spinbox_list = [spinbox.get() for spinbox in self.spin_box_list]
        self.spin_box_list = spinbox_list

    def create_final_check_widget(self):  # next : show_thank_you
        self.get_button_states()
        self.get_spinbox_state()
        self.destroy_current_widgets()
        self.final_check_label = tk.Label(self.master, text="Please check your order")
        self.final_check_label.pack()

        self.order_label = tk.Label(self.master, text=f"{self.user_name} wants to ...")
        self.order_label.pack()
        for item, state, chosen_num in zip(self.inv_list, self.button_states, self.spin_box_list):
            self.order_label = tk.Label(self.master, text=f"\"{item.name}\" * {chosen_num}  {state} for {self.project_name}") #3 return item_name for project_name
            self.order_label.pack()

        self.confirm_button = tk.Button(self.master, text="Confirm", command=self.show_thank_you)
        self.confirm_button.pack()
    
    def show_thank_you(self):  # next : create_widgets
        self.manager.update_db(self.inv_list, self.button_states, self.spin_box_list)
        rem_cnt_list = self.manager.return_rem_cnt_list()
        self.logger = Logger(self.user_name, self.project_name, self.inv_list,  self.spin_box_list, self.button_states, rem_cnt_list)
        self.logger.log()
        self.destroy_current_widgets()
        thank_you_label = tk.Label(self.master, font=("Helvetica", 24))
        thank_you_label.pack()
        thank_you_label.config(text="Thank You !")
        self.after(2000, self.create_widgets)
    
    def create_error_widget(self):
        self.destroy_current_widgets()
        sorry_label = tk.Label(self.master, font=("Helvetica", 24))
        sorry_label.pack()
        sorry_label.config(text="Sorry we don't know such item. please ask ews superviser.")
        self.after(2000, self.create_list_widgets)

    def destroy_current_widgets(self):
        for widget in self.master.winfo_children():
            widget.destroy()


def main(args=None):
    try:
        root = tk.Tk()
        app = MainApplication(root)
        root.protocol("WM_DELETE_WINDOW", lambda: messagebox.showerror("Error", "Cannot close the window"))
        root.mainloop()

    except KeyboardInterrupt:
        print("ctl-C")


if __name__ == "__main__":
    main()