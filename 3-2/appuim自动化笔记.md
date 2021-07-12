### appium环境和架构
* 自动化工具的选择
    * 单平台or多平台
    * 是否有多设备同时测试的场景
    * 不局限于测试环境，任何版本任何环境都可以测试？
    * 最擅长哪种开发语言
    * 当前市面是否有满足项目需求的测试工具？是否需要二次开发？
    
* appium 生态工具
    * adb: android 的控制工具，用于获取andriod的各种数据和控制
    * Appium Desktop： 内嵌了appium server 和inspector的综合工具
    * Appium Server: appium 的核心工具，命令行工具
    * Appium client：各种语言的客户端封装库，用于连接appium server
        * Python、Java、ruby、robotframework-appium
    * APPCrawler 自动遍历工具
* 环境要求：
    * Java1.8
    * Android sdk
    * Node js
    * Python3
    * appium-desktop
    * appium python client
    
### appium录制
* 查看设备 adb devices
* 查看包 adb logcat|grep -i displayed
* app 信息
    * **获取当前界面元素 adb shell dumpsys activity top** 
    * 获取任务列表 adb shell dumpsys activity activities
* app入口：
    * **adb logcat |grep -i displayed** 
    * adb logcat ActivityManager:I |grep 'cmp'
    * aapt dump badging mobike.apk |grep launchable-activity
    * apkanalyzer 最新版本的sdk中才有
* 启动应用
    * **adb shell am start -W -n com.xueqiu.android/.view.WelcomeActivityAlias -S **
* python -m weditor 网页获取元素
    
### 元素定位和等待
* 测试用例组成
    * 导入依赖 webdriver
    * capability 设置
    * 初始化 driver：
        * python webdriver.remote
    * 隐式等待，增强用例的稳定性
    * 元素定位与操作 find+action
    * 断言 
* Capability 设置
    * app apk地址
    * appPackage 包名
    * APPActivity Activity名字
    * automationName 默认使用uiautomator2（Android默认使用uiautomator2，ios默认使用XCUITest）
    * noReset fullReset 是否在测试前后重置相关环境（例如首次打开弹窗，或者是登录信息）
    * unicodeKeyBoard resetKeyBoard 是否需要输入非英文之外的语言在测试完成后重置输入法
    * dontStopAppOnReset 首次启动的时候，不停止app（可以调试或者运行的时候提升运行速度）
    * skipDeviceInitialization 跳过设备初始化（可以调试或者运行的时候提升运行速度）
* 元素定位方式：id,accessibility_id
    * driver.find_element_by_id(resource-id)
    * driver.find_element_by_accessibility_id(content_desc)
    
* Android 七大布局
    * LinearLayout （线性布局）-- 水平，垂直
    * RelativeLayout （相对布局）
    * FrameLayout(帧布局)
    * AbsoluteLayout(绝对布局)
    * TableLayout （表格布局）
    * GridLayout(网格布局)
    * ConstraintLayout （约束布局）        
* Android 四大组件
    * activity 与用户交互的可视化界面
    * service 实现程序后台运行的解决方案
    * content provider 内容提供者、提供程序所需要的数据
    * broadcast receiver 广播接收器，监听外部事件的到来（比如来电）
* 常用控件
    * TextView（文本控件），EditText（可编辑文本控件）
    * Button（按钮），ImageButton（图片按钮），ToggleButton（开关按钮）
    * ImageView （图片控件）
    * CheckBox （复选框控件） RadioButton（单选框控件）
* dom: Document Object Model 文档对象模型
* dom 常见的格式为HTML、xml 核心元素为节点和属性
* Android 应用没有css属性

* Android 定位工具
    * 推荐使用 uiautomatorviewer工具
    * Appium Inspector工具太重
    
* Xpath表达式常用用法：
    * not、contains、ends_with、starts_with
    * and 、or
* 元素定位
    * Id 定位(优先级最高)
    * Xpath定位（速度慢，定位灵活）
    * CSS定位
    * Accessibility ID定位(content-desc)
    * Uiautomator定位（仅安卓速度快，语法复杂）
    * Predicate定位（仅iOS）
* Xpath定位：
    * //*[contains(@resource-id,'login')]
    * //*[text='登录']
    * //*[contains(@resource-id,'login') and contains(@text,'登录')]
* 元素常用方法
    * 输入操作 ele.send_keys('')
    * 设置元素的值 ele.set_value('')
    * 清除操作 ele.clear()
    * 是否可见 ele.is_displayed()
    * 是否可用 ele.is_enabled()
    * 是否被选中 ele.is_selected()  
    * 获取属性值 get_attribute(name)
* 元素属性
    * 获取元素文本 element.text
    * 获取元素坐标 element.location
    * 获取元素尺寸 ele.size
* TouchActions 和MultiAction 点按和多指操作
    * 多指操作
    
    ```
    action0 = TouchAction().tap(el)

    action1 = TouchAction().tap(el)

    MultiAction().add(action0).add(action1).perform()

    ```
* 滑动操作
    * move_to(x=,y=).release().perform()
    
```

def test_touchaction(self):

    action = TouchAction(self.driver)

    window_rect = self.driver.get_window_rect()

    width = window_rect('width')

    height = window_rect('height')

    x1 = int(width/2)

    y_start  = int(height * 4/5)

    y_end = int(height * 1/5)

    action.press(x=1,y = y_start).wait(200).move_to(x=x1,y=y_end).release().perform()

```

### 等待
* 全局隐式等待
    * 在服务端等待
* 显示等待
    * 在客户端等待
    * WebDriverWait(self.driver,10).until(expected_conditons.visibility_of_element_located)(LOCATOR)
* 区别
    * 显示等待在客户端，隐式等待在服务端
    * 隐式等待在整个session生命周期生效，显示等待在写了显示等待的地方生效
* 为什么要显示等待
    * 显示等待可以等待动态加载的ajax元素，显示等待需要使ExpectCo nditions来检查条件
* toast 定位
    * appium使用uiautomator底层的机制来分析抓取toast，并且把toast放到控件树里面，但本身并不属于控件
    * automationName：uiautomator2
    * 必须使用xpath查找
        * //*[@class='android.widget.Toast']
        * //*[contians(@text,"xxxxx")]
    * adb shell dumpsys window | grep mCurrent  获取当前界面activity
    *  setup中添加 ’automationName' ：‘uiautomator2’ 
    
    ```

    self.driver.find_element(MobileBy.Xpath, "//*[@class = xxxx]")

    self.driver.find_element(MobileBy.Xpath,"//*[contains(@text, 'xxxx')]"

    ```    
### 高级定位技巧
* Xpath 定位进阶
    * 父节点定位子节点
    * 子节点定位父节点
    * 子节点定位兄弟节点
    * 爷爷节点定位孙子节点
* uiautomator 定位 driver.find_element_by_android_uiautomator(表达式)
    * 通过resource-id 定位
        * new Uiselector().resourceId("id")
    * 通过 classname 定位
        * new Uiselector().className("className")
    * 通过 content-desc定位
        * new Uiselector().description("content-des属性")
    * 通过文本定位
        * new Uiselector.text("")
        * new Uiselector.textContains("")
        * new Uiselector.textStartsWith("")
        * new Uiselector.textMatches("正则表达式")
    * 组合定位
    * 通过父子关系定位
        * childSelector
    * 兄弟定位
        * fromParent    
    * 通过滚动查找元素
        * new UiScrollable(newUiselector().scrollable(true).instance(0)).scrollIntoView(newUiselector().text("查找的文本").instance(0));
        
### 断言
* hamcrest 断言
    * hamcrest 框架介绍
        * hamcrest 是一个为了测试目的，能组合成灵活表达式的匹配器类库，用于编写断言的框架，使用这个框架编写断言，提高可读性及开发测试的效率
        * hamcrest 提供了大量被称为“匹配器”的方法，每个匹配器都设计用于执行特定的比较操作
        * hamcrest 的可扩展性强，让你能够创建自定义的匹配器
        * 支持多种语言 Java，Python，ruby
        
### Android 纯web页面测试
* 多架构     
    * Native APP ，Hybrid App  ，Web APP
* 获取手机浏览器包名-- adb shell pm list package|grep browser
* 获取手机浏览器版本信息 -- adb shell pm dump com.android.browser|grep version
* Web App 网 页app
    * 通过Chrome自带的chrome://inspect/#devices 可以连接remote远程调试安卓模拟器或者真机
* Hybrid App 混合页面
    * 如何判断页面是   webview
        * 断网查看
        * 看加载条
        * 看顶部是否有关闭按钮
        * 下拉刷新 页面是否刷新
        * 下拉刷新的时候，是否有网页提供方
        * 用工具查看
    * Webview
        * 是Android系统提供能显示网页的系统控价（特殊的view）
        * < Android 4.4 Webview底层实现Webkit内核
        *  `>= Android4.4 Google采用chromium作为系统Webview底层支持，API没有变，支持HTML5，CSS3，JavaScript
    * 准备工作
        * 下载app内Chrome版本对应的webdriver
        * app代码需要打开Webview开关
            * Android6.0 不打开也能查看页面结构(mumu 不可以，genimotion和sdk自带的emulator可以)
            * 启动Webdriver 调试，请在Webdriver类上调用静态方法 setWebContentsDebuggingEnabled 
        * 代码
            * appPackage，appActivity
            * des_cap 里面添加 chromedriverExecutable ： driver路径
        * 切换上下文 进行native APP 和内嵌的web app 定位转换
            * 查到内嵌webdriver的版本
            * 方法一:通过appium日志来查看内嵌chrome版本
            * 方法二： 
                1. adb shell pm list package | grep webview 获取webview包名
                2. adb shell pm dump com.android.webview |grep version 获取该包版本信息
*  获取当前页面包名 adb shell dumpsys window|grep mCurrent

### 微信小程序测试
* 微信小程序 基于Webview 

| 运行环境 | 逻辑层 | 渲染层 |
|     ----      |    ----   |    ----   |
|     iOS      | JavaScriptCore|WKWebview|
| 安卓| V8|chromium定制内核|
| 小程序开发者工具| NWJS| Chrome WebView|                              

* 微信官方文档的测试案例不满足测试要求
    * 设置Chromedriver正确版本
    * 设置 chrome option 传递给chromedriver
    * 使用 adb proxy 解决fix chromedriver 的bug
* 为什么有些手机无法自动化微信小程序
    * 低版本的chromedriver在高版本手机上有bug    
    * chromedriver 与微信定制的chrome内核实现上有问题
    * 解决方案： fix
        * chromedriver 没有使用adb命令，而是使用了adb协议
        * 参考课程中提到的adb proxy 源代码
        * adb proxy
            * mitmdump -p 5038 --rawtcp --mode reverse:http://localhost:5037/  -s adb_proxy.py
        * 解决方案参考：https://ceshiren.com/t/topic/3994
        * 基本 capability 设置
            * DesiredCapabilities desiredCapabilities = new DesiredCapabilities();
            * desiredCapabilities.setCapability(capabilityName:"platformName", value:"android")
            * desiredCapabilities.setCapability(capabilityName:"deviceName", value:"测试人社区 ceshiren.com")
            * desiredCapabilities.setCapability(capabilityName:"appPackage", value:"com.tencent.mm")
            * desiredCapabilities.setCapability(capabilityName:"appActivity", value:"com.tencent.mm.ui.LauncherUI")
            * desiredCapabilities.setCapability(capabilityName:"unicodeKeyboard", value:"true")
            * // 高危操作，如果设置错误，聊天记录会被清空，建议使用小号测试
            * desiredCapabilities.setCapability(capabilityName:"noReset", value:"true")
        * 第一步：设置正确的chromedriver 78.0.390,可以放置在appium自己路径下，也可以desiredCapabilities.setCapability(capabilityName:"chromedriverExecutable", value:"xxx/chromedriver_78.0.39")
        * 第二步：设置    chromeoption 传递给chromedriver，因为小程序重新开了进程
        ```

        ChromeOptions chromeOptions = new ChromeOptions()

        chromeOptions.setExperimentalOption(name:"androidProcess", value:"com.tencent.mm:appbrand0")

        desiredCapabilities.setCapability("goog:chromeOptions",chromeOptions)

        ```
        * 第三步 设置 adb proxy 通过自己的adb代理修复chromedriver的bug，并解决@xweb_devtools_remote 的问题
            * desireCapabilities.setCapability(capabilityName:"adbPort",value:"5038")  

### capability高级用法
* newCommandTimeout 超时时间
* udid 多设备支持 指定设备名称
* autoGrandPermissions APP 打开时，自动授权(机器控制权限)，只有在noRset 不为ture才有效
* dontStopAppOnReset 启动时不结束app再启动

### Webview技术原理
* 域套接字 概念
    * 进程与进程之间通讯的一种方式
    * 客户端与服务端建立连接，需要有共同的套接字，和相应的服务端的端口号
    * 套接字会处于监控状态，来监听客户端发来的请求
* 获取所有Webview的进程
    * adb shell cat /proc/net/unix |grep webview
* 查看进程的应用
    * adb shell ps |grep 1136
            
### Maxim
* 项目地址：https://github.com/zhangzhao4444/Maxim
    * 把framework包推到手机上 adb push framework.jar /手机文件夹  
    * adb push monkey.jar /手机文件夹  
* 用法
    * adb shell CLASSPATH=/手机文件夹/monkey.jar:/sdcard/framework.jar exec app_process /system/bin tv.panda.test.monkey.Monkey -p com.panda.videoliveplatform --uiautomatormix --running-minutes 60 -v -v
    
### AppCrawler
* 地址：https://github.com/seveniruby/AppCrawler
* 运行 java -jar appcrawler.jar 
* 快速运行
    * appcrawler --capability
    * "appPackage=com.xueqiu.android,appActivity=.view.WelcomeActivityAlias"
* 生成样板配置示例
    * java -jar appcrawler.jar --demo
    * 会在当前目录下生成一个demo.yml
* 常用事件
    * 参数模式
    * java -jar <appcrawler.jar路径| --demo
    * appcrawler --capability "appPackage=com.xueqiu.android,appActivity=.view.WelcomeActivityAlias"
* 配置文件（推荐方式）
    * java -jar <appcrawler.jar路径| -c example.yml --capability 'appPackage=com.xueqiu.android,appActivity=.view.WelcomeActivityAlias' -o /tmp/xueqiu/1>
* 执行参数与配置文件
    * capability 设置与appium相同
    * testcase 用于启动app后的基础测试用例
    * selectedList 遍历范围设定
    * triggerActions: 特定条件触发执行动作的设置
    * 执行参数比配置文件优先级高
* capability配置示例                            
 



    

                    


            
                            
             



        

                

                             
            
