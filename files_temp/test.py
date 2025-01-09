import pycurl

def download_lista(url_lista, save_list):
    with open(save_list, 'wb') as file:
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url_lista)
        curl.setopt(curl.WRITEDATA, file)
        curl.perform()
        curl.close()


url_lista ='https://debianraspberry.ikeasi.com/vendors/ubicacionrp/172-19-23-201_lista.txt' 
save_list = './lista.txt' 
download_lista(url_lista, save_list)