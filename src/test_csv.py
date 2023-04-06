import csv
import os
import datetime
from ewsDBManager import Inventory

inventory = Inventory()
header = ['time', 'user name', 'project name', 'id', 'name', 'Return/Take','required quantity', 'remained quantity']


class Logger():
    def __init__(self, inventory_list, req_num_list, rt_list, remaind_list):
        self.user_name = ""
        self.project_name = ""
        self.inventory_list = inventory_list
        self.req_num_list = req_num_list
        self.remaind_list = remaind_list
        self.rt_list = rt_list
        self.header = ['date', 'user name', 'project name', 'id', 'name', 'required quantity', 'ewmained quantity']
        self.body = ""
        self.today = str(datetime.date.today())
        self.file_name = "../log/" + self.today + "-ews_ims_log.csv"


    def log(self):
        with open(self.file_name, "a") as f:
            writer = csv.writer(f)
            self.write_header()
            writer.writerows(self.make_body())
    
    def write_header(self):
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.header) # ヘッダーを書き込みます
        else:
            pass # if exist, do nothing
            
    def make_body(self):
        now = datetime.datetime.now()
        body = []
        for inv, req_qtty, rt, rem_qtty in zip(self.inventory_list, self.req_num_list, self.rt_list, self.remaind_list):
            body.append([now.time(), self.user_name, self.project_name, inv.id, inv.name, rt, req_qtty, rem_qtty])
        
        return body


if __name__ == "__main__":
    logger = Logger([inventory], [1], [1], [1])
    logger.log()