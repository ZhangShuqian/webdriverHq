#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from BasePage import Page

class WarePage(Page):
    '''组织切换'''
    clickOrangize_loc = (By.XPATH, ".//*[@id='wrapper']/div[1]/div[2]/div/div/ul/li[2]/a/span")
    clickOrangizeName_loc = (By.LINK_TEXT, "test仓")
    orangizeName_loc = (By.XPATH, ".//*[@id='wrapper']/div[1]/div[2]/div/div/ul/li[2]/a/span")
    def changeOrangize(self):
        '''切换组织'''
        self.wait
        self.find_element(*self.clickOrangize_loc).click()
        self.wait
        self.find_element(*self.clickOrangizeName_loc).click()

    def getOrangizeName(self):
        '''获取当前组织名称'''
        self.wait
        return self.find_element(*self.orangizeName_loc).text

    '''仓库基础信息栏'''
    BaseWarehouse_loc = (By.LINK_TEXT, u'仓库基础信息')
    def clickBaseWarehouse(self):
        '''点击仓库基础信息'''
        self.wait
        self.find_element(*self.BaseWarehouse_loc).click()

    '''区域管理'''
    BaseArea_loc = (By.LINK_TEXT, u'区域管理')
    BatchArea_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/button")
    StartArea_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[4]/a")
    EndArea_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[5]/a")
    promptInfo_loc = (By.CSS_SELECTOR, '.text')
    createAreaButton_loc = (By.XPATH, ".//*[@id='wrapper']/div[3]/div/div/div/div[2]/div/a")
    areaCode_loc = (By.XPATH, ".//*[@id='areaCode']")
    areaName_loc = (By.XPATH, ".//*[@id='areaName']")
    areaType_loc = (By.XPATH, ".//*[@id='select2-areaType-container']")
    areaTypeSelect_loc = (By.XPATH, "html/body/span/span")
    Sign_loc = (By.TAG_NAME, 'li')
    saveArea_loc = (By.XPATH, ".//*[@id='addArea']")
    infoTitleArea_loc = (By.XPATH, ".//*[@id='wrapper']/div[3]/div/div/div/div[1]/div[1]/div/h3")
    allSelectArea_loc = (By.XPATH, ".//*[@id='queryForm']/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[1]/a")
    StateInfoArea_loc = (By.XPATH, ".//*[@id='area15100014']/span")
    singleEditAreaButton_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[6]/div/button/span[1]')
    singleStartArea_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[6]/div/ul/li[1]/a')
    singleEndArea_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[6]/div/ul/li[2]/a')
    def clickBaseArea(self):
        '''点击区域管理'''
        self.wait
        self.find_element(*self.BaseArea_loc).click()

    def clickBatchAreaButton(self):
        '''点击批量操作'''
        self.wait
        self.find_element(*self.BatchArea_loc).click()

    def clickStartArea(self):
        '''点击批量启用'''
        self.wait
        self.find_element(*self.StartArea_loc).click()

    def clickEndArea(self):
        '''点击批量停用'''
        self.wait
        self.find_element(*self.EndArea_loc).click()

    def getPromptInfo(self):
        '''获取提示信息'''
        self.wait
        return self.find_element(*self.promptInfo_loc).text

    def clickCreateAreaButton(self):
        '''点击创建区域按钮'''
        self.wait
        self.find_element(*self.createAreaButton_loc).click()

    def createArea(self, code, name, type):
        '''创建区域'''
        self.wait
        self.find_element(*self.areaCode_loc).send_keys(code)
        self.wait
        self.find_element(*self.areaName_loc).send_keys(name)
        self.wait
        self.find_element(*self.areaType_loc).click()
        list = self.find_element(*self.areaTypeSelect_loc).find_elements(*self.Sign_loc)
        list[type].click()
        self.wait
        self.find_element(*self.saveArea_loc).click()

    def getInfoTitle(self):
        '''获取区域创建页面title'''
        self.wait
        return self.find_element(*self.infoTitleArea_loc).text

    def clickAllSelectArea(self):
        '''点击全选按钮'''
        self.wait
        self.find_element(*self.allSelectArea_loc).click()

    def getStateInfoArea(self):
        '''获取区域状态信息'''
        self.wait
        return self.find_element(*self.StateInfoArea_loc).text

    def clickSingleEditButton(self):
        '''点击单个编辑按钮'''
        self.wait
        self.find_element(*self.singleEditAreaButton_loc).click()

    def clickSingleEndArea(self):
        '''点击单个停用区域按钮'''
        self.wait
        self.find_element(*self.singleEndArea_loc).click()

    def clickSingleStartArea(self):
        '''点击单个启用区域按钮'''
        self.wait
        self.find_element(*self.singleStartArea_loc).click()

    '''物理仓残次信息维护'''
    BaseDefect_loc = (By.LINK_TEXT, u'物理仓残次信息维护')
    CreateDefectButton_loc = (By.XPATH, ".//*[@id='wrapper']/div[3]/div/div/div[2]/div/a")
    EditDefectButton_loc = (By.XPATH, '//*[@id="12100001"]/td[6]/div/a')
    EditTitleInfo_loc = (By.XPATH, '//*[@id="wrapper"]/div[3]/div/h3')
    singleEditDefectButton_loc = (By.XPATH, '//*[@id="12100001"]/td[6]/div/button')
    singleEndDefect_loc = (By.XPATH, '//*[@id="12100001"]/td[6]/div/ul/li[2]/a')
    singleStartDefect_loc = (By.XPATH, '//*[@id="12100001"]/td[6]/div/ul/li[1]/a')
    StateInfoDefect_loc = (By.XPATH, '//*[@id="warehouseDefectType12100001"]/span')
    CreateTitleInfo_loc = (By.XPATH, '//*[@id="wrapper"]/div[3]/div/h3')
    defectTypeCode_loc = (By.XPATH, '//*[@id="warehouseDefectTypeCode"]')
    defectTypeName_loc = (By.XPATH, '//*[@id="warehouseDefectTypeName"]')
    addDefectButton_loc = (By.XPATH, '//*[@id="addDefectReason"]')
    deleteDefectButton_loc = (By.XPATH, '//*[@id="removeDefectReason"]')
    saveDefectButton_loc = (By.XPATH, '//*[@id="saveOrUpdate"]')
    defectReasonCode_loc = (By.XPATH, '//*[@id="warehouseDefectReasonsBody"]/tr[2]/td[2]/input')
    defectReasonName_loc = (By.XPATH, '//*[@id="warehouseDefectReasonsBody"]/tr[2]/td[3]/input')
    def clickBaseDefect(self):
        '''点击物理仓残次信息维护'''
        self.wait
        self.find_element(*self.BaseDefect_loc).click()

    def clickEditDefectButton(self):
        '''点击编辑按钮'''
        self.wait
        self.find_element(*self.EditDefectButton_loc).click()

    def getEditTitleInfo(self):
        '''获取编辑页面title信息'''
        self.wait
        return self.find_element(*self.EditTitleInfo_loc).text

    def clickSingleEditDefectButton(self):
        '''点击单个编辑按钮'''
        self.wait
        self.find_element(*self.singleEditDefectButton_loc).click()

    def clickSingleEndDefectButton(self):
        '''点击单个停用按钮'''
        self.wait
        self.find_element(*self.singleEndDefect_loc).click()

    def clickSingleStartDefectButton(self):
        '''点击单个启用按钮'''
        self.wait
        self.find_element(*self.singleStartDefect_loc).click()

    def getStateInfoDefect(self):
        '''获取残次类型的状态信息'''
        self.wait
        return self.find_element(*self.StateInfoDefect_loc).text

    def createDefectType(self, code, name):
        '''创建残次类型'''
        self.wait
        self.find_element(*self.defectTypeCode_loc).send_keys(code)
        self.wait
        self.find_element(*self.defectTypeName_loc).send_keys(name)

    def defectReasonCode(self, code):
        '''填写残次原因编码'''
        self.wait
        self.find_element(*self.defectReasonCode_loc).send_keys(code)

    def defectReasonName(self, name):
        '''填写残次原因名称'''
        self.wait
        self.find_element(*self.defectReasonName_loc).send_keys(name)

    def clickSaveDefectButton(self):
        '''点击保存按钮'''
        self.wait
        self.find_element(*self.saveDefectButton_loc).click()

    def clickAddDefectReasonButton(self):
        '''点击新增残次原因按钮'''
        self.wait
        self.find_element(*self.addDefectButton_loc).click()

    def clickRemoveDefectReasonButton(self):
        '''点击删除残次原因按钮'''
        self.wait
        self.find_element(*self.deleteDefectButton_loc).click()

    def clickCreateDefectButton(self):
        '''点击创建残次类型按钮'''
        self.wait
        self.find_element(*self.CreateDefectButton_loc).click()

    '''库位模板配置'''
    BaseTemplet_loc = (By.LINK_TEXT, u'库位模板配置')
    BatchTemplet_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/button')
    BatchEndTemplet_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[4]/a')
    BatchStartTemplet_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[5]/a')
    BatchAllSelectTemplet_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[1]/a')
    stateInfoTemplet_loc = (By.XPATH, '//*[@id="lt17100022"]/span')
    SingleEditTempletButton_loc = (By.XPATH, '//*[@id="17100022"]/td[5]/div/button')
    SingleStartTemplet_loc = (By.XPATH, '//*[@id="17100022"]/td[5]/div/ul/li[1]/a')
    SingleEndTemplet_loc = (By.XPATH, '//*[@id="17100022"]/td[5]/div/ul/li[2]/a')
    createTempletButton_loc = (By.XPATH, '//*[@id="wrapper"]/div[3]/div/div[1]/div[2]/div/a')
    templetCode_loc = (By.XPATH, '//*[@id="templetCode"]')
    templetName_loc = (By.XPATH, '//*[@id="templetName"]')
    templetLong_loc = (By.XPATH, '//*[@id="length"]')
    templetWide_loc = (By.XPATH, '//*[@id="width"]')
    templetHigh_loc = (By.XPATH, '//*[@id="high"]')
    templetVolume_loc = (By.XPATH, '//*[@id="volume"]')
    templetWeight_loc = (By.XPATH, '//*[@id="weight"]')
    templetDimensionality_loc = (By.XPATH, '//*[@id="ruleInfoDiv"]/div/div/div[1]/div/input')
    dimensionalityButton_loc  = (By.XPATH, '//*[@id="ruleInfoDivController"]/i')
    saveTemplet_loc = (By.XPATH, '//*[@id="save"]')
    CreateTempletTitle_loc = (By.XPATH, '//*[@id="wrapper"]/div[3]/div/h3')
    PlusButton_loc = (By.XPATH, '//*[@id="addRuleButton"]/i')
    dimensionalityName_loc = (By.XPATH, '//*[@id="ruleInfoDiv"]/div/div/div[2]/label[1]')
    def clickBaseTemplet(self):
        '''点击库位模板配置'''
        self.wait
        self.find_element(*self.BaseTemplet_loc).click()

    def clickBatchTempletButton(self):
        '''点击批量操作（库位模板）'''
        self.wait
        self.find_element(*self.BatchTemplet_loc).click()

    def clickBatchEndTemplet(self):
        '''点击批量停用'''
        self.wait
        self.find_element(*self.BatchEndTemplet_loc).click()

    def clickBatchStartTemplet(self):
        '''点击批量启用'''
        self.wait
        self.find_element(*self.BatchStartTemplet_loc).click()

    def clickBatchAllSelectTemplet(self):
        '''点击全选'''
        self.wait
        self.find_element(*self.BatchAllSelectTemplet_loc).click()

    def getTempletStateInfo(self):
        '''获取库位模板状态'''
        self.wait
        return self.find_element(*self.stateInfoTemplet_loc).text

    def clickSingleEditTempletButton(self):
        '''点击单个编辑库位模板按钮'''
        self.wait
        self.find_element(*self.SingleEditTempletButton_loc).click()

    def clickSingleStartTemplet(self):
        '''点击单个启用'''
        self.wait
        self.find_element(*self.SingleStartTemplet_loc).click()

    def clickSingleEndTemplet(self):
        '''点击单个停用'''
        self.wait
        self.find_element(*self.SingleEndTemplet_loc).click()

    def clickCreateTempletButton(self):
        '''点击创建库位模板按钮'''
        self.wait
        self.find_element(*self.createTempletButton_loc).click()

    def createTemplet(self, name, code, long, wide, high, volume, weight):
        '''创建库位模板'''
        self.wait
        self.find_element(*self.templetName_loc).send_keys(name)
        self.wait
        self.find_element(*self.templetCode_loc).send_keys(code)
        self.wait
        self.find_element(*self.templetLong_loc).send_keys(long)
        self.wait
        self.find_element(*self.templetWide_loc).send_keys(wide)
        self.wait
        self.find_element(*self.templetHigh_loc).send_keys(high)
        self.wait
        self.find_element(*self.templetVolume_loc).send_keys(volume)
        self.wait
        self.find_element(*self.templetWeight_loc).send_keys(weight)

    def clickAddDimensionalityButton(self):
        '''点击展开维度页面按钮'''
        self.wait
        self.find_element(*self.dimensionalityButton_loc).click()

    def createDimensionality(self, dimensionality):
        '''创建维度'''
        self.wait
        self.find_element(*self.templetDimensionality_loc).send_keys(dimensionality)

    def clickSaveTempletButton(self):
        '''点击保存按钮'''
        self.wait
        self.find_element(*self.saveTemplet_loc).click()

    def getCreateTempletInfo(self):
        '''获取创建页面title'''
        self.wait
        return self.find_element(*self.CreateTempletTitle_loc).text

    def clickPlusDimensionality(self):
        '''点击加号添加维度'''
        self.wait
        self.find_element(*self.PlusButton_loc).click()

    def getDimensionalityName(self):
        '''获取维度名称'''
        self.wait
        return self.find_element(*self.dimensionalityName_loc).text

    '''库位配置'''
    BaseLocation_loc = (By.LINK_TEXT, u'库位配置')
    createLocationButton_loc = (By.XPATH, '//*[@id="wrapper"]/div[3]/div/div/div[2]/div/a[1]')
    BatchLocation_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/button')
    BatchStartLocation_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[4]/a')
    BatchEndLocation_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[5]/a')
    BatchAllSelectLocation_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[1]/a')
    BatchDeleteLocation_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[6]/a')
    StateInfoLocation_loc = (By.XPATH, '//*[@id="location18102861"]/span')
    FixLocationButton_loc = (By.XPATH, '//*[@id="wrapper"]/div[3]/div/div/div[2]/div/a[2]')
    RemoveLocationButton_loc = (By.XPATH, '//*[@id="wrapper"]/div[3]/div/div/div[2]/div/a[3]')
    createTitle_loc = (By.XPATH, '//*[@id="myTab"]/li[1]/a')
    fixTitle_loc = (By.XPATH, '//*[@id="wrapper"]/div[3]/div/div[1]/div/h3')
    removeTitle_loc = (By.XPATH, '//*[@id="wrapper"]/div[4]/div/h3')
    def clickBaseLocation(self):
        '''点击库位配置'''
        self.wait
        self.find_element(*self.BaseLocation_loc).click()

    def clickBatchLocation(self):
        '''点击批量操作'''
        self.wait
        self.find_element(*self.BatchLocation_loc).click()

    def clickBatchStartLocation(self):
        '''点击批量启用'''
        self.wait
        self.find_element(*self.BatchStartLocation_loc).click()

    def clickBatchEndLocation(self):
        '''点击批量停用'''
        self.wait
        self.find_element(*self.BatchEndLocation_loc).click()

    def clickBatchAllSelectLocation(self):
        '''点击全选'''
        self.wait
        self.find_element(*self.BatchAllSelectLocation_loc).click()

    def clickBatchDeleteLocation(self):
        '''点击批量删除'''
        self.wait
        self.find_element(*self.BatchDeleteLocation_loc).click()

    def getLocationStateInfo(self):
        '''获取库位状态'''
        self.wait
        return self.find_element(*self.StateInfoLocation_loc).text

    def clickCreateLocationButton(self):
        '''点击创建库位按钮'''
        self.wait
        self.find_element(*self.createLocationButton_loc).click()

    def clickFixLocationButton(self):
        '''点击库位批量修改按钮'''
        self.wait
        self.find_element(*self.FixLocationButton_loc).click()

    def clickRemoveLocationButton(self):
        '''点击库位批量删除按钮'''
        self.wait
        self.find_element(*self.RemoveLocationButton_loc).click()

    def getCreateTitle(self):
        '''获取创建库位页面title'''
        self.wait
        return self.find_element(*self.createTitle_loc).text

    def getFixTitle(self):
        '''获取批量修改库位页面title'''
        self.wait
        return self.find_element(*self.fixTitle_loc).text

    def getRemoveTitle(self):
        '''获取批量删除库位页面title'''
        self.wait
        return self.find_element(*self.removeTitle_loc).text

    '''二级容器管理'''
    BaseContainer_loc = (By.LINK_TEXT, u'二级容器管理')
    BatchContainer_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/button')
    BatchAllSelectContainer_loc  = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[1]/a')
    BatchEndContainer_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[4]/a')
    BatchStartContainer_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[5]/a')
    stateContainer_loc = (By.XPATH, '//*[@id="container2ndCategory13100006"]/span')
    singleEditContainer_loc = (By.XPATH, '//*[@id="13100006"]/td[7]/div/button')
    singleEndContainer_loc = (By.XPATH, '//*[@id="13100006"]/td[7]/div/ul/li[2]/a')
    singleStartContainer_loc = (By.XPATH, '//*[@id="13100006"]/td[7]/div/ul/li[1]/a')
    createContainerButton_loc = (By.XPATH, '//*[@id="wrapper"]/div[3]/div/div/div[2]/div/a')
    firstContainerType_loc = (By.XPATH, '//*[@id="select2-oneLevelType-container"]')
    firstContainerTypeSelec_loc = (By.XPATH, '/html/body/span/span')
    secondContainerName_loc = (By.XPATH, '//*[@id="categoryName"]')
    secondContainerCode_loc = (By.XPATH, '//*[@id="categoryCode"]')
    codeBuilder_loc = (By.XPATH, '//*[@id="select2-codeGenerator-container"]')
    codeBuilderSelec_loc = (By.XPATH, '/html/body/span/span')
    containerLong_loc = (By.XPATH, '//*[@id="length"]')
    containerWide_loc = (By.XPATH, '//*[@id="width"]')
    containerHigh_loc = (By.XPATH, '//*[@id="high"]')
    lwhUnit_loc = (By.XPATH, '//*[@id="select2-lengthUom-container"]')
    lwhUnitSele_loc = (By.XPATH, '/html/body/span/span')
    containerVolume_loc = (By.XPATH, '//*[@id="volume"]')
    volumeUnit_loc = (By.XPATH, '//*[@id="select2-volumeUom-container"]')
    volumeUnitSele_loc = (By.XPATH, '/html/body/span/span')
    containerWeigh_loc = (By.XPATH, '//*[@id="weight"]')
    weightUnit_loc = (By.XPATH, '//*[@id="select2-weightUom-container"]')
    weightUnitSele_loc = (By.XPATH, '/html/body/span/span')
    saveContainer_loc = (By.XPATH, '//*[@id="save"]')
    infoTitleContainer_loc = (By.XPATH, '//*[@id="wrapper"]/div[3]/div/h3')

    def clickBaseContainer(self):
        '''点击二级容器管理'''
        self.wait
        self.find_element(*self.BaseContainer_loc).click()

    def clickBatchContainerButton(self):
        '''点击批量操作'''
        self.wait
        self.find_element(*self.BatchContainer_loc).click()

    def clickBatchAllSelectContainer(self):
        '''点击全选'''
        self.wait
        self.find_element(*self.BatchAllSelectContainer_loc).click()

    def clickBatchEndContainer(self):
        '''点击批量停用'''
        self.wait
        self.find_element(*self.BatchEndContainer_loc).click()

    def clickBatchStartContainer(self):
        '''点击批量启用'''
        self.wait
        self.find_element(*self.BatchStartContainer_loc).click()

    def getContainerState(self):
        '''获取二级容器当前状态'''
        self.wait
        return self.find_element(*self.stateContainer_loc).text

    def clickSingleEditContainer(self):
        '''点击单个编辑按钮'''
        self.wait
        self.find_element(*self.singleEditContainer_loc).click()

    def clickSingleEndContainer(self):
        '''点击单个停用'''
        self.wait
        self.find_element(*self.singleEndContainer_loc).click()

    def clickSingleStartContainer(self):
        '''点击单个启用'''
        self.wait
        self.find_element(*self.singleStartContainer_loc).click()

    def clickCreateContainerButton(self):
        '''点击创建二级容器按钮'''
        self.wait
        self.find_element(*self.createContainerButton_loc).click()

    def getInfoTitleContainer(self):
        '''获取页面标题'''
        self.wait
        return self.find_element(*self.infoTitleContainer_loc).text

    def createContainer(self, firstLevel, secLevelName, secLevelCode, codeBulider, long, wide, high, lengthUom, volume, volumeUom, weight, weightUom):
        '''创建二级容器'''
        self.clickCreateContainerButton()   #点击创建二级容器按钮
        self.wait
        self.find_element(*self.firstContainerType_loc).click() #点击一级容器类型
        list = self.find_element(*self.firstContainerTypeSelec_loc).find_elements(*self.Sign_loc)
        list[firstLevel].click()    #选择一级容器类型
        self.wait
        self.find_element(*self.secondContainerName_loc).send_keys(secLevelName)    #输入二级容器名称
        self.wait
        self.find_element(*self.secondContainerCode_loc).send_keys(secLevelCode)    #输入二级容器编码
        self.wait
        self.find_element(*self.codeBuilder_loc).click()    #点击编码生成器
        list1 = self.find_element(*self.codeBuilderSelec_loc).find_elements(*self.Sign_loc)
        list1[codeBulider].click()  #选择编码生成器
        self.wait
        self.find_element(*self.containerLong_loc).send_keys(long)  #输入长
        self.wait
        self.find_element(*self.containerWide_loc).send_keys(wide)  #输入宽
        self.wait
        self.find_element(*self.containerHigh_loc).send_keys(high)  #输入高
        self.wait
        self.find_element(*self.lwhUnit_loc).click()    #点击长宽高单位
        list2 = self.find_element(*self.lwhUnitSele_loc).find_elements(*self.Sign_loc)
        list2[lengthUom].click()    #选择长宽高单位
        self.wait
        self.find_element(*self.containerVolume_loc).send_keys(volume)  #输入体积
        self.wait
        self.find_element(*self.volumeUnit_loc).click() #点击体积单位
        list3 = self.find_element(*self.volumeUnitSele_loc).find_elements(*self.Sign_loc)
        list3[volumeUom].click()    #选择体积单位
        self.wait
        self.find_element(*self.containerWeigh_loc).send_keys(weight)   #输入重量
        self.wait
        self.find_element(*self.weightUnit_loc).click() #点击重量单位
        list4 = self.find_element(*self.weightUnitSele_loc).find_elements(*self.Sign_loc)
        list4[weightUom].click()    #选择重量单位
        self.wait
        self.find_element(*self.saveContainer_loc).click()  #点击保存按钮

    '''月台列表'''
    BasePlatform_loc = (By.LINK_TEXT, u'月台列表')
    BatchPlatform_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/button')
    BatchEndPlatform_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[5]/a')
    BatchStartPlatform_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[4]/a')
    BatchAllSelectPlatform_loc = (By.XPATH, '//*[@id="queryForm"]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/ul/li[1]/a')
    statePlatform_loc = (By.XPATH, '//*[@id="platform14100007"]/span')
    singleEditPlatform_loc = (By.XPATH, '//*[@id="14100007"]/td[6]/div/button')
    singleEndPlatform_loc = (By.XPATH, '//*[@id="14100007"]/td[6]/div/ul/li[2]/a')
    singleStartPlatform_loc = (By.XPATH, '//*[@id="14100007"]/td[6]/div/ul/li[1]/a')
    createPlatformButton_loc = (By.XPATH, '//*[@id="wrapper"]/div[3]/div/div/div[2]/div/a')
    platformName_loc = (By.XPATH, '//*[@id="platformName"]')
    platformCode_loc = (By.XPATH, '//*[@id="platformCode"]')
    platformType_loc = (By.XPATH, '//*[@id="select2-platformType-container"]')
    platformTypeSele_loc = (By.XPATH, '/html/body/span/span')
    savePlatform_loc = (By.XPATH, '//*[@id="saveOrUpdate"]')
    infoTitlePlatform_loc = (By.XPATH, '//*[@id="wrapper"]/div[3]/div/h3')

    def clickBasePlatform(self):
        '''点击月台列表'''
        self.wait
        self.find_element(*self.BasePlatform_loc).click()

    def clickBatchPlatform(self):
        '''点击批量操作'''
        self.wait
        self.find_element(*self.BatchPlatform_loc).click()

    def clickBatchAllSelePlatform(self):
        '''点击全选'''
        self.wait
        self.find_element(*self.BatchAllSelectPlatform_loc).click()

    def clickBatchEndPlatform(self):
        '''点击批量停用'''
        self.wait
        self.find_element(*self.BatchEndPlatform_loc).click()

    def clickBatchStartPlatform(self):
        '''点击批量启用'''
        self.wait
        self.find_element(*self.BatchStartPlatform_loc).click()

    def getStatePlatform(self):
        '''获取月台状态'''
        self.wait
        return self.find_element(*self.statePlatform_loc).text

    def clickCreatePlatformButton(self):
        '''点击创建月台按钮'''
        self.wait
        self.find_element(*self.createPlatformButton_loc).click()

    def createPlatform(self, platformCode, platformName, platType):
        '''创建月台'''
        self.clickCreatePlatformButton()
        self.wait
        self.find_element(*self.platformCode_loc).send_keys(platformCode)
        self.wait
        self.find_element(*self.platformName_loc).send_keys(platformName)
        self.wait
        self.find_element(*self.platformType_loc).click()
        list = self.find_element(*self.platformTypeSele_loc).find_elements(*self.Sign_loc)
        list[platType].click()
        self.wait
        self.find_element(*self.savePlatform_loc).click()

    def getplatformTitle(self):
        '''获取创建页面的title'''
        self.wait
        return self.find_element(*self.infoTitlePlatform_loc).text

    def clickSingleEditPlatformButton(self):
        '''点击单个编辑按钮'''
        self.wait
        self.find_element(*self.singleEditPlatform_loc).click()

    def clickSingleEndPlatform(self):
        '''点击单个停用'''
        self.wait
        self.find_element(*self.singleEndPlatform_loc).click()

    def clickSingleStartPlatform(self):
        '''点击单个启用'''
        self.wait
        self.find_element(*self.singleStartPlatform_loc).click()