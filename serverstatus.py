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
    for url in url_list:
        url = url.strip()  # Boşlukları kaldırma
        try:
            res = requests.get(url, verify=False)
            status_code = res.status_code
            if status_code == 403 or status_code == 401:
                status_color = simple_colors.red
                status = "Kapalı"
            else:
                status_color = simple_colors.green
                status = "Açık"
            
            print(f"{url} = {status_color(status)}")
        except requests.exceptions.RequestException:
            print(f"{url} = {simple_colors.red('Kapalı')}")

# Txt dosyasındaki domainleri okuyalım
try:
    with open(txt_file, 'r') as file:
        urls = file.readlines()
        check_domains(urls)
except FileNotFoundError:
    print("Belirtilen txt dosyası bulunamadı.")
except Exception as e:
    print(f"Hata oluştu: {e}")
