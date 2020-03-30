'''
owner : Abhishek Panakkaran
Purpose : Reading and plotting windows physical servers from soa

'''

import pandas as pd

def read_csv_data_week(servername,cred,account,soa_url):
    #vm_processor_ready_percent
        try:
                sn = "&server=" + servername
		
                q = soa_url + account + "&metric=[date,time,display_name,vm_host_name,processor_busy,vm_processor_busy,vm_processor_virtual_count,vm_processor_ready_percent,memory_used_percent,memory_act_percent]&frequency=15&os=allWindows&format=csv&date=[-16,-1]&sortby=[date,time,sub_client_id_1,sub_client_id_2,display_name]" + sn + cred
                print(q)
                df = pd.read_csv(q)
                df['datetime'] = df['date'] + " " + df['time']
                df.index = df['datetime']
                df = df[df['vm_host_name'] != '_Total']
                print(df.info())
           
                print("Getting weekly data for {}".format(servername))
                return df
        except:
                pass
        

def add2(num1 , num2):
    return num1 + num2

name="abhi"
