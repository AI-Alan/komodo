import os 
import sys
import subprocess

path = "/Users/amankumaryadav/Desktop/"   #platform and user sprcific installation loacatin
pr_name = os.path.join(path,'komodo/bin/komo')  #path of program name
envs_path = os.path.join(path,"komodo/envs")   #path of virtual environments present
doc_path = os.path.join(path,"komodo/doc.txt")
run = os.path.join(path,'komodo/bin/run.zsh')
#path of documentation file
python_loc = "python3"
#run_file = os.path.join(path,"komodo/bin/run.zsh")

def create():
    try :
            env = os.path.join(envs_path,sys.argv[2])
            flag = subprocess.call([python_loc,'-m','venv',env]) #add version
            print(sys.argv[2]," : python virtual environment creaed successfully")
    except FileExistsError:
            print("Virtual with this name already present : " ,sys.argv[2]) 
            print("Please change name") 

def delete(env_name):
    v_env = os.path.join(envs_path,env_name)
    subprocess.call(['rm','-r',v_env])
      
def change_venv(env_name):
    v_env = os.path.join(envs_path,env_name,"bin","activate")
    # try :
    #     subprocess.call(['deactivate'])
    #     subprocess.call(['/bin/bash','--rcfile',v_env])
    # except  FileNotFoundError:
    subprocess.call(['/bin/bash','--rcfile',v_env])

if __name__ == "main" :
    pass
    
