# 南苑聚合
南苑聚合的后端

## 项目使用说明
### 配置 env
请在根目录创建 .env 文件

```
# 数据库链接
# 例如: mysql+pymysql://root:123456@localhost:3306/nfu
DATABASE_URL=xxxxxxx

# 各种jwt的签名(随机的字符串即可)
ACCESS_TOKEN=xxxxxxx
REFRESH_TOKEN=xxxxxxx
EMAIL_TOKEN=xxxxxxx
REFRESH_EMAIL_TOKEN=xxxxxxx

# 邮箱信息
MAIL_SERVER=smtp.exmail.qq.com
MAIL_USERNAME=xxxxxxx
MAIL_PASSWORD=xxxxxxx

# host
API_URL=http://127.0.0.1:5000
```

### pipenv
本项目采用 pipenv 管理 第三方库

没有装过 pipenv，请在项目根目录执行

```
➜ pip3 install pipenv
➜ pipenv install
```

开始运行程序

```
➜ cd nfu 
➜ pipenv run flask run
```

## 计划完成模块
### 电费模块
- [x] 电费查询
- [x] 电费充值
- [x] 电费充值记录
- [x] 微信支付接口
- [x] 分析近15天电费

### 车票模块
- [x] 抢票系统
- [x] 支付宝支付接口

### 课表模块
- [x] 查询课表

### 成绩模块
- [x] 查询成绩
- [x] 查看已选总学分
- [x] 查看已修总学分
- [x] 查看已平均绩点
- [x] 查看已平均成绩

### 学分模块
+ 按照培养计划，对已修学分分类
- [ ] 公共必修课
- [ ] 公共选修课
- [ ] 专业核心课
- [ ] 专业方向课
- [ ] 专业选修课
- [ ] 成长必修课

## API URI
### OAuth2 接口
注册接口 `oauth/sign_up`

登陆接口，获取令牌 `oauth/token/get`

刷新令牌 `oauth/token/refresh`

### 验证接口
验证邮箱合法性 `validate/email/token`

### 电费接口
获取宿舍电费 `electric/get`

分析近15天电费 `electric/analyse`

电费充值记录 `electric/order/log`

创建电费充值订单 `electric/order/create`

跳转支付页面 `electric/order/pay`

### 校巴接口
获取班车时刻表 `school_bus/schedule/get`

获取乘车人数据 `school_bus/passenger/get`

获取电子车票 `school_bus/ticket/get`

获取车票的id，用于退票 `school_bus/ticket_id/get`

退票 `school_bus/ticket/delete`

### 课程表接口
获取课程表 `class_schedule/get`

更新课程表 `class_schedule/update`

### 成绩接口
获取成绩单 `achievement/get`

更新成绩单 `achievement/update`

查看总成绩信息 `achievement/total/get`

更新总成绩信息 `achievement/total/update`