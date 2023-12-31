import time

from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver

class SideBars(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    '''----------------------------------------MENU PENGGUNA/USER------------------------------------------------'''
    # LOCATORS
    MENU_PENGGUNA = '//li[@class="menu-item icon-user"]/div/i'
    SUBMENU_TAMBAH_PENGGUNA_BARU = '//div[@class="sidebarWidth4 float-left"]/div/ul/div[6]/div/button[1]'
    SUBMENU_LIST_PENGGUNA = '//div[@class="sidebarWidth4 float-left"]/div/ul/div[6]/div/button[2]'
    SUBMENU_ALOKASI_ELECTIVE_SUBJECT = '//div[@class="sidebarWidth4 float-left"]/div/ul/div[6]/div/button[3]'

    # TEST FUNCTION : OBJECT
    def getMenuPengguna(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.MENU_PENGGUNA)

    def getSubMenuTambahPengguna(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.SUBMENU_TAMBAH_PENGGUNA_BARU)

    def getSubMenuListPengguna(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.SUBMENU_LIST_PENGGUNA)

    def getSubMenuAlokasiPelajaranElective(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.SUBMENU_ALOKASI_ELECTIVE_SUBJECT)

    # TEST FUNCTION : ACTION/STEP
    def go_to_TambahPenggunaPage(self):
        self.getMenuPengguna().click()
        self.getSubMenuTambahPengguna().click()
        time.sleep(0.5)

    def go_to_ListPenggunaPage(self):
        self.getMenuPengguna().click()
        self.getSubMenuListPengguna().click()
        time.sleep(0.5)

    def go_to_AlokasiElectivePage(self):
        self.getMenuPengguna().click()
        self.getSubMenuAlokasiPelajaranElective().click()
        time.sleep(0.5)

    '''-----------------------------------------MENU PROFILE-----------------------------------------------------'''
    # LOCATORS
    MENU_PROFILE = '//*[@id="root"]/div[1]/div[2]/div[1]/div/ul/div[2]/li'



