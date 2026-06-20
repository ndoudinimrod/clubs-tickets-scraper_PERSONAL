import datetime
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

myDatetime = datetime.datetime.now()
today = datetime.date.today()
today_format = today.strftime('%Y%m%d')
# print(today_format)

un_vendredi = datetime.datetime(2022, 6, 24)
un_vendredi_format = un_vendredi.strftime('%A')
# print(un_vendredi_format)


un_samedi = datetime.datetime(2022, 6, 25)
un_samedi_format = un_samedi.strftime('%A')
# print(un_samedi_format)

if "Friday" != un_vendredi_format:
    fin = "It's not friday !!! STOP ALL"
    print(fin)
    sys.exit()

if "Saturday" != un_samedi_format:
    fin = "It's not saturday !!! STOP ALL"
    print(fin)
    sys.exit()

td = myDatetime - un_samedi
sortie = td.days % 7
# print(sortie)

"""
Séparation en 2 partie : vendredi ou samedi 
"""

# Vendredi
date_party = myDatetime
compteur_days = 0
while sortie != 0:
    compteur_days = compteur_days + 1
    one_day = datetime.timedelta(days=1)
    date_party = date_party + one_day
    td = date_party - un_vendredi
    sortie = td.days % 7

# print(str(compteur_days) + ' days')

day = datetime.timedelta(days=compteur_days, weeks=0)
date_party = myDatetime + day

print(date_party.strftime('DATE SEARCHED = %Y%m%d : %A'))
date = date_party.strftime('%Y%m%d')
# print(date)

# create variable  for lunch driver

options = webdriver.ChromeOptions()

prefs = {"download.default_directory": "bizouk"}

options.add_experimental_option("prefs", prefs)
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),chrome_options=options)

# CACHER CREDENTIALS

driver.get("https://www.bizouk.com/login/log-in")

email = driver.find_element(By.ID, "email")
email.send_keys("nimrodndoudi@gmail.com")
email.submit()

email = driver.find_element(By.ID, "password")
email.send_keys("Nimrodsteve7")
email.submit()

#  CHOIX DE SOIREE

# L'EMPIRE CLUB
# 911 PARIS
# THE MOMENT
#

#

driver.get('https://www.bizouk.com/soirees/agenda/region/paris/' + date)
lieu_choisi = "911 PARIS"
"""
if lieu_choisi == "THE MOMENT":  # lieu de la soiree
Celse:
    lieu_soiree = driver.find_elements(By.CSS_SELECTOR, "p.soiree_lieu")  # POUR THE MOMENT

for element in lieu_soiree:

    if lieu_choisi not in element.text:
        # print('Sous-chaîne non trouvée')
        print("Pas de soirée " + lieu_choisi + "\n")
        # sys.exit()
    else:
        place_party = element.text

        print(element.text)
        element.click()

        # Quantite de tickets
        quantity_tikets = 4
        theme_party = driver.find_element(By.CLASS_NAME, 'party_entete')
        select = driver.find_elements(By.CLASS_NAME, )
        print('Vous souhaitez prendre combient de ticket pour  ' + theme_party.text + ' au ' + place_party + ' ?')

        gratuite = driver.find_element(By.XPATH,
                                       "/html/body/main/div[1]/div[2]/div[1]/div/div[3]/div/form/div/table[1]/tbody/tr[1]")
        price = gratuite.text
        # Vérifier si la sous-chaine se trouve dans la chaine principale
        if "\n0.00€" not in price:
            # print('Sous-chaîne non trouvée')
            print("\n Il n'y a plus de places gratuites!\n")
            sys.exit()
        else:
            # print('Sous-chaîne trouvée')
            nbr_place = Select(driver.find_element(By.XPATH,
                                                   "/html/body/main/div[1]/div[2]/div[1]/div/div[3]/div/form/div/table[1]/tbody/tr[1]/td[1]/select"))
            nbr_place.select_by_value(str(quantity_tikets))
            confirm = driver.find_element(By.ID, "btn-resa-etape-contenu")
            confirm.submit()

            # Remplir informations de ticket
            "GESTION POUR PLUSIEURS TICKETS A REMPLIR POUR PLUSIEURS PERSONNES"
            # nbr_person = driver.find_elements(By.CLASS_NAME, 'panel.panel-primary.bzk-panel-primary')
            num_person = 1
            while num_person != (quantity_tikets + 1):
                # 2eme personne                                "/html/body/main/div/form/div/div[2]/div[2]/dd[1]/input"
                # 3eme personne                                "/html/body/main/div/form/div/div[3]/div[2]/dd[1]/input"
                # 4eme personne                                "/html/body/main/div/form/div/div[4]/div[2]/dd[1]/input"
                nom_du_porteur = driver.find_element(By.XPATH, "/html/body/main/div/form/div/div[" + str(
                    num_person) + "]/div[2]/dd[1]/input")
                nom_du_porteur.send_keys("NDOUDI")

                prenom_du_porteur = driver.find_element(By.XPATH, "/html/body/main/div/form/div/div[" + str(
                    num_person) + "]/div[2]/dd[2]/input")
                prenom_du_porteur.send_keys("Nimrod")

                if lieu_choisi == "911 PARIS":
                    nom_prenom = driver.find_element(By.XPATH, "/html/body/main/div/form/div/div[" + str(
                        num_person) + "]/table/tbody/tr[2]/td/dd[1]/input")
                    nom_prenom.send_keys("NDOUDI Nimrod")

                    email_ticket = driver.find_element(By.XPATH, "/html/body/main/div/form/div/div[" + str(
                        num_person) + "]/table/tbody/tr[2]/td/dd[2]/input")
                    email_ticket.send_keys("nimrodndoudi@gmail.com")

                    telephone = driver.find_element(By.XPATH, "/html/body/main/div/form/div/div[" + str(
                        num_person) + "]/table/tbody/tr[2]/td/dd[3]/input")
                    telephone.send_keys("0782576397")

                if lieu_choisi == "L'EMPIRE CLUB":
                    nom_prenom = driver.find_element(By.XPATH,
                                                     "/html/body/main/div/div[3]/form/div[1]/div[2]/dd[1]/input")
                    nom_prenom.send_keys("NDOUDI Nimrod")

                    email_ticket = driver.find_element(By.XPATH,
                                                       "/html/body/main/div/div[3]/form/div[1]/div[2]/dd[2]/input")
                    email_ticket.send_keys("nimrodndoudi@gmail.com")

                    telephone = driver.find_element(By.XPATH,
                                                    "/html/body/main/div/div[3]/form/div[1]/div[2]/dd[3]/input")
                    telephone.send_keys("0782576397")

                num_person = num_person + 1

            confirm = driver.find_element(By.ID, "btn-resa-etape-contenu")
            confirm.submit()

            confirm = driver.find_element(By.ID, "btn-resa-etape-contenu")
            confirm.submit()

            confirm = driver.find_element(By.XPATH, "/html/body/main/div/a")
            confirm.submit()

            confirm = driverl.find_element(By.XPATH, "/html/body/main/div/a")
            confirm.submit()"""

driver.get('https://www.bizouk.com/account/store-orders/attendees-list?order=20221059730720')

# billets = driver.find_elements(By.CLASS_NAME, "item-line")
billets = driver.find_elements(By.CSS_SELECTOR, "div.panel-heading")
nbr_billets = len(billets)
compteur = 0
while compteur < nbr_billets:
    pdf = driver.find_element(By.XPATH,
                              f"/html/body/main/div/div/div/div/div[{compteur + 2}]/div[2]/div/div[3]/div/div/a")
    num = driver.find_element(By.XPATH,
                                    f"/html/body/main/div/div/div/div/div[{compteur + 2}]/div[2]/div/div[2]/div")
    numero_id = num.text
    print(f"{numero_id} a été téléchargé")
    #pdf.sendKeys("bizouk/");
    pdf.click()
    compteur = compteur + 1

# AJOUTER ET VERIFIER UN MESSAGE DE FIN !!!!
