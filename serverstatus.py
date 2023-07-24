import requests
import urllib3
import pyfiglet
import simple_colors

# Başlık ve header
ascii_banner = pyfiglet.figlet_format("SERVER STATUS")
print(simple_colors.blue(ascii_banner))
print(simple_colors.blue("https://github.com/enescalban"))
print("_" * 50)

# 'urllib3' kütüphanesindeki uyarıları devre dışı bırak
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Kullanıcıdan txt dosyası adını al
txt_file = input(simple_colors.green("Lütfen txt dosyasının adını (örn. domains.txt) girin: "))

# Tüm domainleri okuyup kontrol etmek için bir fonksiyon tanımlayalım
def check_domains(url_list):
    status_code_files = {}
    for url in url_list:
        url = url.strip()  # Boşlukları kaldırma
        try:
            res = requests.get(url, verify=False)
            status_code = res.status_code
            if status_code == 200:
                status_color = simple_colors.green
                status_file = '200.txt'
            elif status_code == 403:
                status_color = simple_colors.red
                status_file = '403.txt'
            elif status_code == 401:
                status_color = simple_colors.red
                status_file = '401.txt'
            else:
                status_color = simple_colors.yellow
                status_file = 'other_status.txt'
            
            status_code_files.setdefault(status_code, []).append(url)
            print(f"{url} = {status_color(status_code)}")
        except Exception as e:
            print(f"{url} = {simple_colors.red('Hata:')} {e}")
    
    # Belirli HTTP durum kodlarına sahip domainleri ilgili dosyalara kaydet
    for status_code, domains in status_code_files.items():
        with open(f'{status_code}.txt', 'w') as status_file:
            for domain in domains:
                status_file.write(domain + '\n')

# Txt dosyasındaki domainleri okuyalım
try:
    with open(txt_file, 'r') as file:
        urls = file.readlines()
        check_domains(urls)
except FileNotFoundError:
    print("Belirtilen txt dosyası bulunamadı.")
except Exception as e:
    print(f"Hata oluştu: {e}")
