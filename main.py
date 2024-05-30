from kivy.uix.behaviors import ToggleButtonBehavior
from kivymd.app import MDApp
from kivymd.uix.selectioncontrol.selectioncontrol import MDCheckbox
import math


class MyCalculatorApp(MDApp):
    def build(self):
        return

    def open_menu(self):
        self.root.ids.nav_drawer.set_state("toggle")

    def back_to_menu(self):
        self.root.ids.nav_manager.get_screen('menu').ids.menu_manager.current = "calculator"

    def count_mass(self):
        sh = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        if (sh.mass1.text != "") and (sh.mass2.text != ""):
            x1 = int(sh.mass1.text)
            x2 = int(sh.mass2.text)
            y = round(((x1 - x2) * 100 / x1), 1)
            if x1 >= x2:
                y = round(((x1 - x2) * 100 / x1), 1)
                sh.result.text = f"{y} %"
            else:
                sh.result.text = "---"
        else:
            sh.result.text = ""

    def count_kurosurf(self):
        sh = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        if sh.mass.text != "":
            x = int(sh.mass.text)
            if sh.dose1.active:
                dose = 200
            elif sh.dose2.active:
                dose = 100
            for widget in ToggleButtonBehavior.get_widgets('dose'):
                if widget.active:
                    z1 = (x/1000) * dose
                    z2 = round((z1 / 80), 1)
                    z3 = math.ceil(z2/1.5)
                    sh.result1.text = f"{z1} мг"
                    sh.result2.text = f"{z2} мл"
                    match (z3 % 10):
                        case 1:
                            sh.result3.text = f"{z3} флакон"
                        case 2 | 3 | 4:
                            sh.result3.text = f"{z3} флакона"
                        case 5 | 6 | 7 | 8 | 9 | 0:
                            sh.result3.text = f"{z3} флаконов"
        else:
            sh.result1.text = ""
            sh.result2.text = ""
            sh.result3.text = ""

    def count_cofe(self):
        sh = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        if sh.mass.text != "":
            x = int(sh.mass.text)
            if sh.cofe1.active:
                cofe = 20
            elif sh.cofe2.active:
                cofe = 5
            for widget in ToggleButtonBehavior.get_widgets('cofe'):
                if widget.active:
                    z = (x/1000) * cofe
                    sh.result.text = f"{z} мг"
        else:
            sh.result.text = ""

    def count_dofamine(self):
        sh = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        if sh.mass.text != "" and sh.dofa.text != "":
            x = int(sh.mass.text)
            dofa = float(sh.dofa.text)
            z = round(((x/1000) * dofa * 24 * 60)/40000, 2)
            sh.result.text = f"{z} мл"
        else:
            sh.result.text = ""

    def count_metro(self):
        sh = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        if sh.mass.text != "" and sh.dose.text != "" and sh.crat.text != "0" and sh.crat.text != "":
            x = int(sh.mass.text)
            dose = float(sh.dose.text)
            crat = int(sh.crat.text)
            z1 = round((x / 1000) * dose, 2)
            if crat == 1:
                z2 = z1
                sh.result1.text = f"{z2} мг/сут"
                z3 = round(z2/5, 2)
                sh.result2.text = f"{z3} мл/сут"
            else:
                z2 = round(z1 / crat, 2)
                time = int(24 / crat)
                sh.result1.text = f"{z2} мг/{time} час"
                z3 = round(z2 / 5, 2)
                sh.result2.text = f"{z3} мл/{time} час"
        else:
            sh.result1.text = ""
            sh.result2.text = ""

    def count_ampi(self):
        sh = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        if sh.mass.text != "" and sh.dose.text != "" and sh.crat.text != "0" and sh.crat.text != "":
            x = int(sh.mass.text)
            dose = float(sh.dose.text)
            crat = int(sh.crat.text)
            z1 = round((x / 1000) * dose, 2)
            time = int(24 / crat)
            if crat == 1:
                z2 = z1
                sh.result1.text = f"{z2} мг/сут"
            else:
                z2 = round(z1 / crat, 2)
                sh.result1.text = f"{z2} мг/{time} час"
        else:
            sh.result1.text = ""
        if sh.flacone1.active:
            flacone = 500
        elif sh.flacone2.active:
            flacone = 1000
        elif sh.flacone3.active:
            flacone = 2000
        if sh.result1.text != "" and sh.crat.text != "0" and sh.crat.text != "" and sh.volume.text != "":
            volume = int(sh.volume.text)
            for widget in ToggleButtonBehavior.get_widgets('flacone'):
                if widget.active:
                    z31 = round(flacone/volume, 2)
                    z32 = round(z2/z31, 2)
                    if crat == 1:
                        sh.result2.text = f"{z32} мл/сут"
                    else:
                        sh.result2.text = f"{z32} мл/{time} час"
        else:
            sh.result2.text = ""
    def count_genta(self):
        sh = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        if sh.mass.text != "" and sh.dose.text != "" and sh.crat.text != "0" and sh.crat.text != "":
            x = int(sh.mass.text)
            dose = float(sh.dose.text)
            crat = int(sh.crat.text)
            z1 = round((x / 1000) * dose, 2)
            if crat == 1:
                z2 = z1
                sh.result1.text = f"{z2} мг/сут"
                z3 = round(z2/40, 2)
                sh.result2.text = f"{z3} мл/сут"
            else:
                z2 = round(z1 / crat, 2)
                time = int(24 / crat)
                sh.result1.text = f"{z2} мг/{time} час"
                z3 = round(z2 / 40, 2)
                sh.result2.text = f"{z3} мл/{time} час"
        else:
            sh.result1.text = ""
            sh.result2.text = ""
    def count_neutroindex(self):
        sh = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        if (sh.percent1.text != "" and sh.percent2.text != "" and sh.percent3.text != ""
                and sh.percent4.text != ""):
            x1 = float(sh.percent1.text)
            x2 = float(sh.percent2.text)
            x3 = float(sh.percent3.text)
            x4 = float(sh.percent4.text)
            y = round(((x1 + x2 + x3) / x4), 2)
            if (x1+x2+x3+x4) >= 100:
                sh.result.text = ""
            else:
                sh.result.text = f"{y}"
        else:
            sh.result.text = ""

    def count_entfunc(self):
        sh = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        if sh.mass.text != "" and sh.day.text != "" and sh.day.text != "0":
            x = int(sh.mass.text)
            day = int(sh.day.text)
            z = round((x / 1000) * day * 3)
            sh.result.text = f"{z} мл"
        else:
            sh.result.text = ""

    def count_entzayaz(self):
        sh = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        if sh.mass.text != "" and sh.day.text != "" and sh.day.text != "0":
            x = int(sh.mass.text)
            day = int(sh.day.text)
            z1 = round((x / 100 * 2) * day)
            if day > 28:
                sh.result1.text = ""
            else:
                if 28 >= day > 10:
                    if z1 > round(x/5):
                        z1 = round(x/5)
                        sh.result1.text = f"{z1} мл"
                else:
                    sh.result1.text = f"{z1} мл"
        else:
            sh.result1.text = ""
        if sh.result1.text != ""  and sh.crat.text != "" and sh.crat.text != "0":
            crat = int(sh.crat.text)
            z2 = round(z1 / crat)
            sh.result2.text = f"{z2} мл"
        else:
            sh.result2.text = ""



    def count_entenergy(self):
        sh = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        if sh.mass.text != "" and sh.day.text != "" and sh.day.text != "0":
            x = int(sh.mass.text)
            day = int(sh.day.text)
            if day <= 10:
                energy = 20 + day * 10
            else:
                energy = 120
            sh.energy.text = f"{energy} ккал/кг/сут"
            z1 = round(((x / 1000) * 100 * energy)/70)
            if day > 28:
                sh.result1.text = ""
            else:
                if 28 >= day > 10:
                    if z1 > round(x/5):
                        z1 = round(x/5)
                        sh.result1.text = f"{z1} мл"
                else:
                    sh.result1.text = f"{z1} мл"
        else:
            sh.result1.text = ""
            sh.energy.text = ""
        if sh.result1.text != "" and sh.crat.text != "" and sh.crat.text != "0":
            crat = int(sh.crat.text)
            z2 = round(z1 / crat)
            sh.result2.text = f"{z2} мл"
        else:
            sh.result2.text = ""

    def count_parent(self):
        sh = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        # day = int(sh.day.text)
        if sh.mass.text != "" and sh.physneed.text != "":
            physneed = float(sh.physneed.text)
            mass = int(sh.mass.text)/1000
            dayneed = round(physneed * mass, 1)
            sh.dayneed.text = f"{dayneed} мл/сут"
        else:
            sh.dayneed.text = ""
        if sh.volumeonetime.text != "" and sh.count.text != "" and sh.dayneed.text != "":
            if sh.food1.active:
                x1 = 1
                x2 = 2
                x3 = 3
                x4 = 4
            elif sh.food2.active:
                x1 = 7.78
                x2 = 1.27
                x3 = 3.42
                x4 = 67
            elif sh.food3.active:
                x1 = 8.4
                x2 = 2.6
                x3 = 3.9
                x4 = 79
            volumeonetime = float(sh.volumeonetime.text)
            count = int(sh.count.text)
            volumephys = round((volumeonetime * count)/mass, 1)
            sh.volumephys.text = f"{volumephys} мл/кг/сут"
            for widget in ToggleButtonBehavior.get_widgets('food'):
                if widget.active:
                    if volumephys < 25:
                        volumeent = 0
                        sh.volumeent.multiline = True
                        sh.volumeent.text = "Объём энтерального питания не превышает трофический (25 мл/кг/сут)"
                        ugle = 0
                        belki = 0
                        zhiry = 0
                        kkal = 0
                        sh.ugle.text = "---"
                        sh.belki.text = "---"
                        sh.zhiry.text = "---"
                        sh.kkal.text = "---"
                    else:
                        volumeent = round(volumeonetime * count, 1)
                        sh.volumeent.multiline = False
                        sh.volumeent.text = f"{volumeent} мл/сут"
                        ugle = round(volumeent*x1/100, 2)
                        belki = round(volumeent*x2/100, 2)
                        zhiry = round(volumeent*x3/100, 2)
                        kkal = round(volumeent*x4/100, 2)
                        sh.ugle.text = f"{ugle} г"
                        sh.belki.text = f"{belki} г/кг/сут"
                        sh.zhiry.text = f"{zhiry} г/кг/сут"
                        sh.kkal.text = f"{kkal} ккал"
        else:
            sh.volumephys.text = ""
            sh.volumeent.text = ""
            sh.ugle.text = ""
            sh.belki.text = ""
            sh.zhiry.text = ""
            sh.kkal.text = ""
        if sh.dayneed.text != "" and sh.volumeent.text != "" and sh.bolus.text != "" :
            bolus = float(sh.bolus.text)
            dayneedent = round(dayneed - volumeent - bolus, 1)
            sh.dayneedent.text = f"{dayneedent} мл/сут"
        else:
            sh.dayneedent.text = ""
        if sh.dosebelki.text != "" and sh.belki.text != "":
            dosebelki = float(sh.dosebelki.text)
            daydosebelki = round((dosebelki * mass - belki), 1)
            sh.daydosebelki.text = f"{daydosebelki} г/сут"
            amino = round((daydosebelki * 10), 1)
            sh.amino.text = f"{amino} мл/сут"
        else:
            sh.daydosebelki.text = ""
            sh.amino.text = ""
        if sh.dosezhiry.text != "" and sh.zhiry.text != "":
            dosezhiry = float(sh.dosezhiry.text)
            daydosezhiry = round((dosezhiry * mass - zhiry), 2)
            sh.daydosezhiry.text = f"{daydosezhiry} г/сут"
            amulszhiry = round((daydosezhiry * 5), 1)
            sh.amulszhiry.text = f"{amulszhiry} мл/сут"
        else:
            sh.daydosezhiry.text = ""
            sh.amulszhiry.text = ""
        if sh.na_need.text != "" and sh.mass.text != "":
            na_need = float(sh.na_need.text)
            na_dose = round((na_need * mass)/0.15, 1)
            sh.na_dose.text = f"{na_dose} мл/сут"
        else:
            sh.na_dose.text = ""
        if sh.k_need.text != "" and sh.mass.text != "":
            k_need = float(sh.k_need.text)
            k_dose = round(k_need * mass * 1.85, 1)
            sh.k_dose.text = f"{k_dose} мл/сут"
        else:
            sh.k_dose.text = ""
        if sh.ca_need.text != "" and sh.mass.text != "":
            ca_need = float(sh.ca_need.text)
            ca_dose = round(ca_need * mass * 3.3, 1)
            sh.ca_dose.text = f"{ca_dose} мл/сут"
        else:
            sh.ca_dose.text = ""
        if sh.mg_need.text != "" and sh.mass.text != "":
            mg_need = float(sh.mg_need.text)
            mg_dose = round((mg_need * mass)/250, 1)
            sh.mg_dose.text = f"{mg_dose} мл/сут"
        else:
            sh.mg_dose.text = ""

        if sh.ugleneed.text != "" and sh.mass.text != "":
            ugleneed = float(sh.ugleneed.text)
            daydoseugle = round((mass * ugleneed * 1.44),1)
            sh.daydoseugle.text = f"{daydoseugle} г/сут"
        else:
            sh.daydoseugle.text = ""

        if (sh.na_dose.text != "" and sh.k_dose.text != "" and sh.ca_dose.text != "" and sh.mg_dose.text != ""
            and sh.amino.text != "" and sh.amulszhiry.text != "" and sh.dayneedent.text != ""):
            doseugle = round((dayneedent - amino - amulszhiry - na_dose - k_dose - ca_dose - mg_dose),1)
            sh.doseugle.text = f"{doseugle} мл/сут"
        else:
            sh.doseugle.text = ""
        if sh.conc1.active:
            y1 = 5
            y2 = 10
        elif sh.conc2.active:
            y1 = 5
            y2 = 40
        elif sh.conc3.active:
            y1 = 10
            y2 = 40
        for widget in ToggleButtonBehavior.get_widgets('conc'):
            if widget.active:
                sh.gluk_text1.text = f"Объём раствора глюкозы {y1}% (мл/сут)"
                sh.gluk_text2.text = f"Объём раствора глюкозы {y2}% (мл/сут)"
                if (sh.daydoseugle.text != "" and sh.doseugle.text != ""):
                    v2 = round((daydoseugle * 100 - y1 * doseugle)/(y2-y1), 1)
                    v1 = round(doseugle - v2, 1)
                    if v2 > doseugle:
                        sh.gluk1.text = "Выберите другие концентрации"
                        sh.gluk2.text = "Выберите другие концентрации"
                    elif v2 == doseugle:
                        sh.gluk1.text = "---"
                        sh.gluk2.text = f"{v2} мл/сут"
                    else:
                        sh.gluk1.text = f"{v1} мл/сут"
                        sh.gluk2.text = f"{v2} мл/сут"
                else:
                    sh.gluk1.text = ""
                    sh.gluk2.text = ""
        if sh.dayneedent.text != "" and sh.amulszhiry.text != "":
            speed1 = round((dayneedent - amulszhiry)/24, 1)
            speed2 = round(amulszhiry/24, 1)
            sh.speed1.text = f"{speed1} мл/ч"
            sh.speed2.text = f"{speed2} мл/ч"
        else:
            sh.speed1.text = ""
            sh.speed2.text = ""
        if sh.daydoseugle.text != "" and sh.dayneedent.text != "" and sh.amulszhiry.text != "":
            concgluk = round(daydoseugle*100/(dayneedent - amulszhiry), 1)
            sh.concgluk.text = f"{concgluk}%"
        else:
            sh.concgluk.text = ""
        if sh.kkal.text != "" and sh.daydoseugle.text != "" and sh.daydosezhiry.text != "" and sh.mass.text != "":
            kkalparent = (daydosezhiry * 9) + (daydoseugle * 4)
            sh.kkalparent.text = f"{kkalparent} ккал/сут"
            kkalsum = round((kkal + kkalparent)/mass, 1)
            sh.kkalsum.text = f"{kkalsum} ккал/сут/кг"
        else:
            sh.kkalparent.text = ""
            sh.kkalsum.text = ""



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

    def clear_calculator(self):
        items = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        for item in items:
            if isinstance(items[item], MDCheckbox) == False:
                items[item].text = ""

    def clear_scale(self):
        items = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        for item in items:
            if isinstance(items[item], MDCheckbox):
                items[item].active = False
            else:
                items[item].text = ""

if __name__ == '__main__':
    app = MyCalculatorApp()
    app.run()
