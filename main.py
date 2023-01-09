import ctypes
import tkinter as tk


class WindowConfigParams:
    """窗口配置项参数"""
    root_width = ctypes.windll.user32.GetSystemMetrics(0)
    root_height = ctypes.windll.user32.GetSystemMetrics(1)
    background_color = '#000000'
    title_color = 'black'
    title_background_color = '#fdfafa'
    title_bar_height = 30


class MainWindow(WindowConfigParams):
    def __init__(self):
        self.root = tk.Tk()
        self.mode_val = tk.StringVar()
        self.init_window()

    def init_window(self):
        """窗口初始化"""
        # 设置窗口大小
        self.root.geometry(f'{self.root_width}x{self.root_height}')
        # 删除标题栏
        self.root.overrideredirect(True)
        # 设置透明色
        self.root.attributes('-transparentcolor', self.background_color)
        # 窗口置顶
        self.root.attributes('-topmost', 1)

        # 标题栏
        title_bar = tk.Frame(self.root, bg=self.background_color,
                             highlightcolor=self.background_color)
        # 关闭按钮
        close_button = tk.Button(title_bar, text='关闭', bg=self.title_background_color,
                                 font="bold", fg=self.title_color,
                                 command=self.root.destroy)
        # 初始化按钮
        reset_button = tk.Button(title_bar, text='初始化', bg=self.title_background_color,
                                 font="bold", fg=self.title_color,
                                 command=self.reset_info)

        self.mode_val.set('会议模式')
        # 模式按钮
        mode_button = tk.Button(title_bar, textvariable=self.mode_val, bg=self.title_background_color,
                                font="bold", fg=self.title_color,
                                command=self.change_mode)

        title_bar.place(x=0, y=0, width=self.root_width, height=self.title_bar_height)
        close_button.pack(side='left')
        reset_button.pack(side='left')
        mode_button.pack(side='left')
        tk.Text(self.root, bg=self.background_color).place(x=0, y=30, width=self.root_width,
                                                           height=self.root_height - self.title_bar_height)

    def reset_info(self):
        """初始化数据"""
        self.mode_val.set('会议模式')

    def change_mode(self):
        """切换模式"""
        mode_val = self.mode_val.get()
        if mode_val == '会议模式':
            self.mode_val.set('游戏模式')
        else:
            self.mode_val.set('会议模式')


main_loop = MainWindow()
main_loop.root.mainloop()
