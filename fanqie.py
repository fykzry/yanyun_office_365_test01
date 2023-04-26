# 导入 time 模块
import time

# 定义工作时间和休息时间
WORK_TIME = 25 * 60
REST_TIME = 5 * 60

# 定义计时器函数
def timer(countdown_time):
    """倒计时函数"""
    # 计算倒计时的结束时间
    end_time = time.time() + countdown_time
    # 循环直到倒计时结束
    while time.time() < end_time:
        # 计算剩余时间
        remaining_time = int(end_time - time.time())
        # 输出剩余时间
        print(f"{remaining_time // 60} 分钟剩余时间。")
        # 等待一秒钟
        time.sleep(1)

# 循环计时器
while True:
    # 开始工作时间
    print("Start focus time!")
    # 执行计时器函数
    timer(WORK_TIME)
    # 工作时间结束，开始休息时间
    print("时间到！休息一下。")
    # 执行计时器函数
    timer(REST_TIME)
    # 休息时间结束，返回工作时间
    print("休息时间结束，开始工作吧！")
