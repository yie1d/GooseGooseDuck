import tkinter as tk
from tkinter import ttk
import typing as t

from identity_info import identity_info_dict

identity_info_dict[''] = sum(identity_info_dict.values(), [])


class UserData:
    """用户数据"""
    user_name: t.Optional[str] = None
    user_type: str = ''
    user_info: str = ''
    user_identity: t.Optional[int] = None

    # tab_choose: int = 0

    def __init__(self, main_win, box_coordinate: tuple):
        """

        :param main_win:
        :param box_coordinate:
        """
        self.box_coordinate: tuple = box_coordinate
        # 弹窗
        pop_win: PopWin = PopWin(self, (box_coordinate[0] - 65, box_coordinate[1] + 20))
        self.user_info_button: tk.Button = tk.Button(main_win.root, text='发言内容', bg=main_win.title_background_color,
                                                     activebackground='white',
                                                     font=('bold', 14), fg='black',
                                                     command=pop_win.pop_win_command)  # 下拉框测试
        self.user_type_combo = ttk.Combobox(main_win.root, values=list(identity_info_dict.keys()), width=8,
                                            font=('bold', 12), state='readonly')

        self.user_identity_combo = ttk.Combobox(main_win.root, values=identity_info_dict[''], width=8,
                                                font=('bold', 12))

    def meeting_mode(self):
        """会议模式，展示控件"""
        self.user_info_button.place(x=self.box_coordinate[0] - 150, y=self.box_coordinate[1] + 20)

        self.user_type_combo.place(x=self.box_coordinate[0] - 150, y=self.box_coordinate[1] + 70)
        self.user_type_combo.bind("<<ComboboxSelected>>", self.change_user_identity_list)

        self.user_identity_combo.place(x=self.box_coordinate[0] - 150, y=self.box_coordinate[1] + 120)
        self.user_identity_combo.bind('<KeyRelease>', self.change_tips)
        self.user_identity_combo.bind('<<ComboboxSelected>>', self.change_tips)
        self.user_identity_combo.bind('<Tab>', self.key_tab)

    def game_mode(self):
        """游戏模式，隐藏控件"""
        self.user_info_button.place_forget()
        self.user_type_combo.place_forget()
        self.user_identity_combo.place_forget()

    def change_user_identity_list(self, event=None):
        """身份类型下拉框选择后触发事件"""
        self.user_type = self.user_type_combo.get()
        self.user_identity_combo['value'] = identity_info_dict.get(self.user_type_combo.get(), identity_info_dict[''])
        if self.user_identity_combo.get() not in self.user_identity_combo['value']:
            self.user_identity_combo.set('')

    def change_tips(self, event=None):
        """更改可选项"""
        pass
        # if event.keysym != "Tab":
        #     if len(user_identity_combo_value := self.user_identity_combo.get()) > 0:
        #         self.user_identity_combo['value'] = [keyword for keyword in
        #                                              identity_info_dict.get(self.user_type_combo.get(),
        #                                                                     identity_info_dict['']) if
        #                                              user_identity_combo_value in keyword]
        #     else:
        #         self.user_identity_combo['value'] = identity_info_dict.get(self.user_type_combo.get(),
        #                                                                    identity_info_dict[''])
        #     # self.tab_choose = 0

    def key_tab(self, event=None):
        """身份下拉框按下Tab键时触发事件"""
        # 失去焦点  不能连续点按来切换提示内容  改为展示下拉框选项
        # if self.tab_choose >= len(user_identity_combo_list := self.user_identity_combo['value']):
        #     self.tab_choose = 0
        # self.user_identity_combo.set(user_identity_combo_list[self.tab_choose])
        # self.tab_choose += 1
        # self.user_identity_combo.state(['readonly'])
        pass


class WindowConfigParams:
    """窗口配置项参数"""
    background_color: str = '#000000'
    title_color: str = 'black'
    title_background_color: str = '#fdfafa'
    title_bar_height: int = 40


class MainWindow(WindowConfigParams):
    """主窗口"""

    def __init__(self):
        self.root: tk.Tk = tk.Tk()
        self.root_width: int = self.root.winfo_screenwidth()
        self.root_height: int = self.root.winfo_screenheight()
        self.mode_val: tk.StringVar = tk.StringVar()
        self.init_window()
        self.user_data_list: t.List[UserData] = []
        self.init_user_data()

    def init_user_data(self):
        """用户数据初始化"""
        self.user_data_list: t.List[UserData] = []
        screen_height, screen_width = self.root_height, self.root_width
        box_height, box_width = int(screen_height * 0.1459), int(screen_width * 0.194)

        x = int(screen_height * 0.09)
        for _ in range(4):
            y = int(screen_width * 0.1)
            for _ in range(4):
                self.user_data_list.append(UserData(self, (x + box_width, y)))
                y = y + box_height + 30
            x = x + box_width + 30

    def init_window(self):
        """窗口初始化"""
        # 禁用tab
        self.root.bind_all("<Tab>", lambda event: "break")
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

        self.mode_val.set('游戏模式')
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

    def reset_info(self):
        """初始化数据"""
        self.mode_val.set('游戏模式')
        [_.game_mode() for _ in self.user_data_list]
        self.init_user_data()

    def change_mode(self):
        """切换模式"""
        mode_val = self.mode_val.get()
        if mode_val == '会议模式':
            self.mode_val.set('游戏模式')
            [_.game_mode() for _ in self.user_data_list]
        else:
            self.mode_val.set('会议模式')
            [_.meeting_mode() for _ in self.user_data_list]


class PopWin:
    """弹窗"""

    def __init__(self, cuurent_user: UserData, win_coordinate: tuple):
        """

        :param cuurent_user:
        :param win_coordinate:
        """
        self.current_user: UserData = cuurent_user
        self.pop_flag: bool = False
        self.pop_win: t.Optional[tk.Toplevel] = None
        self.text_input: t.Optional[tk.Text] = None
        self.win_coordinate: tuple = win_coordinate

    def pop_win_command(self):
        """弹出窗口"""
        if not self.pop_flag:
            self.pop_flag = True
            self.pop_win = tk.Toplevel()
            self.text_input = tk.Text(self.pop_win)
            self.pop_win.title('发言信息')
            self.pop_win.attributes('-toolwindow', True)
            self.pop_win.geometry(f'300x200+{self.win_coordinate[0]}+{self.win_coordinate[1]}')
            self.text_input.pack(fill='both', expand=True)
            self.text_input.focus_set()
            self.text_input.insert(tk.END, self.current_user.user_info)

            self.pop_win.bind('<Escape>', self.close_win)
            self.pop_win.protocol('WM_DELETE_WINDOW', self.close_win)
        else:
            self.close_win()

    def close_win(self, event=None):
        """关闭窗口"""
        self.pop_flag = False
        self.current_user.user_info = '\n'.join(self.text_input.get('0.0', tk.END).split('\n')[:-1])
        self.pop_win.destroy()


if __name__ == '__main__':
    main_loop = MainWindow()
    main_loop.root.mainloop()
