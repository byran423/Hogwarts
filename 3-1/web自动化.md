- 等待
    * 隐式等待
        * self.driver.implicitly_wait(3)
    * 显示等待
        * WebDriverWait  配合until()和until_not()方法
            * 方法一：
                ```
                def wait(x):

                    return len(self.driver.find_elements(By.XPATH,'//*[@class="views sortable num"]')) >= 1

                expected_conditions.element_to_be_clickable()  
                ```
            * 方法二：
            ```
           WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@class="views sortable num"]')))
            ```
          
- 控件
    * Xpath
        * 语法 
        ```
            * /bookstore/book[1] 选取属于bookstore子元素的第一个book元素 
            * /bookstore/book[last()] 选取属于bookstore子元素的最后一个book元素
            * /bookstore/book[last()-1] 选取属于bookstore子元素的倒数第二个book元素
            * //title[@lang='eng'] 选取所有title元素，且其中的price元素的值须大于35.00
            * /bookstore/book[price>35.00] 选取bookstore元素的所有book元素，且其中的price元素的值须大于35.00
            * /bookstore/book[price>35.00]/title 选取bookstore元素的所有book元素的所有title元素，且其中的price元素的值须大于35.00
            * nodename 选取此节点的所有子节点
            * / 从根节点选取
            * // 从匹配选择的当前节点选择文档中的节点，而不考虑塔门的位置
            * . 选取当前节点
            * .. 选取当前节点的父节点
            * @选取属性
        ```       
 
        * 例子：百度搜索
        ```
           * Chrome里 Console里 $x('')代表使用xpath定位

           * $x('//*[@id="s_tab"]//b')

           * $x('//*[@id="s_tab"]//a[1]')
        ```
    * CSS
        * 语法    
        ```
        > .intro 选择class=“intro”的所有元素
        >  #firstname 选择id=“firstname”的所有元素
        >     *选择所有元素
        >  div,p 选择所有<div>元素和所有<p>元素
        >  div p 选择<div>元素内部所有的<p>元素
        >  div>p 选择父元素为<div>元素的所有<p>元素
        >  div+p 选择紧接在<div>元素之后的所有<p>元素
        > [target] 选择带有target属性所有元素
        > [target=_blank] 选择target="_blank"的所有元素
        > p:nth-child(2) 选择属于其父元素的第二个子元素的每个<p>元素
        > p~ul 选择前面有<p>元素的每个<ul>元素
        ```       
        * 实战：百度搜索
        ```
        > $('#kw')
        > $('$s_tab a:nth-child(2)')
        > $('$s_tab a:nth-last-child(1)')  
        ```  
- 控件进阶
    * ActionChains ： 执行PC端的鼠标点击，双击，右键，拖拽等事件
        * 调用ActionChains 的方法时不会立即执行，将所有的操作按顺序存放在一个队列里，当你调用perform()方法时，队列中的时间会依次执行
        * 基本用法
        >* 生成一个动作action = ActionChains(driver)      
        >* 动作添加方法1 action.方法1          
        >* 动作添加方法2 action.方法2
        >* 调用perform() 方法执行 （action.perform()）
        * 具体写法：
        >* 链式写法：ActionChains(driver).move_to_element(element).click(element).perform()    
        * 分步写法：
        >* actions = ActionChains(driver)  
        >* action.move_to_element(element)     
        >* action.click(element) 
        >* action.perform() 
        * 用法1：点击、右键、双击   
        >* action = ActionChains(driver)
        >* action.click(element)
        >* action.double_click(element) 
        >* action.context_click(element)  
        >* action.perform()   
        
        * 测试案例一：
            * 打开页面：http://sahitest.com/demo/clicks.htm进行点击，右键，双击
         
        * 用法二：鼠标移动到某个元素上
            * action= ActionChains(self.driver)
            * action.move_to_element(element)
            * action.perform()       
        * 用法三： ActionChains模拟按键方法
            * action = ActionChains(driver)
            * action.send_keys(Keys.BACK_SPACE)
            * 或者action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
            * action.perform()
    
    * TouchActions : 模拟PC和移动端的点击，滑动，拖拽，多点触控等多种手势操作
        * 手势控制
            * tap -- 在指定元素上敲击
            * double tap -- 在指定元素上双敲击
            * tap_and_hold --在指定元素上点击但不释放
            * move -- 手势移动指定偏移（未释放）
            * release -- 释放手势
            * scroll -- 点击手势并滚动
            * scroll_from_element -- 从某个元素位置开始手势点击并滚动(向下滚动为负数，向上滚动为正数)
            * long_press --长按元素
            * flick -- 手势滑动
            * flick_element -- 从某个元素位置开始手势滑动（向下未正数，向上未负数)
            * perform 执行           
        * 表单操作



- frame和多窗口
    * 多窗口处理流程
        1、先获取到当前的窗口句柄(driver.current_window_handle)
        2、再获取到所有的窗口句柄(driver.window_handles)
        3、判断是否是想要操作的窗口，如果是，就可以对窗口进行操作，如果不是，跳转到另外一个窗口，对另一个窗口进行操作(driver.switch_to_window)
    * frame 处理    
        * frame：
            *frame 是html中的框架
            * 基于HTML的框架，又分为垂直框架和水平框架
        * frame分类
            * 包括frameset、frame、iframe三种
            * frameset和普通的标签一样，不影响正常的定位
            * frame与iframe对selenium定位而言是一样的                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        * 多frame切换
            * frame存在两种，一种是嵌套的，一种是未嵌套的
            * driver.switch_to.frame() --根据元素id或者index切换frame
            * driver.switch_to.default_content() -- 切换到默认frame
            * driver.switch_parent_frame() -- 切换到父级frame
        * 处理未嵌套的iframe
            * driver.switch_to_frame(“frame的id”)
            * driver.switch_to_frame("frame-index") frame无ID的时候依据索引来处理，索引从0开始driver.switch_to_frame(0)
        * 处理嵌套的iframe
            * 对于嵌套的先进入到iframe的父节点，再进到子节点，然后对子节点里的对象进行操作
            * driver.switch_to.frame("父节点")
            * driver.switch_to.frame("子节点")

- 执行JS脚本 
    * selenium 执行js代码
        * execute_script: 执行js
        * return: 可以返回js的返回结果
        * execute_script: arguments传参
        * 案例
        ```
      class TestJs(Base):
           def test_js_scroll(self):
              self.driver.get('https://www.baidu.com/')
              self.driver.find_element_by_id('kw').send_keys("selenium 测试")
              element = self.driver.execute_script("return document.getElementById('su')")
              element.click()
              sleep(3)
              self.driver.execute_script("document.documentElement.scrollTop=10000")
              self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
              sleep(3)
              print(self.driver.execute_script('return document.title;return JSON.stringify(performance.timing)'))
         ```

    * 对时间进行操作的思路：
        1、取消日期的的readonly属性
        2、给value赋值
        3、写js代码来实现如上的1，2点，再webdirver对js进行处理
    * 案例：
    ```
  def test_datetime(self):
       self.driver.get('https://www.12306.cn/index/')
       self.driver.execute_script("a=document.getElementById(id='train_date');a.removeAttribute('readonly');a.value='2020-12-12'")
       sleep(3)
    ```
    
- 文件上传、弹框
    * 情况一：input标签可以直接shiyong send_keys(文件地址）上传文件
        * 用法：
            * el=driver.find_element_by_id('上传按钮')
            * el.send_keys("文件路径+文件名")
    * 弹框处理
        * switch_to.alert() 方法，然后使用text/accept/dismiss/send_keys等方法进行操作
        * 操作alert常用的方法： 
            * switch_to.alert():获取当前页面上的警告框
            * text: 返回 alert/confirm/prompt 中的文字信息
            * accept():  接受现有警告框
            * dismiss(): 解散现有警告框
            * send_keys(keysToSend)：发送文本至警告框。keysToSend: 将文本发送至警告框

- pageObject
    * 历史
        * 2013 Martin Flower  https://martinfowler.com/bliki/PageObject.html
        * 2015 Selenium https://github.com/SeleniumHQ/selenium/wiki/PageObjects
        * 2020 https://www.selenium.dev/documentation/en/guidelines_and_recommendations/page_object_models/
    * PageObject 六大原则
        * The public methods represent the services that the page offers(一个方法代替页面服务)
        * Try not to expose the internals of the page(不要暴露细节)
        * Generally don't make assertions -- 不要断言
        * Methods return other PageObjects 方法返回其它PageObjects
        * Need not represent an entire page  --只为页面中重要的元素创建page类
        *  Different result for the same action are modelled as different methods    
                                                                                                                                                                                                                                                                                                                                                                                                                                                            
- 复用已有浏览器
    * 复用浏览器：
        1、需要退出当前所有的Chrome
        2、找到Chrome的启动路径
        3、配置 环境变量（windows 把chrome路径加入环境变量）
        4、 启动命令 win:Google\ Chrome --remote-debugging-port=9222 |mac:/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
        5、 访问http://localhost:9222 查看服务师傅启用
        6、 代码里增加
        ```
      chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address='127.0.0.1:9222'
        self.driver=webdriver.Chrome(options=chrome_arg)
        ```
    * 使用cookie
    ```
     driver.get(url)
     driver.delete_all_cookies()
     for cookie in cookies:
         driver.add_cookie(cookie)
     driver.refresh()
    ```                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    * 把cookie数据放到shelve中
        * python 内置模块，相当于一个小型的数据库
        * 生成cookies 数据     
        ```
      db = shelve.open('./mydbs/cookies')
        db['cookie'] = cookies
        db.close()
        ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    * 使用shelve
    ```
  db = shelve.open('./mydbs/cookies')
    # 取出cookies
    cookies = db['cookies']
    # 打开页面
    self.driver.get('')
    # 塞入cookie
    for cookie in cookies:
        self.driver.add_cookie(cookie)
    ```    
  
  
  
                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            