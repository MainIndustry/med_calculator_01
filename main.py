from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout


class MyCalculatorApp(MDApp):
    def build(self):
        return

    def change_genit(self):
        sh = self.root.ids.nav_manager.get_screen('menu').ids.menu_manager.get_screen('ballard').ids
        if sh.genit2.active == True:
            sh.ballardtext61.text = "Выступающий клитор, плоские половые губы"
            sh.ballardtext62.text = "Выступающий клитор, полностью открытые небольшие малые половые губы"
            sh.ballardtext63.text = "Выступающий клитор, полностью открытые малые половые губы"
            sh.ballardtext64.text = "Одинаково выраженные большие и малые половые губы"
            sh.ballardtext65.text = "Большие половые губы частично закрывают малые"
            sh.ballardtext66.text = "Большие половые губы полностью закрывают малые половые губы и клитор"
        else:
            sh.ballardtext61.text = "Мошонка, пустая, гладкая"
            sh.ballardtext62.text = "Мошонка, пустая, незначительные складки"
            sh.ballardtext63.text = "Яички расположены над входом в мошонку, редкие складки"
            sh.ballardtext64.text = "Яички опускаются в мошонку (процесс не завершён), несколько складок"
            sh.ballardtext65.text = "Яички опущены в мошонку, складки хорошо выражены"
            sh.ballardtext66.text = "Яички свободно подвешены в мошонке, хорошо выражены глубокие складки"
    def open_menu(self):
        self.root.ids.nav_drawer.set_state("toggle")

    def back_to_menu(self):
        self.root.ids.nav_manager.get_screen('menu').ids.menu_manager.current = "calculator"

    def check(self, instance):
        s = ToggleButtonBehavior.get_widgets(instance.group)
        print(instance.active)
        print(s)
        for widget in s:
            if widget.active:
                print(widget)

    def count_silverman(self):
        c1 = ToggleButtonBehavior.get_widgets('silver1')
        c2 = ToggleButtonBehavior.get_widgets('silver2')
        c3 = ToggleButtonBehavior.get_widgets('silver3')
        c4 = ToggleButtonBehavior.get_widgets('silver4')
        c5 = ToggleButtonBehavior.get_widgets('silver5')
        c_sum = c1 + c2 + c3 + c4 + c5
        y = 0
        for widget in c_sum:
            if widget.active:
                y += 1
        if y == 5:
            sh = self.root.ids.nav_manager.get_screen('menu').ids.menu_manager.get_screen('silverman').ids
            x1 = 1 if sh.silverman12.active == True else (2 if sh.silverman13.active == True else 0)
            x2 = 1 if sh.silverman22.active == True else (2 if sh.silverman23.active == True else 0)
            x3 = 1 if sh.silverman32.active == True else (2 if sh.silverman33.active == True else 0)
            x4 = 1 if sh.silverman42.active == True else (2 if sh.silverman43.active == True else 0)
            x5 = 1 if sh.silverman52.active == True else (2 if sh.silverman53.active == True else 0)
            x_sum = x1 + x2 + x3 + x4 + x5
            res = self.root.ids.nav_manager.get_screen('menu').ids.menu_manager.get_screen('silverman').ids.result
            match x_sum:
                case 1:
                    res.text = "1 балл"
                case 2 | 3 | 4:
                    res.text = f"{x_sum} балла"
                case 5 | 6 | 7 | 8 | 9 | 10 | 0:
                    res.text = f"{x_sum} баллов"
            inter = self.root.ids.nav_manager.get_screen('menu').ids.menu_manager.get_screen('silverman').ids.inter
            match x_sum:
                case 0:
                    inter.text = "Всё хорошо"
                case 1 | 2 | 3:
                    inter.text = "Лёгкое"
                case 4 | 5 | 6:
                    inter.text = "Средне"
                case 7 | 8 | 9:
                    inter.text = "Тяжело"
                case 10:
                    inter.text = "Всё очень плохо"
        else:
            self.root.ids.nav_manager.get_screen('menu').ids.menu_manager.get_screen('silverman').ids.result.text = ""
            self.root.ids.nav_manager.get_screen('menu').ids.menu_manager.get_screen('silverman').ids.inter.text = ""

    def clear_silverman(self):
        c1 = ToggleButtonBehavior.get_widgets('silver1')
        c2 = ToggleButtonBehavior.get_widgets('silver2')
        c3 = ToggleButtonBehavior.get_widgets('silver3')
        c4 = ToggleButtonBehavior.get_widgets('silver4')
        c5 = ToggleButtonBehavior.get_widgets('silver5')
        c_sum = c1 + c2 + c3 + c4 + c5
        for widget in c_sum:
            if widget.active == True:
                widget.active = False
        self.root.ids.nav_manager.get_screen('menu').ids.menu_manager.get_screen('silverman').ids.result.text = ""
        self.root.ids.nav_manager.get_screen('menu').ids.menu_manager.get_screen('silverman').ids.inter.text = ""

    def count_downes(self):
        c1 = ToggleButtonBehavior.get_widgets('downes1')
        c2 = ToggleButtonBehavior.get_widgets('downes2')
        c3 = ToggleButtonBehavior.get_widgets('downes3')
        c4 = ToggleButtonBehavior.get_widgets('downes4')
        c5 = ToggleButtonBehavior.get_widgets('downes5')
        c_sum = c1 + c2 + c3 + c4 + c5
        y = 0
        for widget in c_sum:
            if widget.active == True:
                y += 1
        if y == 5:
            sh = self.root.ids.nav_manager.get_screen('menu').ids.menu_manager.get_screen('downes').ids
            x1 = 1 if sh.downes12.active == True else (2 if sh.downes13.active == True else 0)
            x2 = 1 if sh.downes22.active == True else (2 if sh.downes23.active == True else 0)
            x3 = 1 if sh.downes32.active == True else (2 if sh.downes33.active == True else 0)
            x4 = 1 if sh.downes42.active == True else (2 if sh.downes43.active == True else 0)
            x5 = 1 if sh.downes52.active == True else (2 if sh.downes53.active == True else 0)
            x_sum = x1 + x2 + x3 + x4 + x5
            res = self.root.ids.nav_manager.get_screen('menu').ids.menu_manager.get_screen('downes').ids.result
            match x_sum:
                case 1:
                    res.text = "1 балл"
                case 2 | 3 | 4:
                    res.text = f"{x_sum} балла"
                case 5 | 6 | 7 | 8 | 9 | 10 | 0:
                    res.text = f"{x_sum} баллов"
            inter = self.root.ids.nav_manager.get_screen('menu').ids.menu_manager.get_screen('downes').ids.inter
            match x_sum:
                case 0 | 1 | 2:
                    inter.text = "Дыхательная недостаточность отсутствует"
                case 3 | 4:
                    inter.text = "Лёгкая дыхательная недостаточность"
                case 5 | 6:
                    inter.text = "Дыхательная недостаточность средней тяжести"
                case _:
                    inter.text = "Тяжелая дыхательная недостаточность"
        else:
            self.root.ids.nav_manager.get_screen('menu').ids.menu_manager.get_screen('downes').ids.result.text = ""
            self.root.ids.nav_manager.get_screen('menu').ids.menu_manager.get_screen('downes').ids.inter.text = ""

    def clear_downes(self):
        c1 = ToggleButtonBehavior.get_widgets('downes1')
        c2 = ToggleButtonBehavior.get_widgets('downes2')
        c3 = ToggleButtonBehavior.get_widgets('downes3')
        c4 = ToggleButtonBehavior.get_widgets('downes4')
        c5 = ToggleButtonBehavior.get_widgets('downes5')
        c_sum = c1 + c2 + c3 + c4 + c5
        for widget in c_sum:
            if widget.active == True:
                widget.active = False
        self.root.ids.nav_manager.get_screen('menu').ids.menu_manager.get_screen('downes').ids.result.text = ""
        self.root.ids.nav_manager.get_screen('menu').ids.menu_manager.get_screen('downes').ids.inter.text = ""

    def count_ballard(self):
        sh = self.root.ids.nav_manager.get_screen('menu').ids.menu_manager.get_screen('ballard').ids
        c1 = []
        c2 = []
        active_group1 = []
        active_group2 = []
        ballard_group1 = ['poza','squarewindow','armrecoil','angle','scarf','heel']
        ballard_group2 = ['ballard1','ballard2','ballard3','ballard4','ballard5','ballard6']
        for item in ballard_group1:
            c1.extend(ToggleButtonBehavior.get_widgets(item))
        for item in ballard_group2:
            c2.extend(ToggleButtonBehavior.get_widgets(item))
        for widget in c1:
            if widget.active == True:
                active_group1.append(widget)
        for widget in c2:
            if widget.active == True:
                active_group2.append(widget)
        if len(active_group1) == 6:
            x1 = 0
            for i in active_group1:
                match i:
                    case sh.squarewindow_1 | sh.angle_1 | sh.scarf_1 | sh.heel_1:
                        x1 += -1
                    case sh.poza_1 | sh.squarewindow_2 | sh.armrecoil_1 | sh.angle_2 | sh.scarf_2 | sh.heel_2:
                        x1 += 0
                    case sh.poza_2 | sh.squarewindow_3 | sh.armrecoil_2 | sh.angle_3 | sh.scarf_3 | sh.heel_3:
                        x1 += 1
                    case sh.poza_3 | sh.squarewindow_4 | sh.armrecoil_3 | sh.angle_4 | sh.scarf_4 | sh.heel_4:
                        x1 += 2
                    case sh.poza_4 | sh.squarewindow_5 | sh.armrecoil_4 | sh.angle_5 | sh.scarf_5 | sh.heel_5:
                        x1 += 3
                    case sh.poza_5 | sh.squarewindow_6 | sh.armrecoil_5 | sh.angle_6 | sh.scarf_6 | sh.heel_6:
                        x1 += 4
                    case sh.angle_7:
                        x1 += 5
            match (x1 % 10):
                case 1:
                    sh.result1.text = f"{x1} балл"
                case 2 | 3 | 4:
                    sh.result1.text = f"{x1} балла"
                case 5 | 6 | 7 | 8 | 9 | 0:
                    sh.result1.text = f"{x1} баллов"
        else:
            sh.result1.text = ""
        if len(active_group2) == 6:
            x2 = 0
            for i in active_group2:
                match i:
                    case sh.ballard31 | sh.ballard51:
                        x2 += -2
                    case sh.ballard11 | sh.ballard21 | sh.ballard32 | sh.ballard41 | sh.ballard52 | sh.ballard61:
                        x2 += -1
                    case sh.ballard12 | sh.ballard22 | sh.ballard33 | sh.ballard42 | sh.ballard53 | sh.ballard62:
                        x2 += 0
                    case sh.ballard13 | sh.ballard23 | sh.ballard34 | sh.ballard43 | sh.ballard54 | sh.ballard63:
                        x2 += 1
                    case sh.ballard14 | sh.ballard24 | sh.ballard35 | sh.ballard44 | sh.ballard55 | sh.ballard64:
                        x2 += 2
                    case sh.ballard15 | sh.ballard25 | sh.ballard36 | sh.ballard45 | sh.ballard56 | sh.ballard65:
                        x2 += 3
                    case sh.ballard16 | sh.ballard26 | sh.ballard37 | sh.ballard46 | sh.ballard57 | sh.ballard66:
                        x2 += 4
                    case sh.ballard17:
                        x2 += 5
            match (x2 % 10):
                case 1:
                    sh.result2.text = f"{x2} балл"
                case 2 | 3 | 4:
                    sh.result2.text = f"{x2} балла"
                case 5 | 6 | 7 | 8 | 9 | 0:
                    sh.result2.text = f"{x2} баллов"
        else:
            sh.result2.text = ""
        if len(active_group1+active_group2) == 12:
            x_sum = x1 + x2
            match (x_sum % 10):
                case 1:
                    sh.resultfinal.text = f"{x_sum} балл"
                case 2 | 3 | 4:
                    sh.resultfinal.text = f"{x_sum} балла"
                case 5 | 6 | 7 | 8 | 9 | 0:
                    sh.resultfinal.text = f"{x_sum} баллов"
            weeks = 24
            if x_sum < 10:
                sh.inter.text = "---"
            elif -10 <= x_sum < -5:
                weeks = 20
            elif -5 <= x_sum < 0:
                weeks = 22
            elif 0 < x_sum:
                a = (x_sum//5) * 2
                weeks += a
            match (weeks % 10):
                case 0 | 6 | 8:
                    sh.inter.text = f"{weeks} недель"
                case 2 | 4:
                    sh.inter.text = f"{weeks} недели"
        else:
            sh.resultfinal.text = ""
            sh.inter.text = ""

    def clear_ballard(self):
        sh = self.root.ids.nav_manager.get_screen('menu').ids.menu_manager.get_screen('ballard').ids
        c = []
        ballard_group = ['poza','squarewindow','armrecoil','angle','scarf','heel',
                         'ballard1', 'ballard2', 'ballard3', 'ballard4', 'ballard5', 'ballard6']
        for item in ballard_group:
            c.extend(ToggleButtonBehavior.get_widgets(item))
        for widget in c:
            if widget.active == True:
                widget.active = False
        sh.result1.text = ""
        sh.result2.text = ""
        sh.resultfinal.text = ""
        sh.inter.text = ""


if __name__ == '__main__':
    app = MyCalculatorApp()
    app.run()
