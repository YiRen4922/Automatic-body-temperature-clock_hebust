# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv
from PIL import Image
import pytesseract




class Daka():
    def __init__(self, user, qq, pwd):
        self.user = user
        self.qq = qq
        self.pwd = pwd

    def binarization(image):
        # 转成灰度图
        imgry = image.convert('L')
        # 二值化，阈值可以根据情况修改
        threshold = 138
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        out = imgry.point(table, '1')
        return out
    def write_in(self):
        headers= ["user", "pwd", "qq"]
        datas = {
            "user": self.user,
            "pwd": self.pwd,
            "qq": self.qq
        }
        with open("daka_data.csv", "a", newline='') as f:
            writer = csv.DictWriter(f, headers)
            # writer.writeheader()
            writer.writerow(datas)
    def read_data(self):
        with open("daka_data.csv", 'r') as f:
            reader = csv.DictReader(f)
            for line in reader:
                print(line)
    def test_eight_components(self):
        driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

        driver.get("http://xscfw.hebust.edu.cn/survey/login")

        driver.find_element(By.ID, "user" ).clear()
        driver.find_element(By.ID, "pwd").clear()
        time.sleep(1)
        driver.find_element(By.ID, "user").send_keys(self.user)
        driver.find_element(By.ID, "pwd").send_keys(self.pwd)
        time.sleep(1)
        while(True):
            driver.find_element(By.ID, "login").click()
            time.sleep(1)
            driver.save_screenshot('picture.png')
            ce = driver.find_element(By.ID, "verifyCode")
            # print(ce.location)
            left = ce.location['x'] + 50
            top = ce.location['y'] + 78
            right = left + ce.size['width'] + 10
            bottom = top + ce.size['height']
            im = Image.open('picture.png')
            data = (left, top, right, bottom)
            # print(data)
            img = im.crop(data)
            image = Daka.binarization(img)
            image.save("picture2.png")
            image = Image.open("picture2.png")
            code = pytesseract.image_to_string(image)
            print(code)
            print(len(code))
            code = str(code)
            print(code)
            print(len(code))

            driver.find_element(By.ID, "vcode").clear()
            driver.find_element(By.ID, "vcode").send_keys(code)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/a[2]').click()
            if len(code) != 6:
                driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/a[1]').click()
                continue
            try:
                # 鼠标点击事件
                time.sleep(1)
                ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, 'li[class="mdui-list-item mdui-ripple"]')).perform()
                print("登录成功")
                break
            except Exception:
                print("验证码错误\n")
                time.sleep(1)


        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "input[name='c1']").clear()
        driver.find_element(By.CSS_SELECTOR, "input[name='c4']").clear()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "input[name='c1']").send_keys("36.5")
        driver.find_element(By.CSS_SELECTOR, "input[name='c4']").send_keys("36.5")
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="main"]/div[7]/label[2]').click()
        time.sleep(1)
        driver.find_element(By.ID, "save").click()
        time.sleep(1)
        print("打卡成功")
        driver.quit()


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # my_daka.write_in()
    # my_daka.read_data(user="2107090317")
    user = "2107090317"
    pwd = "Xinxi15733292960#"
    qq = "2976784922"
    with open("daka_data.csv", 'r') as f:
        reader = csv.DictReader(f)
        for line in reader:
            print(line)
            user = line['user']
            pwd = line['pwd']
            qq = line['qq']
            my_daka = Daka(user=user, pwd=pwd, qq=qq)
            my_daka.test_eight_components()



# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
