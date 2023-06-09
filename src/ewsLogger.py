import csv
import os
import datetime
from ewsDBManager import Inventory


class Logger():
    def __init__(self, user_name, project_name, inventory_list, req_num_list, rt_list, remaind_list):
        self.user_name = user_name
        self.project_name = project_name
        self.inventory_list = inventory_list
        self.req_num_list = req_num_list
        self.remaind_list = remaind_list
        self.rt_list = rt_list
        self.header = ['time', 'user name', 'project name', 'id', 'name', 'Return/Take','required quantity', 'remained quantity']
        self.today = str(datetime.date.today())
        self.file_name = "../log/" + self.today + "-ews_ims_log.csv"


    def log(self):
        with open(self.file_name, "a") as f:
            writer = csv.writer(f)
            if not os.path.getsize(self.file_name): # if first time user today -> write header
                writer.writerow(self.header)

            writer.writerows(self._make_body())
            
    def _make_body(self):
        now = datetime.datetime.now()
        body = []
        for inv, req_qtty, rt, rem_qtty in zip(self.inventory_list, self.req_num_list, self.rt_list, self.remaind_list):
            body.append([now.time(), self.user_name, self.project_name, inv.id, inv.name, rt, req_qtty, rem_qtty])
        
        return body


if __name__ == "__main__":
    inventory = Inventory()
    logger = Logger("admin","test_user",[inventory], [1], [1], [1])
    logger.log()