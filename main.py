import pyautogui
import tkinter as tk
import typing as t


class UserData:
    """用户数据"""
    user_name: t.Optional[str] = None
    user_type: t.Optional[t.Literal[0, 1, 2]] = None
    user_identity: t.Optional[int] = None
    user_info: str = ''


class WindowConfigParams:
    """窗口配置项参数"""
    root_width: int = pyautogui.size().width
    root_height: int = pyautogui.size().height
    background_color: str = '#000000'
    title_color: str = 'black'
    title_background_color: str = '#fdfafa'
    title_bar_height: int = 40


class MainWindow(WindowConfigParams):
    """主窗口"""

    def __init__(self):
        self.root: tk.Tk = tk.Tk()
        self.mode_val: tk.StringVar = tk.StringVar()
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
                                 font=('bold', 14), fg=self.title_color,
                                 command=self.root.destroy)
        # 初始化按钮
        reset_button = tk.Button(title_bar, text='初始化', bg=self.title_background_color,
                                 font=('bold', 14), fg=self.title_color,
                                 command=self.reset_info)

        self.mode_val.set('会议模式')
        # 模式按钮
        mode_button = tk.Button(title_bar, textvariable=self.mode_val, bg=self.title_background_color,
                                font=('bold', 14), fg=self.title_color,
                                command=self.change_mode)

        title_bar.place(x=0, y=0, width=self.root_width, height=self.title_bar_height)
        close_button.pack(side='left')
        reset_button.pack(side='left')
        mode_button.pack(side='left')
        tk.Text(self.root, bg=self.background_color).place(x=0, y=self.title_bar_height, width=self.root_width,
                                                           height=self.root_height - self.title_bar_height)

        # 弹窗测试
        self.a = UserData()
        p1 = PopWin(self.a)
        info_button = tk.Button(self.root, text='发言内容', bg=self.title_background_color, activebackground='white',
                                font=('bold', 14), fg='black', command=p1.pop_win_command)
        info_button.place(x=100, y=200)

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


class PopWin:
    """弹窗"""

    def __init__(self, cuurent_user: UserData):
        """

        :param cuurent_user: 弹窗所属用户
        """
        self.current_user: UserData = cuurent_user
        self.pop_flag: bool = False
        self.pop_win: t.Optional[tk.Toplevel] = None
        self.text_input: t.Optional[tk.Text] = None

    def pop_win_command(self):
        """弹出窗口"""
        if not self.pop_flag:
            self.pop_flag = True
            self.pop_win = tk.Toplevel()
            self.text_input = tk.Text(self.pop_win)
            self.pop_win.title('发言信息')
            self.pop_win.attributes('-toolwindow', True)
            self.pop_win.geometry('300x200+200+200')
            self.text_input.pack(fill='both', expand=True)
            self.text_input.focus_set()
            self.text_input.insert(tk.END, self.current_user.user_info)

            self.pop_win.bind('<Escape>', self.close_win)
            self.pop_win.protocol('WM_DELETE_WINDOW', self.close_win)
        else:
            self.close_win()

    def close_win(self, ev=None):
        """关闭窗口"""
        self.pop_flag = False
        self.current_user.user_info = '\n'.join(self.text_input.get('0.0', tk.END).split('\n')[:-1])
        self.pop_win.destroy()


main_loop = MainWindow()
main_loop.root.mainloop()
