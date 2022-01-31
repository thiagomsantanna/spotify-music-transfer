from concurrent.futures import thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from jsonReader import readJson
import time
# import requests



# chrome_options = Options()
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument('--headless')

# chrome_options=chrome_options
playlists = readJson('Playlist1.json')
# print(playlists)
# print("##############################################################################################")
playlistTest = playlists['playlists'][0]
#print(playlistTest)

d = webdriver.Chrome()
d.get('https://open.spotify.com')
d.maximize_window();

d.implicitly_wait(5)

d.find_element(By.XPATH, "//button[@data-testid='login-button']").click()

d.implicitly_wait(8);
d.find_element(By.ID, "login-username").send_keys('thiagomundicisantanna@gmail.com')
d.find_element(By.ID, "login-password").send_keys('lolecoisadeviado123')

d.find_element(By.XPATH, "//p[text()='Entrar']").click()

d.implicitly_wait(10)

for playlist in playlists['playlists']:
    print('sexo')


d.find_element(By.XPATH, "//button[@data-testid='create-playlist-button']").click()
d.find_element(By.XPATH, "//button[@data-testid='more-button']").click()
d.find_element(By.XPATH, "//span[text()='Editar os detalhes']/..").click()

d.implicitly_wait(3)

playlistInputName = d.find_element(By.XPATH, "//input[@placeholder='Add a name']")
playlistInputName.clear()
playlistInputName.send_keys(playlistTest['name'])
d.find_element(By.XPATH, "//textarea[@data-testid='playlist-edit-details-description-input']").send_keys(playlistTest['description'])

d.find_element(By.XPATH, "//button[@data-testid='playlist-edit-details-save-button']").click()
# d.find_element(By.XPATh, "//span[text()='Apagar']/..").click()

d.implicitly_wait(8)

musicSearchBox = d.find_element(By.XPATH, "//input[@role='searchbox']")
crrtTrack = None
playlistMusics = playlistTest['items']

for music in playlistMusics:
    crrtTrack = music['track']
    print(crrtTrack['trackName'])
    
    musicSearchBox.send_keys(crrtTrack['trackName'])#.track.name
    time.sleep(3)
    d.find_element(By.XPATH, f"//a[text()='{crrtTrack['artistName']}']/../../../following-sibling::div/button[@data-testid='add-to-playlist-button']").click()#.track.artistName

    d.find_element(By.XPATH, "//button[@aria-label='Limpar o campo de busca']").click()#.track.name

    d.implicitly_wait(10)

