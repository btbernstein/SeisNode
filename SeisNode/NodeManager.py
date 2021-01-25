import pickle
import subprocess
import time
from datetime import datetime as dt
import pandas as pd
import csv
import threading
from os import path
from SeisNode import SeisNode


class NodeManager:
    """
    [In progress]
    
    """
    def __init__(self):
        self.node_path = "/home/pi/SeisNode"
        self.save_path = "/home/pi/SeisNode/save/node.pickle"
        self.data_dir = "/home/pi/SeisNode/data"
        self.data_path = None
        # Check for existing node file
        if path.exists(self.save_path):
            # Load node
            self._load_from_file()
        else:
            # Create new node
            self.node = SeisNode()
            
        # Start and connect to the GPS     
        self._start_gps()
     
        
    def _load_from_file(self):
        """
        Loads an existing SeisNode class from a file.
        """
        
        self.node = pickle.load(open(self.save_path, "rb", -1)) 
    
    def _save_to_file(self):
        """
        Saves the current SeisNode class from a file.
        """
        
        with open(self.save_path, "wb") as f:
            pickle.dump(self.node, f, -1)

    
    def _start_gps(self):
        """
        Calls the bash script that connects to the GPS, and
        ensures the GPS is connected before continuing startup process.
        """
        
        sensor_script = "/home/pi/SeisNode/scripts/start_sensors.sh"
        subprocess.call(sensor_script)
        
        # GPS is connected when the sensor has a 3D lock (mode=3)
        gpsd.connect()
        packet = gpsd.get_current()
        while packet.mode != 3:
            continue
        return True   
    
    def _flush_node(self):
        """
        Periodically saves the node
        """
        init_time = time.time()
        while True:
            if time.time()-init_time % 120 == 0:
                self._save_to_file()
                self.write_data_csv()
        
    def collect_data(self,plot_data=False):
        """
        Tells the node to collect data
        """
        vz,vx,vy = self.node.collect_data()
        #threading.Thread(target=self._flush_node).start()
        if plot_data:
            plot_data(vz,vx,vy)
            
    def write_data_csv(self,filename=self.data_path):
        """
        Appends data to a csv file and clears data stored in the node
        """
        if filename == None:
            name = dt.strftime(dt.today(), "%d-%m-%Y_%H%M")
            self.data_path = f"{self.data_dir}/{name}.csv"
            filename = self.data_path
        
        arr = np.array([self.node.vz,self.node.vx,self.node.vy])
        self.node.vz.clear();self.node.vx.clear();self.node.vy.clear()
        with open(self.data_path, "a") as f:
            writer = csv.writer(f)
            writer.writerows(arr.T)
        
    def plot_data(self,vz,vx,vy):
        """
        Plots the 3 data components
        """
        plt.figure(figsize=(12,15))
        plt.subplot(311)
        plt.plot(vz)
        plt.xlabel("Samples")
        plt.ylabel("Amplitude")
        plt.title(f"Z Signal at {rate} SPS")
        plt.subplot(312)
        plt.plot(vx)
        plt.xlabel("Samples")
        plt.ylabel("Amplitude")
        plt.title(f"X Signal at {rate} SPS")
        plt.subplot(313)
        plt.plot(vy)
        plt.xlabel("Samples")
        plt.ylabel("Amplitude")
        plt.title(f"Y Signal at {rate} SPS")
        plt.tight_layout()
        plt.savefig(f"Figures/{rate}_full_signal_cont.jpg")
