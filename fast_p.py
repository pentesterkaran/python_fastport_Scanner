import socket
import threading
import sys
import os
import ipaddress
import queue
from colorama import Fore,Back,Style
import os
import time
import argparse

owner = '''

@Creator

 【ｐｅｎｔｅｓｔｅｒｋａｒａｎ】

    '''

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--target',help='give target ip or domain',dest='target',required=True)
    parser.add_argument('-s','--start',help='Give start port',dest='start_port',required=True,type=int)
    parser.add_argument('-e','--end',help='Give end port',dest='end_port',required=True,type=int)
    parser.add_argument('-t','--threads',help='Specify threads(default=10)',dest='threads',type=int)
    return parser.parse_args()

class rang:
    red = Fore.RED
    blue = Fore.BLUE
    cyan = Fore.CYAN
    yellow = Fore.YELLOW
    green = Fore.GREEN
    bright = Style.BRIGHT
    reset = Style.RESET_ALL



def make_file():
    if not os.path.exists('open_ports.txt'):
        with open('open_ports.txt','w') as file:
            file.write('\t\tOPEN PORTS\n\n')
    else:
        os.remove('open_ports.txt')
        with open('open_ports.txt','w') as file:
            file.write('\t\tOPEN PORTS\n\n')



def get_ip(target):
    try:
        ip = ipaddress.ip_address(target)
        return str(ip)
    except:
        try:
            ip = socket.gethostbyname(target)
            return str(ip)
        except socket.gaierror:
            print("Host Resolution Failed")


def scan(ip):
    with open("open_ports.txt",'a') as f:
        while not q.empty():
            port = q.get()
            try:
                sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip,port))
                if result == 0:
                    print(f"{port}\t\t {rang.yellow}OPEN {rang.reset}")
                    f.write(f"{port} \t OPEN\n")
                else:
                    print(f"{port}\t\t {rang.cyan}CLOSE{rang.reset}")
            except socket.error as e:
                print(f"{rang.red}SomeThing Bad Happen with socket{rang.reset}")
                sys.exit(-1)
            except OverflowError:
                print(f"{rang.red}I think By Mistake you provide port number more than 65535{rang.reset}")
                sys.exit(-1)
            # except TypeError:
            #     print("String Datatype is Expected")
            except KeyboardInterrupt:
                pass
            finally :
                sock.close()
            q.task_done()
        f.close()

def clear_term():
    os.system('cls' if os.system=='nt' else 'clear')

def thread_n(no_threads):
    for i in range(no_threads):
        thread = threading.Thread(target=scan, args=(ip_addr,))
        thread.start()

def q_port(start,end):
    for port in range(start,end+1):
        q.put(port)

if __name__ == "__main__":

    args = get_arguments()
    ip_addr = args.target
    start= args.start_port
    end = args.end_port
    
    
    if args.threads:
        threads = args.threads
    else:
        threads = 10
    
    
    clear_term()
    print(f'{rang.bright}{rang.yellow}\t\t\t\t\t {owner}')
    make_file()
    q = queue.Queue()
    q_port(start,end)
    print(f"{rang.green}{rang.bright}\t\t\tStarted Scanning Ports at {ip_addr}{rang.reset}")
    start_time = time.time()
    try:
        print(f"{rang.bright}{rang.blue}\nPORT\t\t STATE{rang.reset}")
        thread_n(threads)
        q.join()
    except KeyboardInterrupt:
        print(f"{rang.red}\n\tKeyboard Interrupt Successfully Received{rang.reset}")
    
    print(f"{rang.bright}{rang.yellow}Time-Taken:{time.time()-start_time}")

