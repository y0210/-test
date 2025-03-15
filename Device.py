import time
import uiautomator2 as u2

class Device:
    timeout = 3

    def __init__(self, device):
        self.d = device

    def swipe_up(self):
        x = self.get_screen_width()
        y = self.get_screen_height()
        x1 = x // 2
        y1 = y * 0.3
        y2 = y * 0.8
        self.d.swipe(x1, y1, x1, y2)

    def swipe_down(self):
        x = self.get_screen_width()
        y = self.get_screen_height()
        x1 = x // 2
        y1 = y * 0.3
        y2 = y * 0.8
        self.d.swipe(x1, y2, x1, y1)

    def swipe_left(self):
        x = self.get_screen_width()
        y = self.get_screen_height()
        y1 = y // 2
        x1 = x * 0.3
        x2 = x * 0.8
        self.d.swipe(x1, y1, x2, y1)

    def swipe_right(self):
        x = self.get_screen_width()
        y = self.get_screen_height()
        y1 = y // 2
        x1 = x * 0.3
        x2 = x * 0.8
        self.d.swipe(x2, y1, x1, y1)

    def get_screen_height(self):
        """
        获取屏幕的高度
        :return:
        """
        height = self.d.device_info["display"]["height"]
        return height

    def get_screen_width(self):
        """
        获取屏幕的宽度
        :return:
        """
        width = self.d.device_info["display"]["width"]
        return width

    def judge_element_exist(self,element):
        """
        校验元素是否存在
        :return:
        """
        if self.d(text=element).wait(Device.timeout):
            print('==已找到%s元素，继续执行==' % element)
            return True
        else:
            print('==未找到%s元素，结束执行==' % element)
            return False

    def swipe_top(self):
        """
        滑动到顶部
        """
        while True:
            page_connect = self.d.dump_hierarchy()[:(len(self.d.dump_hierarchy())) // 2]
            self.swipe_up()
            time.sleep(2)
            new_page_connect = self.d.dump_hierarchy()[:(len(self.d.dump_hierarchy())) // 2]
            if page_connect == new_page_connect:
                print("==已滑到顶部==")
                break

    def swipe_bottom(self):
        """
        滑动到底部
        """
        while True:
            page_connect = self.d.dump_hierarchy()[(len(self.d.dump_hierarchy())) // 2:]
            self.swipe_down()
            time.sleep(2)
            new_page_connect = self.d.dump_hierarchy()[(len(self.d.dump_hierarchy())) // 2:]
            if page_connect == new_page_connect:
                print("==已滑到底部==")
                break

    def press_power(self):
        """
        点击电源键
        :return: None
        """
        # Check ANR
        self.d.press("power")

    def press_back(self):
        """
            点击返回键
        :return: None
        """
        # Check ANR
        self.d.press("back")
        return True

    def press_recent(self):
        """
            点击enter键
        :return: None
        """
        self.d.press("recent")

    def press_home(self):
        """
            点击home键
        :return: None
        """
        # Check ANR
        self.d.press("home")

    def press_enter(self):
        """
            点击enter键
        :return: None
        """
        self.d.press("enter")

    def clear_task_all(self):
        self.judge_home()
        while True:
            self.press_recent()
            time.sleep(2)
            if self.d(resourceId="com.android.launcher3:id/snapshot").exists():
                print("==多任务界面==")
                break
        while True:
            self.swipe_left()
            time.sleep(1)
            if self.d(text="全部清除").exists():
                print("==已找到“全部清除”==")
                break
        while True:
            self.d(text="全部清除").click()
            time.sleep(1)
            if self.d(resourceId="com.android.quicksearchbox:id/search_widget_text"):
                print("==已全部清除==")
                break

    def swipe_clear_task(self):
        x = self.get_screen_width()
        y = self.get_screen_height()
        x1 = x // 2
        y1 = y * 0.1
        y2 = y * 0.6
        self.d.swipe(x1, y2, x1, y1)

    def judge_home(self):
        while True:
            self.press_home()
            time.sleep(1)
            if self.d(resourceId="com.android.quicksearchbox:id/search_widget_text"):
                print("==已回到主屏幕==")
                break


if __name__ == "__main__":
    device = u2.connect("0123456789ABCDEF")
    # device(text="图库").click()
    # if public.judge_element_exist(device,element="相册"):
    #     device(description="切换到相机").click()
    # else:
    #     print()
    Device(device).press_enter()