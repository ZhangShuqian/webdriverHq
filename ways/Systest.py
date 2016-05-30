#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from ways.BasePage import Page
from selenium.webdriver.support.select import Select

class SysPage(Page):
    '''基础信息管理'''
    BaseMenue_loc = (By.LINK_TEXT, u'基础信息管理')
    def clickBaseMenue(self):
        '''点击基础信息管理菜单'''
        self.wait
        self.find_element(*self.BaseMenue_loc).click()

    '''品牌配置'''
    BaseBrand_loc = (By.LINK_TEXT, u'品牌配置')
    BatchBrand_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/button")
    StartBrand_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/ul/li[4]/a")
    EndBrand_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/ul/li[5]/a")
    DeleteBrand_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/ul/li[6]/a")
    prompt_loc = (By.CSS_SELECTOR, '.text')
    AllSelectBrand_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/ul/li[1]/a")
    StateBrand_loc = (By.XPATH, ".//*[@id='brand1']/span")
    CreateBrandButton_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[1]/div[2]/div/a")
    BrandReturnButton_loc = (By.XPATH, ".//*[@id='wrapper']/div[3]/div/div[2]/div/div/a")
    InfoBrand_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[1]/div[1]/h3")
    TitleBrand_loc = (By.XPATH, ".//*[@id='wrapper']/div[3]/div/h3")
    BrandCode_loc = (By.XPATH, ".//*[@id='brandform']/div[1]/div/input[1]")
    BrandName_loc = (By.XPATH, ".//*[@id='brandform']/div[2]/div/input")
    BrandEnname_loc = (By.XPATH, ".//*[@id='brandform']/div[3]/div/input")
    SaveBrand_loc = (By.XPATH, ".//*[@id='saveButton01']")
    singleEditButton_loc = (By.XPATH, '//*[@id="1"]/td[6]/div/button')
    singleEndBrand_loc = (By.XPATH, '//*[@id="1"]/td[6]/div/ul/li[2]/a')
    singleStartBrand_loc = (By.XPATH, '//*[@id="1"]/td[6]/div/ul/li[1]/a')
    def clickBaseBrand(self):
        '''点击品牌配置'''
        self.wait
        self.find_element(*self.BaseBrand_loc).click()

    def clickBatchBrand(self):
        '''点击品牌批量操作'''
        self.wait
        self.find_element(*self.BatchBrand_loc).click()

    def clickStartBrand(self):
        '''品牌批量启用'''
        self.wait
        self.find_element(*self.StartBrand_loc).click()

    def clickEndBrand(self):
        '''品牌批量停用'''
        self.wait
        self.find_element(*self.EndBrand_loc).click()

    def clickDeleteBrand(self):
        '''品牌批量删除'''
        self.wait
        self.find_element(*self.DeleteBrand_loc).click()

    def clickAllSelectBrand(self):
        '''点击全选（品牌管理）'''
        self.wait
        self.find_element(*self.AllSelectBrand_loc).click()

    def clickCreateBrandButton(self):
        '''点击创建品牌按钮'''
        self.wait
        self.find_element(*self.CreateBrandButton_loc).click()

    def clickReturnButtonBrand(self):
        '''点击返回按钮（品牌管理）'''
        self.wait
        self.find_element(*self.BrandReturnButton_loc).click()

    def getPrompt(self):
        '''获取提示信息'''
        self.wait
        return self.find_element(*self.prompt_loc).text

    def getInfoBrand(self):
        '''获取品牌列表主页标题'''
        self.wait
        return self.find_element(*self.InfoBrand_loc).text

    def checkStateBrand(self):
        '''验证品牌当前状态'''
        self.wait
        return self.find_element(*self.StateBrand_loc).text

    def getTitleBrand(self):
        '''获取创建品牌页面的title'''
        self.wait
        return self.find_element(*self.TitleBrand_loc).text

    def createBrand(self, code, name, engname):
        '''创建品牌'''
        self.wait
        self.find_element(*self.BrandCode_loc).send_keys(code)
        self.wait
        self.find_element(*self.BrandName_loc).send_keys(name)
        self.wait
        self.find_element(*self.BrandEnname_loc).send_keys(engname)
        self.wait
        self.find_element(*self.SaveBrand_loc).click()

    def clickSingleEditBrandButton(self):
        '''点击单个编辑按钮'''
        self.wait
        self.find_element(*self.singleEditButton_loc).click()

    def clickSingleStartBrand(self):
        '''点击单个启用'''
        self.wait
        self.find_element(*self.singleStartBrand_loc).click()

    def clickSingleEndBrand(self):
        '''点击单个停用'''
        self.wait
        self.find_element(*self.singleEndBrand_loc).click()

    '''客户管理'''
    BaseCustomer_loc = (By.LINK_TEXT, u'客户管理')
    BatchCustomer_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/button")
    EndCustomer_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[5]/a")
    StartCustomer_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[4]/a")
    CreateCustomerButton_loc = (By.XPATH, ".//*[@id='wrapper']/div[3]/div/div/div[2]/div/a")
    CustomerCode_loc = (By.XPATH, ".//*[@id='customerCode']")
    CustomerName_loc = (By.XPATH, ".//*[@id='customerName']")
    CustomerContacts_loc = (By.XPATH, ".//*[@id='pic']")
    CustomerIphone_loc = (By.XPATH, ".//*[@id='picContact']")
    Sign_loc = (By.TAG_NAME, 'li')
    Ways_loc = (By.ID, "select2-paymentTerm-container")
    WaysSelect_loc = (By.ID, 'select2-paymentTerm-results')
    invocetype_loc = (By.ID, 'select2-invoiceType-container')
    invocetypeSelect_loc = (By.ID, 'select2-invoiceType-results')
    customertype_loc = (By.ID, 'select2-customerType-container')
    customertypeSelect_loc = (By.ID, 'select2-customerType-results')
    saveCustomer_loc = (By.XPATH, ".//*[@id='saveOrUpdate']")
    titleCustomer_loc = (By.XPATH, ".//*[@id='wrapper']/div[3]/div/h3")
    allSelectCustomer_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[1]/a')
    stateCustomer_loc = (By.XPATH, '//*[@id="customer1"]/span')
    singleEditCustomer_loc = (By.XPATH, '//*[@id="1"]/td[10]/div/button')
    singleEndCustomer_loc = (By.XPATH, '//*[@id="1"]/td[10]/div/ul/li[2]/a')
    singleStartCustomer_loc = (By.XPATH, '//*[@id="1"]/td[10]/div/ul/li[1]/a')
    def clickBaseCustomer(self):
        '''点击客户管理'''
        self.wait
        self.find_element(*self.BaseCustomer_loc).click()

    def clickBatchCustomer(self):
        '''客户批量操作'''
        self.wait
        self.find_element(*self.BatchCustomer_loc).click()

    def clickEndCustomer(self):
        '''客户批量停用'''
        self.wait
        self.find_element(*self.EndCustomer_loc).click()

    def clickStartCustomer(self):
        '''客户批量启用'''
        self.wait
        self.find_element(*self.StartCustomer_loc).click()

    def createCustomerButton(self):
        '''点击创建客户按钮'''
        self.wait
        self.find_element(*self.CreateCustomerButton_loc).click()

    def createCustomer(self, code, name, contacts, iphone, ways, invocetype, customertype):
        '''创建客户'''
        self.wait
        self.find_element(*self.CustomerCode_loc).send_keys(code)  # 输入客户编码
        self.wait
        self.find_element(*self.CustomerName_loc).send_keys(name)  # 输入客户名称
        self.wait
        self.find_element(*self.CustomerContacts_loc).send_keys(contacts)  # 输入联系人
        self.wait
        self.find_element(*self.CustomerIphone_loc).send_keys(iphone)  # 输入联系电话
        self.wait
        self.find_element(*self.Ways_loc).click()  # 点击结算方式选项框
        list = self.find_element(*self.WaysSelect_loc).find_elements(*self.Sign_loc)
        list[ways].click() # 选择结算方式
        self.wait
        self.find_element(*self.invocetype_loc).click()  # 点击发票类型选项框
        list1 = self.find_element(*self.invocetypeSelect_loc).find_elements(*self.Sign_loc)
        list1[invocetype].click()  # 选择发票类型
        self.wait
        self.find_element(*self.customertype_loc).click()  # 点击客户类型选项框
        list2 = self.find_element(*self.customertypeSelect_loc).find_elements(*self.Sign_loc)
        list2[customertype].click()  # 选择客户类型
        self.wait
        self.find_element(*self.saveCustomer_loc).click()  # 点击保存按钮

    def getTitleCustomer(self):
        '''获取创建客户页面的title'''
        self.wait
        return self.find_element(*self.titleCustomer_loc).text

    def clickAllSelectCustomer(self):
        '''点击全选'''
        self.wait
        self.find_element(*self.allSelectCustomer_loc).click()

    def getStateCustomer(self):
        '''获取客户状态'''
        self.wait
        return self.find_element(*self.stateCustomer_loc).text

    def clickSingleEditCustomerButton(self):
        '''点击单个编辑按钮'''
        self.wait
        self.find_element(*self.singleEditCustomer_loc).click()

    def clickSingleEndCustomer(self):
        '''点击单个停用'''
        self.wait
        self.find_element(*self.singleEndCustomer_loc).click()

    def clickSingleStartCustomer(self):
        '''点击单个启用'''
        self.wait
        self.find_element(*self.singleStartCustomer_loc).click()

    '''物流商'''
    BaseLogistics_loc = (By.LINK_TEXT, u'物流商')
    BatchLogistics_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div/button")
    EndLogistics_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div/ul/li[5]/a")
    StartLogistics_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div/ul/li[4]/a")
    createLogisticsButton_loc = (By.XPATH, ".//*[@id='wrapper']/div[3]/div/div/div[2]/div/a")
    titleLogistic_loc = (By.XPATH, ".//*[@id='wrapper']/div[3]/div/div/div[1]/div/div[1]/div/h3")
    LogisticsCode_loc = (By.XPATH, ".//*[@id='id']")
    LogisticsName_loc = (By.XPATH, ".//*[@id='name']")
    saveLogistic_loc = (By.XPATH, ".//*[@id='saveButton']")
    InfoLogistics_loc = (By.XPATH, ".//*[@id='wrapper']/div[3]/div/div/div[1]/h3")
    allSelectLogistics_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div/ul/li[1]/a")
    stateInfoLogistics_loc = (By.XPATH, ".//*[@id='logistics2']/span")
    EditButton_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[9]/div/a")
    EditTitle_loc = (By.XPATH, ".//*[@id='wrapper']/div[3]/div/div/div[1]/div/div[1]/div/h3")
    singleEditLogistics_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[9]/div/button')
    singleEndLogistics_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[9]/div/ul/li[2]/a')
    singleStartLogistics_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[9]/div/ul/li[1]/a')
    def clickBaseLogistic(self):
        '''点击物流商'''
        self.wait
        self.find_element(*self.BaseLogistics_loc).click()

    def clickBatchLogistic(self):
        '''物流商批量操作'''
        self.wait
        self.find_element(*self.BatchLogistics_loc).click()

    def clickEndLogistic(self):
        '''物流商批量停用'''
        self.wait
        self.find_element(*self.EndLogistics_loc).click()

    def clickStartLogistic(self):
        '''物流商批量启用'''
        self.wait
        self.find_element(*self.StartLogistics_loc).click()

    def createLogisticButton(self):
        '''点击创建物流商按钮'''
        self.wait
        self.find_element(*self.createLogisticsButton_loc).click()

    def createLogistic(self, code, name):
        '''创建物流商'''
        self.wait
        self.find_element(*self.LogisticsCode_loc).send_keys(code)
        self.wait
        self.find_element(*self.LogisticsName_loc).send_keys(name)
        self.wait
        self.find_element(*self.saveLogistic_loc).click()

    def getTitleLogistic(self):
        '''获取创建物流商页面的title'''
        self.wait
        return self.find_element(*self.titleLogistic_loc).text

    def getInfoLogistic(self):
        '''获取物流商主页面信息'''
        self.wait
        return self.find_element(*self.InfoLogistics_loc).text

    def clickAllSelectLogistic(self):
        '''点击全选按钮'''
        self.wait
        self.find_element(*self.allSelectLogistics_loc).click()

    def StateInfoLogistic(self):
        '''获取物流商状态信息'''
        self.wait
        return self.find_element(*self.stateInfoLogistics_loc).text

    def clickEditButtonLogistics(self):
        '''点击编辑按钮'''
        self.wait
        self.find_element(*self.EditButton_loc).click()

    def getEditTitleLogistics(self):
        '''获取编辑页面标题'''
        self.wait
        return self.find_element(*self.EditTitle_loc).text

    def clickSingleEditLogisticsButton(self):
        '''点击单个编辑按钮'''
        self.wait
        self.find_element(*self.singleEditLogistics_loc).click()

    def clickSingleEndLogistics(self):
        '''点击单个停用'''
        self.wait
        self.find_element(*self.singleEndLogistics_loc).click()

    def clickSingleStartLogistics(self):
        '''点击单个启用'''
        self.wait
        self.find_element(*self.singleStartLogistics_loc).click()

    '''商品管理'''
    BaseSku_loc = (By.LINK_TEXT, u'商品管理')
    BatchSku_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/button")
    EndSku_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[4]/a")
    StartSku_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[5]/a")
    createSkuButton_loc = (By.XPATH, ".//*[@id='wrapper']/div[3]/div/div/div[2]/div/a")
    firstTitle_loc = (By.XPATH, ".//*[@id='addSkuBaseInfoTab']")
    allSelectSku_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[1]/a")
    stateSku_loc = (By.XPATH, ".//*[@id='sku243']/span")
    CreateSkuButton_loc = (By.XPATH, ".//*[@id='wrapper']/div[3]/div/div/div[2]/div/a")
    SkuReturnButton_loc = (By.XPATH, ".//*[@id='wrapper']/div[3]/div/div/div[2]/div/div/button[3]")
    infoSku_loc = (By.XPATH, ".//*[@id='wrapper']/div[3]/div/div/div[1]/h3")
    singleEditSKuButton_loc = (By.XPATH, '//*[@id="243"]/td[18]/div/button')
    singleStartSKu_loc = (By.XPATH, '//*[@id="243"]/td[18]/div/ul/li[1]/a')
    singleEndSKu_loc = (By.XPATH, '//*[@id="243"]/td[18]/div/ul/li[2]/a')
    def clickBaseSku(self):
        '''点击商品管理'''
        self.wait
        self.find_element(*self.BaseSku_loc).click()

    def clickBatchSku(self):
        '''商品批量操作'''
        self.wait
        self.find_element(*self.BatchSku_loc).click()

    def clickStartSku(self):
        '''商品批量启用'''
        self.wait
        self.find_element(*self.StartSku_loc).click()

    def clickEndSku(self):
        '''商品批量停用'''
        self.wait
        self.find_element(*self.EndSku_loc).click()

    def clickAllSelectSku(self):
        '''点击全选（商品管理）'''
        self.wait
        self.find_element(*self.allSelectSku_loc).click()

    def createSkuButton(self):
        '''点击创建商品按钮'''
        self.wait
        self.find_element(*self.createSkuButton_loc).click()

    def getFirstTitle(self):
        '''获取创建商品页面的首页title'''
        self.wait
        return self.find_element(*self.firstTitle_loc).text

    def checkStateSku(self):
        '''验证商品当前状态'''
        self.wait
        return self.find_element(*self.stateSku_loc).text

    def clickCreateSkuButton(self):
        '''点击创建商品'''
        self.wait
        self.find_element(*self.CreateSkuButton_loc).click()

    def clickReturnButtonSku(self):
        '''点击返回按钮（商品管理）'''
        self.wait
        self.find_element(*self.SkuReturnButton_loc).click()

    def getInfoSku(self):
        '''获取商品列表主页标题'''
        self.wait
        return self.find_element(*self.infoSku_loc).text

    def clickSingleEditSKuButton(self):
        '''点击单个编辑按钮'''
        self.wait
        self.find_element(*self.singleEditSKuButton_loc).click()

    def clickSingleEndSKu(self):
        '''点击单个停用'''
        self.wait
        self.find_element(*self.singleEndSKu_loc).click()

    def clickSingleStartSku(self):
        '''点击单个启用'''
        self.wait
        self.find_element(*self.singleStartSKu_loc).click()

    '''店铺'''
    BaseStore_loc = (By.LINK_TEXT, u'店铺')
    BatchStore_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/button")
    StartStore_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[5]/a")
    EndStore_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[4]/a")
    allSelectStore_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[1]/a")
    stateStore_loc = (By.XPATH, ".//*[@id='store13100000']/span")
    eidtStoreButton_loc = (By.XPATH, ".//*[@id='13100000']/td[15]/div/a")
    defectType_loc = (By.XPATH, ".//*[@id='addStoreDefectTypeInfoTab']")
    defectReson_loc = (By.XPATH, ".//*[@id='addStoreDefectReasonInfoTab']")
    warehouseStore_loc = (By.XPATH, "html/body/div[5]/div[3]/div/div/div/div/div/div/div/div/div/form/div/div[11]/div/ul/li/h2")
    singleEditStoreButton_loc = (By.XPATH, '//*[@id="13100000"]/td[15]/div/button')
    singleEndStore_loc = (By.XPATH, '//*[@id="13100000"]/td[15]/div/ul/li[2]/a')
    singleStartStore_loc = (By.XPATH, '//*[@id="13100000"]/td[15]/div/ul/li[1]/a')
    def clickBaseStore(self):
        '''点击店铺'''
        self.wait
        self.find_element(*self.BaseStore_loc).click()

    def clickBatchStore(self):
        '''点击店铺批量操作'''
        self.wait
        self.find_element(*self.BatchStore_loc).click()

    def clickStartStore(self):
        '''店铺批量启用'''
        self.wait
        self.find_element(*self.StartStore_loc).click()

    def clickEndStore(self):
        '''店铺批量停用'''
        self.wait
        self.find_element(*self.EndStore_loc).click()

    def clickAllSelectStore(self):
        '''点击全选（店铺）'''
        self.wait
        self.find_element(*self.allSelectStore_loc).click()

    def checkStateStore(self):
        '''验证店铺当前状态'''
        self.wait
        return self.find_element(*self.stateStore_loc).text

    def clickEditButtonStore(self):
        '''点击店铺编辑按钮'''
        self.wait
        self.find_element(*self.eidtStoreButton_loc).click()

    def getDefectTypeStore(self):
        '''获取店铺残次类型title'''
        self.wait
        return self.find_element(*self.defectType_loc).text

    def getDefectReasonStore(self):
        '''获取店铺残次原因title'''
        self.wait
        return self.find_element(*self.defectReson_loc).text

    def getWarehouseStore(self):
        '''获取店铺编辑页面下的物流仓列表title'''
        self.wait
        return self.find_element(*self.warehouseStore_loc).text

    def clickSingleEditStoreButton(self):
        '''点击单个编辑按钮'''
        self.wait
        self.find_element(*self.singleEditStoreButton_loc).click()

    def clickSingleEndStore(self):
        '''点击单个停用'''
        self.wait
        self.find_element(*self.singleEndStore_loc).click()

    def clickSingleStartStore(self):
        '''点击单个启用'''
        self.wait
        self.find_element(*self.singleStartStore_loc).click()

    '''度量单位配置'''
    BaseUom_loc = (By.LINK_TEXT, u'度量单位配置')
    BatchUom_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/button")
    StartUom_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/ul/li[4]/a")
    EndUom_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/ul/li[5]/a")
    createUomButton_loc = (By.CSS_SELECTOR, '.btn.btn-success')
    titleUom_loc = (By.XPATH, ".//*[@id='wrapper']/div[3]/div/h3")  #type, name, sign, rate
    uomType_loc = (By.CLASS_NAME, "select2-selection__rendered")
    uomTypeSelect_loc = (By.XPATH, "//ul[contains(@id,'select2-groupCode-')]")
    uomName_loc = (By.XPATH, ".//*[@id='addUomForm']/div[2]/div/input[1]")
    uomSign_loc = (By.XPATH, ".//*[@id='addUomForm']/div[3]/div/input")
    uomRate_loc = (By.XPATH, ".//*[@id='addUomForm']/div[4]/div/input")
    saveUom_loc = (By.XPATH, ".//*[@id='saveUomButton']")
    stateUom_loc = (By.XPATH, '//*[@id="uom9"]/span')
    allSelectUom_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/ul/li[1]/a')
    singleEditUomButton_loc = (By.XPATH, '//*[@id="9"]/td[7]/div/button')
    singleEndUom_loc = (By.XPATH, '//*[@id="9"]/td[7]/div/ul/li[2]/a')
    singleStartUom_loc = (By.XPATH, '//*[@id="9"]/td[7]/div/ul/li[1]/a')
    def clickBaseUom(self):
        '''点击度量单位配置'''
        self.wait
        self.find_element(*self.BaseUom_loc).click()

    def clickBatchUom(self):
        '''度量单位批量操作'''
        self.wait
        self.find_element(*self.BatchUom_loc).click()

    def clickEndUom(self):
        '''度量单位批量停用'''
        self.wait
        self.find_element(*self.EndUom_loc).click()

    def clickStartUom(self):
        '''度量单位批量启用'''
        self.wait
        self.find_element(*self.StartUom_loc).click()

    def clickUomButton(self):
        '''点击创建度量单位按钮'''
        self.wait
        self.find_element(*self.createUomButton_loc).click()

    def createUom(self, type, name, sign, rate):
        '''创建度量单位'''
        self.wait
        self.find_element(*self.uomType_loc).click()
        list = self.find_element(*self.uomTypeSelect_loc).find_elements(*self.Sign_loc)
        list[type].click()  # 选择单位类型
        self.wait
        self.find_element(*self.uomName_loc).send_keys(name)  # 输入单位名称
        self.wait
        self.find_element(*self.uomSign_loc).send_keys(sign)  # 输入单位符号
        self.wait
        self.find_element(*self.uomRate_loc).send_keys(rate)  # 输入换算率
        self.wait
        self.find_element(*self.saveUom_loc).click()

    def getTitleUom(self):
        '''获取创建度量单位页面的title'''
        self.wait
        return self.find_element(*self.titleUom_loc).text

    def getStateUom(self):
        '''获取度量单位状态'''
        self.wait
        return self.find_element(*self.stateUom_loc).text

    def clickAllSelectUom(self):
        '''点击全选按钮'''
        self.wait
        self.find_element(*self.allSelectUom_loc).click()

    def clickSingleEditUomButton(self):
        '''点击单个编辑按钮'''
        self.wait
        self.find_element(*self.singleEditUomButton_loc).click()

    def clickSingleEndUom(self):
        '''点击单个停用'''
        self.wait
        self.find_element(*self.singleEndUom_loc).click()

    def clickSingleStartUom(self):
        '''点击单个启用'''
        self.wait
        self.find_element(*self.singleStartUom_loc).click()

    '''供应商'''
    BaseSupplier_loc = (By.LINK_TEXT, u'供应商')
    BatchSupplier_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/button")
    StartSupplier_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[5]/a")
    EndSupplier_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[4]/a")
    allSelectSupplier_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[1]/a")
    stateSupplier_loc = (By.XPATH, ".//*[@id='supplier12100010']/span")
    createSupplierButton_loc = (By.XPATH, ".//*[@id='wrapper']/div[3]/div/div/div[2]/div/a")
    returnButtonSupplier_loc = (By.XPATH, ".//*[@id='wrapper']/div[3]/div/div/div[2]/div/div/button[3]")
    infoSupplier_loc = (By.XPATH, ".//*[@id='wrapper']/div[3]/div/div/div[1]/h3")
    supplierEditButton_loc = (By.XPATH, ".//*[@id='12100010']/td[10]/div/a")
    supplierEditTitle_loc = (By.XPATH, ".//*[@id='wrapper']/div[3]/div/h3")
    supplierTitle_loc = (By.XPATH, ".//*[@id='wrapper']/div[3]/div/h3") #name, code, type, customer, level, user, contact
    supplierName_loc = (By.XPATH, ".//*[@id='name']")
    supplierCode_loc = (By.XPATH, ".//*[@id='code']")
    supplierType_loc = (By.XPATH, ".//*[@id='select2-type-container']")
    supplierTypeSelect_loc = (By.XPATH, 'html/body/span/span')
    supplierCustomer_loc = (By.XPATH, ".//*[@id='select2-customerId-container']")
    supplierCustomerSelect_loc = (By.XPATH, "html/body/span/span")
    supplierLevel_loc = (By.XPATH, ".//*[@id='select2-level-container']")
    supplierLevelSelect_loc = (By.XPATH, "html/body/span/span")
    supplierUser_loc = (By.XPATH, ".//*[@id='user']")
    supplierContact_loc = (By.XPATH, ".//*[@id='contact']")
    saveSupplier_loc = (By.XPATH, ".//*[@id='save']")
    singleEditSupplierButton_loc = (By.XPATH, '//*[@id="12100010"]/td[10]/div/button')
    singleEndSupplier_loc = (By.XPATH, '//*[@id="12100010"]/td[10]/div/ul/li[2]/a')
    singleStartSupplier_loc = (By.XPATH, '//*[@id="12100010"]/td[10]/div/ul/li[1]/a')
    def clickBatchSupplier(self):
        '''点击供应商批量操作'''
        self.wait
        self.find_element(*self.BatchSupplier_loc).click()

    def clickBaseSupplier(self):
        '''点击供应商'''
        self.wait
        self.find_element(*self.BaseSupplier_loc).click()

    def clickSupplierButton(self):
        '''点击创建供应商按钮'''
        self.wait
        self.find_element(*self.createSupplierButton_loc).click()

    def createSupplier(self, name, code, type, customer, level, user, contact):
        '''创建供应商'''
        self.wait
        self.find_element(*self.supplierName_loc).send_keys(name)
        self.wait
        self.find_element(*self.supplierCode_loc).send_keys(code)
        self.wait
        self.find_element(*self.supplierType_loc).click()
        list = self.find_element(*self.supplierTypeSelect_loc).find_elements(*self.Sign_loc)
        list[type].click()
        self.wait
        self.find_element(*self.supplierCustomer_loc).click()
        list1 = self.find_element(*self.supplierCustomerSelect_loc).find_elements(*self.Sign_loc)
        list1[customer].click()
        self.wait
        self.find_element(*self.supplierLevel_loc).click()
        list2 = self.find_element(*self.supplierLevelSelect_loc).find_elements(*self.Sign_loc)
        list2[level].click()
        self.wait
        self.find_element(*self.supplierUser_loc).send_keys(user)
        self.wait
        self.find_element(*self.supplierContact_loc).send_keys(contact)
        self.wait
        self.find_element(*self.saveSupplier_loc).click()

    def getInfoSupplier(self):
        '''获取供应商主页面信息'''
        self.wait
        return self.find_element(*self.infoSupplier_loc).text

    def getTitleSupplier(self):
        '''获取创建供应商页面的title'''
        self.wait
        return self.find_element(*self.supplierTitle_loc).text

    def getEditTitleSupplier(self):
        '''获取供应商编辑页面的标题'''
        self.wait
        return self.find_element(*self.supplierEditTitle_loc).text

    def clickEditButtonSupplier(self):
        '''点击供应商编辑按钮'''
        self.wait
        self.find_element(*self.supplierEditButton_loc).click()

    def clickStartSupplier(self):
        '''供应商批量启用'''
        self.wait
        self.find_element(*self.StartSupplier_loc).click()

    def clickEndSupplier(self):
        '''供应商批量停用'''
        self.wait
        self.find_element(*self.EndSupplier_loc).click()

    def clickReturnButtonSupplier(self):
        '''点击返回按钮（供应商管理）'''
        self.wait
        self.find_element(*self.returnButtonSupplier_loc).click()

    def clickAllSelectSupplier(self):
        '''点击全选（供应商管理）'''
        self.wait
        self.find_element(*self.allSelectSupplier_loc).click()

    def checkStateSupplier(self):
        '''验证供应商当前状态'''
        self.wait
        return self.find_element(*self.stateSupplier_loc).text

    def clickSingleEditSupplierButton(self):
        '''点击单个编辑按钮'''
        self.wait
        self.find_element(*self.singleEditSupplierButton_loc).click()

    def clickSingleEndSupplier(self):
        '''点击单个停用'''
        self.wait
        self.find_element(*self.singleEndSupplier_loc).click()

    def clickSingleStartSupplier(self):
        '''点击单个启用'''
        self.wait
        self.find_element(*self.singleStartSupplier_loc).click()

    '''系统参数配置信息'''
    BaseSysdic_loc = (By.LINK_TEXT, u'系统参数配置信息')
    BatchSysdic_loc = (By.XPATH, '//*[@id="queryForm"]/div[2]/div/div/div[2]/div/div/div/div[1]/div/button')
    BatchEndSysdic_loc = (By.XPATH, '//*[@id="queryForm"]/div[2]/div/div/div[2]/div/div/div/div[1]/div/ul/li[5]/a')
    BatchStartSysdic_loc = (By.XPATH, '//*[@id="queryForm"]/div[2]/div/div/div[2]/div/div/div/div[1]/div/ul/li[4]/a')
    createSysdicButton_loc = (By.XPATH, '//*[@id="queryForm"]/div[1]/div[2]/div/a')
    groupName_loc = (By.XPATH, '//*[@id="select2-groupName-container"]')
    groupNameSelect_loc = (By.XPATH, '/html/body/span/span')
    groupCode_loc = (By.XPATH, '//*[@id="select2-groupCode-container"]')
    groupCodeSelect_loc = (By.XPATH, '/html/body/span/span')
    parameterName_loc = (By.XPATH, '//*[@id="addForm"]/div[3]/div/input')
    paramenterCode_loc = (By.XPATH, '//*[@id="addForm"]/div[4]/div/input')
    saveSysdicButton_loc = (By.XPATH, '//*[@id="saveButton"]')
    sysdicTitle_loc = (By.XPATH, '//*[@id="wrapper"]/div[3]/div/h3')

    def clickBaseSysdictionary(self):
        '''点击系统参数配置信息栏'''
        self.wait
        self.find_element(*self.BaseSysdic_loc).click()

    def clickBatchSysdictionary(self):
        '''点击批量操作'''
        self.wait
        self.find_element(*self.BatchSysdic_loc).click()

    def clickBatchEndSysdic(self):
        '''点击批量停用'''
        self.wait
        self.find_element(*self.BatchEndSysdic_loc).click()

    def clickBatchStartSysdic(self):
        '''点击批量启用'''
        self.wait
        self.find_element(*self.BatchStartSysdic_loc).click()

    def clickCreateSysdicButton(self):
        '''点击创建系统参数按钮'''
        self.wait
        self.find_element(*self.createSysdicButton_loc).click()

    def createSysdictonary(self, groupName, paramName, paramCode):
        '''创建系统参数'''
        self.wait
        self.find_element(*self.groupName_loc).click()
        list = self.find_element(*self.groupNameSelect_loc).find_elements(*self.Sign_loc)
        list[groupName].click()
        self.wait
        #级联问题
        # self.find_element(*self.groupCode_loc).click()
        # list1 = self.find_element(*self.groupCodeSelect_loc).find_elements(*self.Sign_loc)
        # list1[groupCode].click()
        # self.wait
        self.find_element(*self.parameterName_loc).send_keys(paramName)
        self.wait
        self.find_element(*self.paramenterCode_loc).send_keys(paramCode)
        self.wait
        self.find_element(*self.saveSysdicButton_loc).click()

    def getSysdicTitle(self):
        '''获取创建页面title'''
        self.wait
        return self.find_element(*self.sysdicTitle_loc).text

    '''国家省市区配置'''
    BaseRegion_loc = (By.LINK_TEXT, u'国家省市区配置')
    ListTitle_loc = (By.XPATH, '//*[@id="wrapper"]/div[4]/div/div/div[1]/h3')
    countryList_loc = (By.XPATH, '//*[@id="myTab"]/li[1]/a')
    provinceList_loc = (By.XPATH,'//*[@id="myTab"]/li[2]/a')
    cityList_loc = (By.XPATH, '//*[@id="myTab"]/li[3]/a')
    areaList_loc = (By.XPATH, '//*[@id="myTab"]/li[4]/a')
    addRegionButton_loc = (By.XPATH, '//*[@id="wrapper"]/div[4]/div/div/div[2]/div/a')
    BatchRegion_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[1]/div/button')
    BatchEndRegion_loc = (By.XPATH,'//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[1]/div/ul/li[5]/a')
    BatchStartRegion_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[1]/div/ul/li[4]/a')
    BatchDeleteRegion_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[1]/div/ul/li[6]/a')
    saveRegion_loc = (By.XPATH, '//*[@id="save"]')
    createTitle_loc = (By.XPATH, '//*[@id="wrapper"]/div[3]/div/h3')
    regionName_loc = (By.XPATH, '//*[@id="regionName"]')
    regionCode_loc = (By.XPATH, '//*[@id="regionCode"]')
    CountryName_loc = (By.XPATH, '//*[@id="select2-country-container"]')
    CountryNameSelect_loc = (By.XPATH, '/html/body/span/span')

    def clickBaseRegion(self):
        '''点击国家省市区配置'''
        self.wait
        self.find_element(*self.BaseRegion_loc).click()

    def getListTitle(self):
        '''获取页面标题'''
        self.wait
        return self.find_element(*self.ListTitle_loc).text

    def clickCountryList(self):
        '''点击国家列表'''
        self.wait
        self.find_element(*self.countryList_loc).click()

    def clickProvinceList(self):
        '''点击省列表'''
        self.wait
        self.find_element(*self.provinceList_loc).click()

    def clickCityList(self):
        '''点击市列表'''
        self.wait
        self.find_element(*self.cityList_loc).click()

    def clickAreaList(self):
        '''点击区列表'''
        self.wait
        self.find_element(*self.areaList_loc).click()

    def clickAddRegionButton(self):
        '''点击新增(国家、省、市、区)按钮'''
        self.wait
        self.find_element(*self.addRegionButton_loc).click()

    def clickBatchRegionButton(self):
        '''点击批量操作'''
        self.wait
        self.find_element(*self.BatchRegion_loc).click()

    def clickBatchEndRegion(self):
        '''点击批量停用'''
        self.wait
        self.find_element(*self.BatchEndRegion_loc).click()

    def clickBatchStartRegion(self):
        '''点击批量启用'''
        self.wait
        self.find_element(*self.BatchStartRegion_loc).click()

    def clickBatchDeleteRegion(self):
        '''点击批量删除'''
        self.wait
        self.find_element(*self.BatchDeleteRegion_loc).click()

    def getTitleInfo(self):
        '''获取创建页面主题'''
        self.wait
        return self.find_element(*self.createTitle_loc).text

    def createCountry(self, name, code):
        '''创建国家'''
        self.clickCountryList()
        self.clickAddRegionButton()
        self.wait
        self.find_element(*self.regionName_loc).send_keys(name)
        self.wait
        self.find_element(*self.regionCode_loc).send_keys(code)
        self.wait
        self.find_element(*self.saveRegion_loc).click()

    def createProvince(self, countryName, name, code):
        '''创建省'''
        self.clickProvinceList()
        self.clickAddRegionButton()
        self.wait
        self.find_element(*self.CountryName_loc).click()
        list = self.find_element(*self.CountryNameSelect_loc).find_elements(*self.Sign_loc)
        list[countryName].click()
        self.wait
        self.find_element(*self.regionName_loc).send_keys(name)
        self.wait
        self.find_element(*self.regionCode_loc).send_keys(code)
        self.wait
        self.find_element(*self.saveRegion_loc).click()

    def createCity(self, countryName, name, code):
        '''创建市'''
        self.clickCityList()
        self.clickAddRegionButton()
        self.wait
        self.find_element(*self.CountryName_loc).click()
        list = self.find_element(*self.CountryNameSelect_loc).find_elements(*self.Sign_loc)
        list[countryName].click()
        self.wait
        self.find_element(*self.regionName_loc).send_keys(name)
        self.wait
        self.find_element(*self.regionCode_loc).send_keys(code)
        self.wait
        self.find_element(*self.saveRegion_loc).click()

    def createArea(self, countryName, name, code):
        '''创建区'''
        self.clickAreaList()
        self.clickAddRegionButton()
        self.wait
        self.find_element(*self.CountryName_loc).click()
        list = self.find_element(*self.CountryNameSelect_loc).find_elements(*self.Sign_loc)
        list[countryName].click()
        self.wait
        self.find_element(*self.regionName_loc).send_keys(name)
        self.wait
        self.find_element(*self.regionCode_loc).send_keys(code)
        self.wait
        self.find_element(*self.saveRegion_loc).click()

    '''店铺品牌绑定查询和维护'''
    BaseBStore_loc = (By.LINK_TEXT, u'店铺品牌绑定查询和维护')
    BatchBStore_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/button')
    BatchEndBStore_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[5]/a')
    BatchStartBStore_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[4]/a')
    createBstoreButton_loc = (By.XPATH, '//*[@id="wrapper"]/div[3]/div/div/div/div[2]/div/a')
    SBrandName_loc = (By.XPATH, '//*[@id="select2-brand-container"]')
    SBrandNameSelect_loc = (By.XPATH, '/html/body/span/span')
    BStoreName_loc = (By.XPATH, '//*[@id="select2-store-container"]')
    BStoreNameSelect_loc = (By.XPATH, '/html/body/span/span')
    BrandStoreInfoTitle_loc = (By.XPATH, '//*[@id="wrapper"]/div[3]/div/div/div/div[1]/div[1]/div/h3')
    saveBrandStoreButton_loc = (By.XPATH, '//*[@id="addStoreBrand"]')

    def clickBaseBStore(self):
        '''点击店铺品牌绑定查询和维护'''
        self.wait
        self.find_element(*self.BaseBStore_loc).click()

    def clickBatchBStoreButton(self):
        '''点击批量操作'''
        self.wait
        self.find_element(*self.BatchBStore_loc).click()

    def clickBatchEndBStore(self):
        '''点击批量停用'''
        self.wait
        self.find_element(*self.BatchEndBStore_loc).click()

    def clickBatchStartBStore(self):
        '''点击批量启用'''
        self.wait
        self.find_element(*self.BatchStartBStore_loc).click()

    def clickCreateBSButton(self):
        '''点击创建品牌绑定店铺按钮'''
        self.wait
        self.find_element(*self.createBstoreButton_loc).click()

    def createBrandStore(self, brandName, storeName):
        '''创建店铺绑定品牌'''
        self.clickCreateBSButton()
        self.wait
        self.find_element(*self.SBrandName_loc).click()
        list = self.find_element(*self.SBrandNameSelect_loc).find_elements(*self.Sign_loc)
        list[brandName].click()
        self.wait
        self.find_element(*self.BStoreName_loc).click()
        list1 = self.find_element(*self.BStoreNameSelect_loc).find_elements(*self.Sign_loc)
        list1[storeName].click()
        self.wait
        self.find_element(*self.saveBrandStoreButton_loc).click()

    def getBStitleInfo(self):
        '''获取页面标题'''
        self.wait
        return self.find_element(*self.BrandStoreInfoTitle_loc).text
