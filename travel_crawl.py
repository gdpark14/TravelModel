
from bs4 import BeautifulSoup
import openpyxl
from selenium import webdriver
import time

excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
excel_sheet.column_dimensions['D'].width = 100


excel_sheet.append(['장소','시군구','전화번호','키워드'])
driver=webdriver.Chrome('C:/Users/USER/Downloads/chromedriver_win32 (1)/chromedriver.exe')
driver.get('https://korean.visitkorea.or.kr/list/ms_list.do?areacode=4')
time.sleep(1)

html=driver.page_source
soup = BeautifulSoup(html, "html.parser")

location=soup.find_all('li','bdr_nor')
for i in location:
    var=i.find('div','area_txt')
    location_name=var.find('a').get_text()
    sigungu=var.find_all('p')[0].get_text()
    telephone=var.find_all('p')[1].get_text()
    hashtag_place=i.find_all('span')
    hashtag=""
    for x in range(0,len(hashtag_place)):
        hashtag=hashtag+hashtag_place[x].get_text()
    excel_sheet.append([location_name,sigungu,telephone,hashtag])


cell_A1 = excel_sheet['A1']
cell_A1.alignment = openpyxl.styles.Alignment(horizontal="center")

cell_B1 = excel_sheet['B1']
cell_B1.alignment = openpyxl.styles.Alignment(horizontal="center")

cell_C1 = excel_sheet['C1']
cell_C1.alignment = openpyxl.styles.Alignment(horizontal="center")

cell_D1 = excel_sheet['D1']
cell_D1.alignment = openpyxl.styles.Alignment(horizontal="center")

excel_file.save('travel_location2.xlsx')
excel_file.close()