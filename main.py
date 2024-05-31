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
        items = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        if (items.mass1.text != "") and (items.mass2.text != ""):
            x1 = int(items.mass1.text)
            x2 = int(items.mass2.text)
            y = round(((x1 - x2) * 100 / x1), 1)
            if x1 >= x2:
                y = round(((x1 - x2) * 100 / x1), 1)
                items.result.text = f"{y} %"
            else:
                items.result.text = "---"
        else:
            items.result.text = ""

    def count_kurosurf(self):
        items = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        if items.mass.text != "":
            x = int(items.mass.text)
            if items.dose1.active:
                dose = 200
            elif items.dose2.active:
                dose = 100
            for widget in ToggleButtonBehavior.get_widgets('dose'):
                if widget.active:
                    z1 = (x/1000) * dose
                    z2 = round((z1 / 80), 1)
                    z3 = math.ceil(z2/1.5)
                    items.result1.text = f"{z1} мг"
                    items.result2.text = f"{z2} мл"
                    match (z3 % 10):
                        case 1:
                            items.result3.text = f"{z3} флакон"
                        case 2 | 3 | 4:
                            items.result3.text = f"{z3} флакона"
                        case 5 | 6 | 7 | 8 | 9 | 0:
                            items.result3.text = f"{z3} флаконов"
        else:
            items.result1.text = ""
            items.result2.text = ""
            items.result3.text = ""

    def count_cofe(self):
        items = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        if items.mass.text != "":
            x = int(items.mass.text)
            if items.cofe1.active:
                cofe = 20
            elif items.cofe2.active:
                cofe = 5
            for widget in ToggleButtonBehavior.get_widgets('cofe'):
                if widget.active:
                    z = (x/1000) * cofe
                    items.result.text = f"{z} мг"
        else:
            items.result.text = ""

    def count_dofamine(self):
        items = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        if items.mass.text != "" and items.dofa.text != "":
            x = int(items.mass.text)
            dofa = float(items.dofa.text)
            z = round(((x/1000) * dofa * 24 * 60)/40000, 2)
            items.result.text = f"{z} мл"
        else:
            items.result.text = ""

    def count_metro(self):
        items = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        if items.mass.text != "" and items.dose.text != "" and items.crat.text != "0" and items.crat.text != "":
            x = int(items.mass.text)
            dose = float(items.dose.text)
            crat = int(items.crat.text)
            z1 = round((x / 1000) * dose, 2)
            if crat == 1:
                z2 = z1
                items.result1.text = f"{z2} мг/сут"
                z3 = round(z2/5, 2)
                items.result2.text = f"{z3} мл/сут"
            else:
                z2 = round(z1 / crat, 2)
                time = int(24 / crat)
                items.result1.text = f"{z2} мг/{time} час"
                z3 = round(z2 / 5, 2)
                items.result2.text = f"{z3} мл/{time} час"
        else:
            items.result1.text = ""
            items.result2.text = ""

    def count_ampi(self):
        items = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        if items.mass.text != "" and items.dose.text != "" and items.crat.text != "0" and items.crat.text != "":
            x = int(items.mass.text)
            dose = float(items.dose.text)
            crat = int(items.crat.text)
            z1 = round((x / 1000) * dose, 2)
            time = int(24 / crat)
            if crat == 1:
                z2 = z1
                items.result1.text = f"{z2} мг/сут"
            else:
                z2 = round(z1 / crat, 2)
                items.result1.text = f"{z2} мг/{time} час"
        else:
            items.result1.text = ""
        if items.flacone1.active:
            flacone = 500
        elif items.flacone2.active:
            flacone = 1000
        elif items.flacone3.active:
            flacone = 2000
        if items.result1.text != "" and items.crat.text != "0" and items.crat.text != "" and items.volume.text != "":
            volume = float(items.volume.text)
            for widget in ToggleButtonBehavior.get_widgets('flacone'):
                if widget.active:
                    z31 = round(flacone/volume, 2)
                    z32 = round(z2/z31, 2)
                    if crat == 1:
                        items.result2.text = f"{z32} мл/сут"
                    else:
                        items.result2.text = f"{z32} мл/{time} час"
        else:
            items.result2.text = ""
    def count_genta(self):
        items = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        if items.mass.text != "" and items.dose.text != "" and items.crat.text != "0" and items.crat.text != "":
            x = int(items.mass.text)
            dose = float(items.dose.text)
            crat = int(items.crat.text)
            z1 = round((x / 1000) * dose, 2)
            if crat == 1:
                z2 = z1
                items.result1.text = f"{z2} мг/сут"
                z3 = round(z2/40, 2)
                items.result2.text = f"{z3} мл/сут"
            else:
                z2 = round(z1 / crat, 2)
                time = int(24 / crat)
                items.result1.text = f"{z2} мг/{time} час"
                z3 = round(z2 / 40, 2)
                items.result2.text = f"{z3} мл/{time} час"
        else:
            items.result1.text = ""
            items.result2.text = ""
    def count_neutroindex(self):
        items = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        if (items.percent1.text != "" and items.percent2.text != "" and items.percent3.text != ""
                and items.percent4.text != ""):
            x1 = float(items.percent1.text)
            x2 = float(items.percent2.text)
            x3 = float(items.percent3.text)
            x4 = float(items.percent4.text)
            y = round(((x1 + x2 + x3) / x4), 2)
            if (x1+x2+x3+x4) >= 100:
                items.result.text = ""
            else:
                items.result.text = f"{y}"
        else:
            items.result.text = ""

    def count_entfunc(self):
        items = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        if items.mass.text != "" and items.day.text != "" and items.day.text != "0":
            x = int(items.mass.text)
            day = int(items.day.text)
            z = round((x / 1000) * day * 3)
            items.result.text = f"{z} мл"
        else:
            items.result.text = ""

    def count_entzayaz(self):
        items = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        if items.mass.text != "" and items.day.text != "" and items.day.text != "0":
            x = int(items.mass.text)
            day = int(items.day.text)
            z1 = round((x / 100 * 2) * day)
            if day > 28:
                items.result1.text = ""
            else:
                if 28 >= day > 10:
                    if z1 > round(x/5):
                        z1 = round(x/5)
                        items.result1.text = f"{z1} мл"
                else:
                    items.result1.text = f"{z1} мл"
        else:
            items.result1.text = ""
        if items.result1.text != ""  and items.crat.text != "" and items.crat.text != "0":
            crat = int(items.crat.text)
            z2 = round(z1 / crat)
            items.result2.text = f"{z2} мл"
        else:
            items.result2.text = ""



    def count_entenergy(self):
        items = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        if items.mass.text != "" and items.day.text != "" and items.day.text != "0":
            x = int(items.mass.text)
            day = int(items.day.text)
            if day <= 10:
                energy = 20 + day * 10
            else:
                energy = 120
            items.energy.text = f"{energy} ккал/кг/сут"
            z1 = round(((x / 1000) * 100 * energy)/70)
            if day > 28:
                items.result1.text = ""
            else:
                if 28 >= day > 10:
                    if z1 > round(x/5):
                        z1 = round(x/5)
                        items.result1.text = f"{z1} мл"
                else:
                    items.result1.text = f"{z1} мл"
        else:
            items.result1.text = ""
            items.energy.text = ""
        if items.result1.text != "" and items.crat.text != "" and items.crat.text != "0":
            crat = int(items.crat.text)
            z2 = round(z1 / crat)
            items.result2.text = f"{z2} мл"
        else:
            items.result2.text = ""

    def count_parent(self):
        items = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        # day = int(items.day.text)
        if items.mass.text != "" and items.physneed.text != "":
            physneed = float(items.physneed.text)
            mass = int(items.mass.text)/1000
            dayneed = round(physneed * mass, 1)
            items.dayneed.text = f"{dayneed} мл/сут"
        else:
            items.dayneed.text = ""
        if items.volumeonetime.text != "" and items.count.text != "" and items.dayneed.text != "":
            if items.food1.active:
                x1 = 1
                x2 = 2
                x3 = 3
                x4 = 4
            elif items.food2.active:
                x1 = 7.78
                x2 = 1.27
                x3 = 3.42
                x4 = 67
            elif items.food3.active:
                x1 = 8.4
                x2 = 2.6
                x3 = 3.9
                x4 = 79
            volumeonetime = float(items.volumeonetime.text)
            count = int(items.count.text)
            volumephys = round((volumeonetime * count)/mass, 1)
            items.volumephys.text = f"{volumephys} мл/кг/сут"
            for widget in ToggleButtonBehavior.get_widgets('food'):
                if widget.active:
                    if volumephys < 25:
                        volumeent = 0
                        items.volumeent.multiline = True
                        items.volumeent.text = "Объём энтерального питания не превышает трофический (25 мл/кг/сут)"
                        ugle = 0
                        belki = 0
                        zhiry = 0
                        kkal = 0
                        items.ugle.text = "---"
                        items.belki.text = "---"
                        items.zhiry.text = "---"
                        items.kkal.text = "---"
                    else:
                        volumeent = round(volumeonetime * count, 1)
                        items.volumeent.multiline = False
                        items.volumeent.text = f"{volumeent} мл/сут"
                        ugle = round(volumeent*x1/100, 2)
                        belki = round(volumeent*x2/100, 2)
                        zhiry = round(volumeent*x3/100, 2)
                        kkal = round(volumeent*x4/100, 2)
                        items.ugle.text = f"{ugle} г"
                        items.belki.text = f"{belki} г/кг/сут"
                        items.zhiry.text = f"{zhiry} г/кг/сут"
                        items.kkal.text = f"{kkal} ккал"
        else:
            items.volumephys.text = ""
            items.volumeent.text = ""
            items.ugle.text = ""
            items.belki.text = ""
            items.zhiry.text = ""
            items.kkal.text = ""
        if items.dayneed.text != "" and items.volumeent.text != "" and items.bolus.text != "" :
            bolus = float(items.bolus.text)
            dayneedent = round(dayneed - volumeent - bolus, 1)
            items.dayneedent.text = f"{dayneedent} мл/сут"
        else:
            items.dayneedent.text = ""
        if items.dosebelki.text != "" and items.belki.text != "":
            dosebelki = float(items.dosebelki.text)
            daydosebelki = round((dosebelki * mass - belki), 1)
            items.daydosebelki.text = f"{daydosebelki} г/сут"
            amino = round((daydosebelki * 10), 1)
            items.amino.text = f"{amino} мл/сут"
        else:
            items.daydosebelki.text = ""
            items.amino.text = ""
        if items.dosezhiry.text != "" and items.zhiry.text != "":
            dosezhiry = float(items.dosezhiry.text)
            daydosezhiry = round((dosezhiry * mass - zhiry), 2)
            items.daydosezhiry.text = f"{daydosezhiry} г/сут"
            amulszhiry = round((daydosezhiry * 5), 1)
            items.amulszhiry.text = f"{amulszhiry} мл/сут"
        else:
            items.daydosezhiry.text = ""
            items.amulszhiry.text = ""
        if items.na_need.text != "" and items.mass.text != "":
            na_need = float(items.na_need.text)
            na_dose = round((na_need * mass)/0.15, 1)
            items.na_dose.text = f"{na_dose} мл/сут"
        else:
            items.na_dose.text = ""
        if items.k_need.text != "" and items.mass.text != "":
            k_need = float(items.k_need.text)
            k_dose = round(k_need * mass * 1.85, 1)
            items.k_dose.text = f"{k_dose} мл/сут"
        else:
            items.k_dose.text = ""
        if items.ca_need.text != "" and items.mass.text != "":
            ca_need = float(items.ca_need.text)
            ca_dose = round(ca_need * mass * 3.3, 1)
            items.ca_dose.text = f"{ca_dose} мл/сут"
        else:
            items.ca_dose.text = ""
        if items.mg_need.text != "" and items.mass.text != "":
            mg_need = float(items.mg_need.text)
            mg_dose = round((mg_need * mass)/250, 1)
            items.mg_dose.text = f"{mg_dose} мл/сут"
        else:
            items.mg_dose.text = ""

        if items.ugleneed.text != "" and items.mass.text != "":
            ugleneed = float(items.ugleneed.text)
            daydoseugle = round((mass * ugleneed * 1.44),1)
            items.daydoseugle.text = f"{daydoseugle} г/сут"
        else:
            items.daydoseugle.text = ""

        if (items.na_dose.text != "" and items.k_dose.text != "" and items.ca_dose.text != "" and items.mg_dose.text != ""
            and items.amino.text != "" and items.amulszhiry.text != "" and items.dayneedent.text != ""):
            doseugle = round((dayneedent - amino - amulszhiry - na_dose - k_dose - ca_dose - mg_dose),1)
            items.doseugle.text = f"{doseugle} мл/сут"
        else:
            items.doseugle.text = ""
        if items.conc1.active:
            y1 = 5
            y2 = 10
        elif items.conc2.active:
            y1 = 5
            y2 = 40
        elif items.conc3.active:
            y1 = 10
            y2 = 40
        for widget in ToggleButtonBehavior.get_widgets('conc'):
            if widget.active:
                items.gluk_text1.text = f"Объём раствора глюкозы {y1}% (мл/сут)"
                items.gluk_text2.text = f"Объём раствора глюкозы {y2}% (мл/сут)"
                if (items.daydoseugle.text != "" and items.doseugle.text != ""):
                    v2 = round((daydoseugle * 100 - y1 * doseugle)/(y2-y1), 1)
                    v1 = round(doseugle - v2, 1)
                    if v2 > doseugle:
                        items.gluk1.text = "Выберите другие концентрации"
                        items.gluk2.text = "Выберите другие концентрации"
                    elif v2 == doseugle:
                        items.gluk1.text = "---"
                        items.gluk2.text = f"{v2} мл/сут"
                    else:
                        items.gluk1.text = f"{v1} мл/сут"
                        items.gluk2.text = f"{v2} мл/сут"
                else:
                    items.gluk1.text = ""
                    items.gluk2.text = ""
        if items.dayneedent.text != "" and items.amulszhiry.text != "":
            speed1 = round((dayneedent - amulszhiry)/24, 1)
            speed2 = round(amulszhiry/24, 1)
            items.speed1.text = f"{speed1} мл/ч"
            items.speed2.text = f"{speed2} мл/ч"
        else:
            items.speed1.text = ""
            items.speed2.text = ""
        if items.daydoseugle.text != "" and items.dayneedent.text != "" and items.amulszhiry.text != "":
            concgluk = round(daydoseugle*100/(dayneedent - amulszhiry), 1)
            items.concgluk.text = f"{concgluk}%"
        else:
            items.concgluk.text = ""
        if items.kkal.text != "" and items.daydoseugle.text != "" and items.daydosezhiry.text != "" and items.mass.text != "":
            kkalparent = (daydosezhiry * 9) + (daydoseugle * 4)
            items.kkalparent.text = f"{kkalparent} ккал/сут"
            kkalsum = round((kkal + kkalparent)/mass, 1)
            items.kkalsum.text = f"{kkalsum} ккал/сут/кг"
        else:
            items.kkalparent.text = ""
            items.kkalsum.text = ""



    def count_silverman(self):
        items = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        y = 0
        c = []
        c_group = ['silver1', 'silver2', 'silver3', 'silver4', 'silver5']
        for item in c_group:
            c.extend(ToggleButtonBehavior.get_widgets(item))
        for widget in c:
            if widget.active == True:
                y += 1
        if y == 5:
            x1 = 1 if items.silverman12.active == True else (2 if items.silverman13.active == True else 0)
            x2 = 1 if items.silverman22.active == True else (2 if items.silverman23.active == True else 0)
            x3 = 1 if items.silverman32.active == True else (2 if items.silverman33.active == True else 0)
            x4 = 1 if items.silverman42.active == True else (2 if items.silverman43.active == True else 0)
            x5 = 1 if items.silverman52.active == True else (2 if items.silverman53.active == True else 0)
            x_sum = x1 + x2 + x3 + x4 + x5
            match x_sum:
                case 1:
                    items.result.text = "1 балл"
                case 2 | 3 | 4:
                    items.result.text = f"{x_sum} балла"
                case 5 | 6 | 7 | 8 | 9 | 10 | 0:
                    items.result.text = f"{x_sum} баллов"
            items.inter.multiline = True
            match x_sum:
                case 0:
                    items.inter.text = "Отсутствие дыхательной недостаточности"
                case 1 | 2 | 3:
                    items.inter.text = "Лёгкая степень тяжести синдрома дыхательных расстройств"
                case 4 | 5 | 6:
                    items.inter.text = "Средняя степень тяжести синдрома дыхательных расстройств"
                case 7 | 8 | 9 | 10:
                    items.inter.text = "Тяжёлый синдром дыхательных расстройств"
        else:
            items.result.text = ""
            items.inter.multiline = False
            items.inter.text = ""

    def count_downes(self):
        items = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        y = 0
        c = []
        c_group = ['downes1','downes2','downes3','downes4','downes5']
        for item in c_group:
            c.extend(ToggleButtonBehavior.get_widgets(item))
        for widget in c:
            if widget.active == True:
                y += 1
        if y == 5:
            x1 = 1 if items.downes12.active == True else (2 if items.downes13.active == True else 0)
            x2 = 1 if items.downes22.active == True else (2 if items.downes23.active == True else 0)
            x3 = 1 if items.downes32.active == True else (2 if items.downes33.active == True else 0)
            x4 = 1 if items.downes42.active == True else (2 if items.downes43.active == True else 0)
            x5 = 1 if items.downes52.active == True else (2 if items.downes53.active == True else 0)
            x_sum = x1 + x2 + x3 + x4 + x5
            match x_sum:
                case 1:
                    items.result.text = "1 балл"
                case 2 | 3 | 4:
                    items.result.text = f"{x_sum} балла"
                case 5 | 6 | 7 | 8 | 9 | 10 | 0:
                    items.result.text = f"{x_sum} баллов"
            items.inter.multiline = True
            match x_sum:
                case 0:
                    items.inter.text = "Отсутствие дыхательной недостаточности"
                case 1 | 2 | 3:
                    items.inter.text = "Лёгкая степень тяжести синдрома дыхательных расстройств"
                case 4 | 5 | 6:
                    items.inter.text = "Средняя степень тяжести синдрома дыхательных расстройств"
                case 7 | 8 | 9 | 10:
                    items.inter.text = "Тяжёлый синдром дыхательных расстройств"
        else:
            items.result.text = ""
            items.inter.multiline = False
            items.inter.text = ""
    def count_ballard(self):
        items = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
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
                    case items.squarewindow_1 | items.angle_1 | items.scarf_1 | items.heel_1:
                        x1 += -1
                    case items.poza_1 | items.squarewindow_2 | items.armrecoil_1 | items.angle_2 | items.scarf_2 | items.heel_2:
                        x1 += 0
                    case items.poza_2 | items.squarewindow_3 | items.armrecoil_2 | items.angle_3 | items.scarf_3 | items.heel_3:
                        x1 += 1
                    case items.poza_3 | items.squarewindow_4 | items.armrecoil_3 | items.angle_4 | items.scarf_4 | items.heel_4:
                        x1 += 2
                    case items.poza_4 | items.squarewindow_5 | items.armrecoil_4 | items.angle_5 | items.scarf_5 | items.heel_5:
                        x1 += 3
                    case items.poza_5 | items.squarewindow_6 | items.armrecoil_5 | items.angle_6 | items.scarf_6 | items.heel_6:
                        x1 += 4
                    case items.angle_7:
                        x1 += 5
            match (x1 % 10):
                case 1:
                    items.result1.text = f"{x1} балл"
                case 2 | 3 | 4:
                    items.result1.text = f"{x1} балла"
                case 5 | 6 | 7 | 8 | 9 | 0:
                    items.result1.text = f"{x1} баллов"
        else:
            items.result1.text = ""
        if len(active_group2) == 6:
            x2 = 0
            for i in active_group2:
                match i:
                    case items.ballard31 | items.ballard51:
                        x2 += -2
                    case items.ballard11 | items.ballard21 | items.ballard32 | items.ballard41 | items.ballard52 | items.ballard61:
                        x2 += -1
                    case items.ballard12 | items.ballard22 | items.ballard33 | items.ballard42 | items.ballard53 | items.ballard62:
                        x2 += 0
                    case items.ballard13 | items.ballard23 | items.ballard34 | items.ballard43 | items.ballard54 | items.ballard63:
                        x2 += 1
                    case items.ballard14 | items.ballard24 | items.ballard35 | items.ballard44 | items.ballard55 | items.ballard64:
                        x2 += 2
                    case items.ballard15 | items.ballard25 | items.ballard36 | items.ballard45 | items.ballard56 | items.ballard65:
                        x2 += 3
                    case items.ballard16 | items.ballard26 | items.ballard37 | items.ballard46 | items.ballard57 | items.ballard66:
                        x2 += 4
                    case items.ballard17:
                        x2 += 5
            match (x2 % 10):
                case 1:
                    items.result2.text = f"{x2} балл"
                case 2 | 3 | 4:
                    items.result2.text = f"{x2} балла"
                case 5 | 6 | 7 | 8 | 9 | 0:
                    items.result2.text = f"{x2} баллов"
        else:
            items.result2.text = ""
        if len(active_group1+active_group2) == 12:
            x_sum = x1 + x2
            match (x_sum % 10):
                case 1:
                    items.resultfinal.text = f"{x_sum} балл"
                case 2 | 3 | 4:
                    items.resultfinal.text = f"{x_sum} балла"
                case 5 | 6 | 7 | 8 | 9 | 0:
                    items.resultfinal.text = f"{x_sum} баллов"
            weeks = 24
            if x_sum < 10:
                items.inter.text = "---"
            elif -10 <= x_sum < -5:
                weeks = 20
            elif -5 <= x_sum < 0:
                weeks = 22
            elif 0 < x_sum:
                a = (x_sum//5) * 2
                weeks += a
            match (weeks % 10):
                case 0 | 6 | 8:
                    items.inter.text = f"{weeks} недель"
                case 2 | 4:
                    items.inter.text = f"{weeks} недели"
        else:
            items.resultfinal.text = ""
            items.inter.text = ""

    def change_genit(self):
        items = self.root.ids.nav_manager.current_screen.ids.menu_manager.current_screen.ids
        if items.genit2.active == True:
            items.ballard_text61.text = "Выступающий клитор, плоские половые губы"
            items.ballard_text62.text = "Выступающий клитор, полностью открытые небольшие малые половые губы"
            items.ballard_text63.text = "Выступающий клитор, полностью открытые малые половые губы"
            items.ballard_text64.text = "Одинаково выраженные большие и малые половые губы"
            items.ballard_text65.text = "Большие половые губы частично закрывают малые"
            items.ballard_text66.text = "Большие половые губы полностью закрывают малые половые губы и клитор"
        else:
            items.ballard_text61.text = "Мошонка, пустая, гладкая"
            items.ballard_text62.text = "Мошонка, пустая, незначительные складки"
            items.ballard_text63.text = "Яички расположены над входом в мошонку, редкие складки"
            items.ballard_text64.text = "Яички опускаются в мошонку (процесс не завершён), несколько складок"
            items.ballard_text65.text = "Яички опущены в мошонку, складки хорошо выражены"
            items.ballard_text66.text = "Яички свободно подвешены в мошонке, хорошо выражены глубокие складки"

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
        if self.root.ids.nav_manager.current_screen.ids.menu_manager.current == "ballard":
            items.result1.text = ""
            items.result2.text = ""
            items.resultfinal.text = ""
            items.inter.text = ""
        else:
            items.result.text = ""
            items.inter.text = ""

if __name__ == '__main__':
    app = MyCalculatorApp()
    app.run()
