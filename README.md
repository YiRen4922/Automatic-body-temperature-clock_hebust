# Automatic-body-temperature-clock_hebust
## hebust, 河北科技大学每日自动体温打卡, web自动化, python, selenium, tesseract
- 使用selenium实现自动点击填写等操作
- 使用PIL.Image截取验证码图片
- 使用tesseract识别验证码，成功率一般，但能用
- 使用csv文件读写数据，能够存储数据批量运行
---
使用方法：
在daka_data.csv中按照"学号，密码，QQ"填入信息
然后，运行main.py即可（体温默认为36.5）
## 仅包含自动打卡，定时请自行设置
