from kivy.uix.behaviors import ToggleButtonBehavior
from kivymd.app import MDApp


class MyCalculatorApp(MDApp):
    def build(self):
        return

    def open_menu(self):
        self.root.ids.nav_drawer.set_state("toggle")

    def back_to_menu(self):
        self.root.ids.nav_manager.get_screen('menu').ids.menu_manager.current = "calculator"

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


if __name__ == '__main__':
    app = MyCalculatorApp()
    app.run()
