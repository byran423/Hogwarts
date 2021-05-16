- pip依赖管理与虚拟环境
    - 虚拟环境
        * 创建虚拟环境
         * python -m venv tutorial-env(虚拟环境名称)
        * 激活虚拟环境
          * Mac -- source  tutorial-env/bin/activate
          * window --  tutorial-env\Scripts\activate.bat
        * 退出虚拟环境
         * deactive
- pytest插件开发
    - 打包发布笔记
        * 必须要有代码包和setup.py文件
            * setup.py是一个构件工具 
        * setup
        
        ```
        from setuptools import setup    
        setup(        
            name = 'pytest_encode',        
            url = 'https://github.com/xxx/pytest-encode',        
            version = '1.0',        
            author = 'yangbai',
            author_email = '547556017@qq.com',
            description='set your encoding and logger'
            long_description='Show Chinese for your mark.parametrize(). Define logger varibale ....'
            classifiers=[# 分类索引，pip对所属宝的分类
                ‘Framework :: Pytest',
                'Programming Language :: Python'
                'Topic :: Software Development :: Testing',
                'Programming Language :: Python :: 3.8'
            ],
            license = 'proprietary',
            packages = ['pytest_encode'],
            keywords = [
                'pytest', 'py.test', 'pytest_encode'
            ],
        # 需要安装的依赖
        install_requires=['pytest'],
        # 入口模块 或者入口函数
        entry_points={
            'pytest11':[
                'pytest-encode = pytest_encode'
                ]
            },
            zip_safe=False
        )
        ```
        * 打包需要两个工具 wheel, setuptools
        * 打包命令 python setup.py sdist bdist_wheel
            * 通过打包命令打出了一个源码包，一个是whl通过pip install 进行安装
        * pip freeze >requirement.txt 导出当前环境的所有包名
        * 将打出来的包发出到pypi上
            * 在pypi上注册一个账户
            * 使用Twine来上传发行包
             * 安装 --python -m pip install  twine
             * 上传包 -- python -m twine upload --repository testpypi dist/*

    - 添加命令行参数笔记
        * pytest_addoption (parser,pluginmanager)  hook函数
        ```
        #添加一个命令行参数
        def pytest_addoption(parser):
            mygroup = parser.getgroup('hogwarts') # group 将下面所有的option都展示在这个group下
            mygroup.addoption("env",   # 注册一个命令行选项
                default='test',   # 参数的默认值
                dest= 'env',   #   存储的变量
                help='set your run env'   # 帮助提示，参数的描述信息
        )
        @pytest.fixture(scope='session')
        def cmdoption(request):
            env = reqeust.config.getoption("--env",default='test')
            if env == 'test':
                print("test环境")
            elif env == 'dev':
                print("dev 环境")
            with open(datapath) as f:
                datas = yaml.safe._load(f)
            return env,datas
        ```
        * 只执行指定函数   pytest --env dev test_mm.py::test_env -vs
        ```
        def test_env(cmdoption):
            evn,datas = cmdoption
            host = datas['env]['host']
            port = datas['env']['port']
            url = str(host)+str(port)
            print(url)
        ```
    - hook函数
        * 最简单方式定义一个hook函数，放在conftest.py
        ```
        def pytest_collection_modifyitems(session,config,items:List):
            for item in items:
                item.name = item.name.encode('utf-8').decode('unicode-escape')
                item._nodeid = item.nodeid.endoce('utf-8').decode('unicode-escape')
                items.reverse()
                if 'login' in item.nodeid:
                    item.add_marker(pytest.mark.login)
        ```
        * 执行时想只执行login有关的用例
         * pytest -m login
    - pytest插件
        * 外部插件 -- pip install 安装的插件
        * 本地插件 -- pytest自动模块发现机制（conftest.py存放的）
        * 内置插件  --代码内部的_pytest目录加载
        * hook函数 -- External Libraries 里的hookspec.py 文件里
        
- pytest框架结构
    - 框架结构
        * 模块级 setup_module/teardown_module 模块始末，全局的（优先级最高）
        * 函数级 setup_function/teardown_function 只对函数用例生效（不在类中）
        * **类级（setup_class/teardown_class）**只在类中前后运行一次（在类中）
        * 方法级（setup_method/teardown_method）开始于方法始末（在类中）
        * 类里面的（setup/teardown）运行在调用方法的前后
    - pytest
        * 测试文件识别 -- test_*.py 或者*_test.py
        * 命令行 pytest -vs 执行测试用例，查看执行过程中的详细信息和打印信息
        * pytest 文件名.py::类名::方法名 执行某个方法
        
- unittest测试框架
    - unittest
        * python自带的单元测试框架
        * test case ,test suites ,test fixtures, test runner
        * 编写规范
         * 首先import unittest
         * 测试类继承unittest.Testcase
         * 测试方法以 test_开头
        * setUpClass 和tearDownClass 在整个测试类前后分别调用的方法需要@classmethod装饰器
        * setUp和tearDown 在每个测试用例前后分别调用的方法
        * TestSuite
         * 创建 -- suite= unittest.TestSuite()
         * 添加 suite.addTest()
         * unittest.TextTestRunner().run(suite)
        * 执行某个测试类
        ```suite1 = unittest.TestLoader().loadTestFromTestCase(TestCase1)
        suite = unitest.TestSuite([suite1])
        suite.TextTestRunner(verbosity=2).run(suite)
        ```
        * 执行某个目录下的所有测试用例
        * test_dir = './test_case'
        * discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
            * discover 可以一次调用多个脚本
            * test_dir被测试脚本路径
            * pattern 脚本名称匹配规则
                    
- 测试报告定制
    - allure
        - 前端自动化截图
            * @allure.attach 显示许多不同类型的提供的附件，可以补充测试、步骤或测试结果
            * 步骤
                * 在测试报告里附加网页：
                 * allure.attach(body(内容),name,attachment_type,extension)
                 * allure.attach('<head></head><body>首页</body>','这是错误页的结果信息',allure.attachment_type.HTML)
                * 在测试报告里附加图片：
                    * allure.attah.file(source,name,attachment_type,extension):
                    * allure.attach.file("./result/b.png",attachment_type=allure.attachment_type.PNG)
                ```
                @allure.testcase("http://测试用例管理地址")
                @allure.feature("百度搜索")
                @pytest.mark.parametrize('test_data1','['allure','pytset','unittest']')
                def test_step_demo(test_data1):
                with allure.step("打开百度网页")：
                    driver = webdriver.Chrome("/webdriver路径")
                    driver.get("http://www.baidu.com")
                with allure.step(f"输入搜索词：{test_data1}")
                    driver.find_element_by_id("kw").send_keys(test_data1)
                    time.sleep(2)
                    driver.find_element_by_id("su").click()
                    time.sleep(2)
                with allure.step("保存图片")：
                     driver.save_screenshot("./result/b.png")
                     allure.attach.file("./result/b.png",attachment_type = allure.attachment_type.PNG)
                with allure.step("关闭浏览器")：
                    driver.quit()
                ```
        - 特性
            * 功能上加@allure.feature('功能名称')
            * 子功能上加@allure.stroy（‘子功能名称'）
            * 步骤上加@allure.step('步骤细节')
            * @allure.attach('具体文本信息')，需要附加的信息，可以是文本，数据，图片，视频，网页
            * 如果只测试登录功能运行的时候可以加限制过滤
                * pytest文件名--allure-features‘购物车功能’ -- allure-stroies‘加入购物车’（注意这里--allure_features中间是下划线）
            * feature相当于一个功能，一个大的模块，将case分类到某个feature中，报告中behaviore中显示，相当于testsuite
            * stroy相当于对应这个功能或者模块下的不同场景，分支功能，属于feature之下的结构，报告在features中显示，相当于testcase
            * feature与story类似于父子关系
            * step可以放在关键步骤中，在报告中显示
                * 在app,web自动测试当中，建议每切到一个新的页面当做一个step
                    * @allure.step只能以装饰器的形式放在类或者方法上面
                    * with allure.step()可以放在测试用例方法里面，但测试步骤的代码需要被该语句包含
            * issue，testcase 关联测试用例（可以直接给测试用例的地址链接）
                * @allure.link("链接地址",name='链接名称')
            * 关联bug
                * 执行的时候需要加个参数
                    * --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
            * 按重要级别分类
                * 通过附加pytest.mark标记
                * 通过allure.feature,allure.story
                * 通过allure.severity来附加标记
                    * 级别Trivial,Minor，Normal，Critical，Blocker、
                * 步骤
                    * 在方法，函数和类上面加  
                        * @allure.severity(allure.severity_levle.TRIVIAL)
                    * 执行时：
                        * pytest -s -v 文件名 --allure-severity normal critical         
        - allure
            * 安装 brew install allure
            * 升级homebrew 更改
            ```
            vim ~/.zshrc
            export HOMEBREW_NO_AUTO_UPDATE=true
            # 刷新环境变量
            source ~/.zshrc
            ```
            * 安装 pip install allure-pytest
                * 方式一：
                    * pytest --alluredir=/tmp/my_allure_results
                    * allure serve /tmp/my_allure_results
                * 方式二：
                    * allure generate ./result/ -o ./report/ --clean
                    * allure open -h 127.0.0.1 -p 8883 ./report/ 
                                             
- 单元测试覆盖
    - 路径覆盖
    - 条件覆盖
    - 判断覆盖
    - 语句覆盖
   
- 数据驱动
    - 数据驱动
        * 数据驱动就是数据的改变从而驱动自动化测试的执行，最终引起测试结果的改变。简单来说，就是参数化的应用，数据量小的测试用例可以使用代码的参数化来实现数据驱动，数据量大的情况下建议使用一种结构化的文件（yaml，json）来对数据进行存储，然后在测试用例中读取这些数据
        ```
        class TestDemo:
            @pytest.mark.parametrize("env",yaml.safe_load(open("./env.yml")))
            def test_demo(self, env):
                if "test" in env:
                    print(env)
        ```
      
     