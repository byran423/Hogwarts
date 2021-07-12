


from appium import webdriver
desire_cap = {
  "platformName": "Android",
  "deviceName": "860BDMM22KJX",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".view.WelcomeActivityAlias",
  "noReset": True,
  # 复用上次打开的app
  # "dontStopAppOnReset":True #
  # 跳过设备初始化，加快多用例运行速度
  "skipDeviceInitialization": True
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desire_cap)
driver.implicitly_wait(10)
el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[6]/android.widget.FrameLayout/android.widget.ImageView")
el1.click()
driver.implicitly_wait(10)
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ViewFlipper/android.widget.LinearLayout/android.widget.TextView")
el3.click()
driver.implicitly_wait(10)
el4 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el4.click()
el4.send_keys("阿里巴巴")
driver.implicitly_wait(10)
el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
el5.click()








