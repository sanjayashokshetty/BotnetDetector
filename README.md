# BotnetDetector
## Execution
1. Download the dataset `ISOT_Botnet_DataSet_2010.pcap` and it's datasheet to the project's root folder. [Here](https://www.uvic.ca/engineering/ece/isot/datasets/) is a source.
1. Generate `ISOT-172-16.csv` from `ISOT_Botnet_DataSet_2010.pcap` by executing
    ```bash
    python3 PcapToCSV.py
    ```
1. Generate `172.16.*.*.pcap` files from `ISOT-172-16.csv` by running the `setup.ipynb` notebook or
   ```bash
   python3 pcapIPfilter.py
   ```
1. Generate `flow.pickle` using the `make dictionary 1.ipynb` notebook.
1. Run the `processing.ipynb` notebook to view various visualization of the data
1. Run the analysis notebooks with different feature configurations to tune the model.
## File structure
* PcapToCSV.py:
Parse the PCAP dump from ISOT and generate CSV formatted file where each row is a packet in the 172.16.0.0/16 subnet. A packet is represented as source IP, destination IP, source port, destination port, protocol, time, packet size, source MAC address, destination MAC address.

* setup.ipynb, pcapIPfilter.py: 
Segregate traffic of each machine in the 172.16.0.0/16 subnet to different files. This makes analysing and visualizing some given flows faster.

* make dictioanary 1.ipynb:
Generate the core in-memory data-structure than represents traffic flow. It is a dictionary where key is (source ip, destination ip, source port, destination port, protocol) and value is a time series list representing that flow.
 
* processing.ipynb:
Use various visualization techniques to observe patterns and make inferences.

* analysis_new_features.ipynb, analysis_paper.ipynb:
Use feature engineering and feature selection, and improve performance and accuracy of the ML model.