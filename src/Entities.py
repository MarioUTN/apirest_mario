# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 11:28:34 2022

@author: Mario
"""


import math
from fractions import Fraction
import json

#01
class Punto:

    def __init__(self, id_punto, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.id_punto = id_punto

    def get_X(self):
        return self.coord_x

    def set_X(self, x):
        self.coord_x = x

    def Show_Point(self):
        return "({0},{1})".format(self.coord_x, self.coord_y)

    def convert_object_list(self, list):
        try:
            data = json.loads(list)[0]
            p = Punto(data['id_punto'], data['coord_x'], data['coord_y'])
            return p
        except Exception as ex:
            raise Exception(ex)

    def convert_object_json(self, data):
        try:
            p = Punto(data['id_punto'], data['coord_x'], data['coord_y'])
            return p
        except Exception as ex:
            raise Exception(ex)

    def convert_object_json_data(self, data):
        try:
            p = Punto(0, data['coord_x'], data['coord_y'])
            return p
        except Exception as ex:
            raise Exception(ex)

    def convert_to_json(self):
        return {
            "id_punto": self.id_punto,
            "coord_x": self.coord_x,
            "coord_y": self.coord_y
        }

#02
class Circunferencia:

    def __init__(self, id_circunferencia , centro, radio):
        self.id_circunferencia = id_circunferencia
        self.centro = centro
        self.radio = radio

    def CalculateArea(self):
        return round(math.pi * math.pow(self.radio, 2), 2)

    def CalculatePerimeter(self):
        return round(math.pi * self.radio, 2)

    def Sign(self, n):
        if n <= 0:
            return "+"
        else:
            return ""

    def CanonicalEquation(self):
        return "(x{1}{0})^2 + (y{3}{2})^2 = {4}".format(
            self.centro.coord_x * (-1), self.Sign(self.centro.coord_x), self.centro.coord_y * (-1),
            self.Sign(self.centro.coord_y), math.pow(self.radio, 2))

    def Show_Circunference(self):
        return " Radio: {0}\n Point: {1}\n Area: {2} \n Perimeter: {3}\n Canonical Equation: {4}".format(
            self.radio, self.centro.Show_Point(), self.CalculateArea(),
            self.CalculatePerimeter(), self.CanonicalEquation())

    def convert_object_circunference(self, list):
        try:
            data = json.loads(list)[0]
            centro = Punto(0, 0, 0)
            centro = centro.convert_object_json(data['centro'])
            circunference = Circunferencia(data['circunferencia'].get('id_circunferencia'), centro, data['circunferencia'].get('radio'))
            return circunference
        except Exception as ex:
            raise Exception(ex)

    def convert_object_circunference_data(self, data):
        try:
            centro = Punto(0, 0, 0)
            centro = centro.convert_object_json_data(data)
            centro.id_punto = 0
            circunference = Circunferencia(0, centro, data['radio'])
            return circunference
        except Exception as ex:
            raise Exception(ex)

    def get_elements(self):
        return {
            "radius": self.radio,
            "center": self.centro.Show_Point(),
            "area": self.CalculateArea(),
            "perimeter": self.CalculatePerimeter(),
            "equation": self.CanonicalEquation()
        }

    def convert_to_json(self):
        return {
            "id_circunferencia": self.id_circunferencia,
            "centro": self.centro.convert_to_json(),
            "radio": self.radio
        }

#03
class Recta:

    def __init__(self, id_recta, punto_a, punto_b):
        self.id_recta = id_recta
        self.punto_a = punto_a
        self.punto_b = punto_b

    def Distance(self):
        return round(math.sqrt(
            math.pow(self.punto_b.coord_x - self.punto_a.coord_x, 2) +
            math.pow(self.punto_b.coord_y - self.punto_a.coord_y, 2)), 2)

    def Pendiente(self):
        y = self.punto_b.coord_y - self.punto_a.coord_y
        x = self.punto_b.coord_x - self.punto_a.coord_x
        if x != 0:
            return str(Fraction(y/x).limit_denominator())
        else:
            return "0"

    def Sign(self, n):
        if n <= 0:
            return "+"
        else:
            return ""

    def LineEquation(self):
        if self.Pendiente() != "0":
            return "y{0}{1} = {2}(x{3}{4})".format(self.Sign(self.punto_a.coord_y),
                                                   self.punto_a.coord_y * (-1),
                                                   self.Pendiente(),
                                                   self.Sign(self.punto_a.coord_x),
                                                   self.punto_a.coord_x * (-1))
        else:
            return "y = {0}".format(self.punto_a.coord_x)

    def ShowLine(self):
        return "PA: {0}\nPB: {1}\nDistance: {2}\nLine Equation: {3}\nPendiente: {4}".format(
            self.punto_a.Show_Point(), self.punto_b.Show_Point(),
            self.Distance(), self.LineEquation(), self.Pendiente())

    def convert_line(self, list):
        try:
            data = json.loads(list)[0]
            pa = Punto(0, 0, 0)
            pa = pa.convert_object_json(data['punto_a'])
            pb = Punto(0, 0, 0)
            pb = pb.convert_object_json(data['punto_b'])
            line = Recta(data['recta'].get('id_recta'), pa, pb)
            return line
        except Exception as ex:
            raise Exception(ex)

    def convert_line_data(self, data):
        try:
            pa = Punto(0, data['coord_xa'], data['coord_ya'])
            pb = Punto(0, data['coord_xb'], data['coord_yb'])
            line = Recta(0, pa, pb)
            return line
        except Exception as ex:
            raise Exception(ex)


    def get_elements(self):
        return {
            "punto_a": self.punto_a.Show_Point(),
            "punto_b": self.punto_b.Show_Point(),
            "distance": self.Distance(),
            "line_equation": self.LineEquation(),
            "slope": self.Pendiente()
        }


    def convert_to_json(self):
        return {
            "id_recta": self.id_recta,
            "punto_a": self.punto_a.convert_to_json(),
            "punto_b": self.punto_b.convert_to_json()
        }

#04
class Parabola:

    def __init__(self, id_parabola, vertice, p, eje_focal):
        self.id_parabola = id_parabola
        self.vertice = vertice
        self.p = p
        self.eje_focal = eje_focal

    def convert_object_parabola(self, list):
        try:
            data = json.loads(list)[0]
            vertice = Punto(0, 0, 0)
            vertice = vertice.convert_object_json(data['vertice'])
            parabola = Parabola(data['parabola'].get('id_parabola'), vertice,data['parabola'].get('p'), "{0}".format(data['parabola'].get('eje_focal')))
            return parabola
        except Exception as ex:
            raise Exception(ex)

    def convert_object_parabola_data(self, data):
        try:
            vertice = Punto(0, 0, 0)
            vertice = vertice.convert_object_json_data(data)
            vertice.id_punto = 0
            parabola = Parabola(0, vertice,data['p'], "{0}".format(data['eje_focal']))
            return parabola
        except Exception as ex:
            raise Exception(ex)

    def Vertice_Validate(self):
        return self.vertice.coord_x == 0 and self.vertice.coord_y == 0

    def Sign(self, n):
        if n <= 0:
            return "+"
        else:
            return ""

    def Foco(self):
        if self.eje_focal == "x":
            return Punto(self.vertice.id_punto, self.vertice.coord_x, self.vertice.coord_y + self.p)
        else:
            return Punto(self.vertice.id_punto, self.vertice.coord_x + self.p, self.vertice.coord_y)

    def Lado_Recto(self):
        return 4 * abs(self.p)

    def Ecuacion(self):
        if self.eje_focal == "y" and self.Vertice_Validate():
            return "y^2 = {0}x".format(str(Fraction(4 * self.p).limit_denominator()))
        elif self.eje_focal == "x" and self.Vertice_Validate():
            return "x^2 = {0}y".format(str(Fraction(4 * self.p).limit_denominator()))
        elif self.eje_focal == "y" and not self.Vertice_Validate():
            return "(y{0}{1})^2 = {2}(x{3}{4})".format(
                self.Sign(self.vertice.coord_y), self.vertice.coord_y * (-1), str(Fraction(4 * self.p).limit_denominator()),
                self.Sign(self.vertice.coord_x), self.vertice.coord_x * (-1))
        elif self.eje_focal == "x" and not self.Vertice_Validate():
            return "(x{0}{1})^2 = {2}(y{3}{4})".format(
                self.Sign(self.vertice.coord_x), self.vertice.coord_x * (-1), str(Fraction(4 * self.p).limit_denominator()),
                self.Sign(self.vertice.coord_y), self.vertice.coord_y * (-1))

    def Directriz(self):
        if self.eje_focal == "x":
            return "y = {0}".format(str(Fraction(self.vertice.coord_y - self.p).limit_denominator()))
        elif self.eje_focal == "y":
            return "x = {0}".format(str(Fraction(self.vertice.coord_x - self.p).limit_denominator()))

    def Eje_Simetria(self):
        if self.eje_focal == "x":
            return "x = {0}".format(self.vertice.coord_x)
        elif self.eje_focal == "y":
            return "y = {0}".format(self.vertice.coord_y)

    def Show_Parabola(self):
        return "Vertice: {0}\nEcuacion: {1}\nFoco: {2}\nLado Recto: {3}\nDirectriz: {4}\nEje de Simetria: {5}".format(
            self.vertice.Show_Point(), self.Ecuacion(),
            self.Foco().Show_Point(), self.Lado_Recto(), self.Directriz(),
            self.Eje_Simetria())


    def get_elements(self):
        return {
            "vertex": self.vertice.Show_Point(),
            "straight_side": self.Lado_Recto(),
            "focus": self.Foco().Show_Point(),
            "directrix": self.Directriz(),
            "simmetry_axis": self.Eje_Simetria(),
            "equation": self.Ecuacion()
        }


    def convert_to_json(self):
        return {
            "id_parabola": self.id_parabola,
            "vertice": self.vertice.convert_to_json(),
            "p": self.p,
            "eje_focal": self.eje_focal
        }

#05
class Elipse:

    def __init__(self, id_elipse, centro, a, b, eje_focal):
        self.id_elipse = id_elipse
        self.centro = centro
        self.eje_focal = eje_focal
        self.a = a
        self.b = b

    def Center_Validate(self):
        return self.centro.coord_x == 0 and self.centro.coord_y == 0

    def Validate_Ellipse(self):
        return self.a > self.b > 0

    def Sign(self, n):
        if n <= 0:
            return "+"
        else:
            return ""

    def convert_object_elipse(self, list):
        try:
            data = json.loads(list)[0]
            centro = Punto(0, 0, 0)
            centro = centro.convert_object_json(data['centro'])
            elipse = Elipse(data['elipse'].get('id_elipse'), centro, data['elipse'].get('a'), data['elipse'].get('b'), "{0}".format(data['elipse'].get('eje_focal')))
            return elipse
        except Exception as ex:
            raise Exception(ex)

    def convert_object_elipse_data(self, data):
        try:
            centro = Punto(0, 0, 0)
            centro = centro.convert_object_json_data(data)
            centro.id_punto = 0
            elipse = Elipse(0, centro, data['a'], data['b'], "{0}".format(data['eje_focal']))
            return elipse
        except Exception as ex:
            raise Exception(ex)

    def Equation(self):
        if self.eje_focal == "x" and self.Center_Validate(
        ) and self.Validate_Ellipse():
            return "x^2/{0} + y^2/{1} = 1".format(self.a * self.a,
                                                  self.b * self.b)
        elif self.eje_focal == "x" and not self.Center_Validate(
        ) and self.Validate_Ellipse():
            return "(x{0}{1})^2/{2} + (y{3}{4})^2/{5} = 1".format(
                self.Sign(self.centro.coord_x), self.centro.coord_x * (-1),
                                                self.a * self.a, self.Sign(self.centro.coord_y),
                                                self.centro.coord_y * (-1), self.b * self.b)
        elif self.eje_focal == "y" and self.Center_Validate(
        ) and self.Validate_Ellipse():
            return "x^2/{0} + y^2/{1} = 1".format(self.b * self.b,
                                                  self.a * self.a)
        elif self.eje_focal == "y" and not self.Center_Validate(
        ) and self.Validate_Ellipse():
            return "(x{0}{1})^2/{2} + (y{3}{4})^2/{5} = 1".format(
                self.Sign(self.centro.coord_x), self.centro.coord_x * (-1),
                                                self.b * self.b, self.Sign(self.centro.coord_y),
                                                self.centro.coord_y * (-1), self.a * self.a)
        else:
            return "Error, cumplir que a>b>0"

    def C(self):
        return round(math.sqrt(self.a * self.a - self.b * self.b), 2)

    def Foco_A(self):
        foco_a = Punto(self.centro.id_punto, self.centro.coord_x - self.C(), self.centro.coord_y)
        return foco_a

    def Foco_B(self):
        foco_b = Punto(self.centro.id_punto, self.centro.coord_x + self.C(), self.centro.coord_y)
        return foco_b

    def Verice_A(self):
        vertice_a = Punto(self.centro.id_punto, self.centro.coord_x - self.a, self.centro.coord_y)
        return vertice_a

    def Verice_B(self):
        vertice_b = Punto(self.centro.id_punto, self.centro.coord_x + self.a, self.centro.coord_y)
        return vertice_b

    def Intercepto_EjeNormal_A(self):
        a = Punto(self.centro.id_punto, self.centro.coord_x, self.centro.coord_y - self.b)
        return a

    def Intercepto_EjeNormal_B(self):
        b = Punto(self.centro.id_punto, self.centro.coord_x, self.centro.coord_y + self.b)
        return b

    def EjeMayor(self):
        return round(2 * self.a, 2)

    def EjeMenor(self):
        return round(2 * self.b, 2)

    def LadoRecto(self):
        return round((2 * self.b * self.b) / self.a, 2)

    def Exentrecidad(self):
        return round(self.C() / self.a, 2)

    def Show_Ellipse(self):
        return "Centro: {0}\nEcuacion: {1}\nFocos: F-1 {2} F-2 {3}\nVertices: V-1 {4} V-2 {5}\nInterceptos: B-1 {6} " \
               "B-2 {7}\nEje mayor: {8}\nEje Menor: {9}\nLado Recto: {10}".format(self.centro.Show_Point(),
                                                                                  self.Equation(),
                                                                                  self.Foco_A().Show_Point(),
                                                                                  self.Foco_B().Show_Point(),
                                                                                  self.Verice_A().Show_Point(),
                                                                                  self.Verice_B().Show_Point(),
                                                                                  self.Intercepto_EjeNormal_A().Show_Point(),
                                                                                  self.Intercepto_EjeNormal_B().Show_Point(),
                                                                                  self.EjeMayor(), self.EjeMenor(),
                                                                                  self.LadoRecto())


    def get_elements(self):
        return {
            "center": self.centro.Show_Point(),
            "equation": self.Equation(),
            "focus_a": self.Foco_A().Show_Point(),
            "focus_b": self.Foco_B().Show_Point(),
            "vertex_a": self.Verice_A().Show_Point(),
            "vertex_b": self.Verice_B().Show_Point(),
            "intercepto_a": self.Intercepto_EjeNormal_A().Show_Point(),
            "intercepto_b": self.Intercepto_EjeNormal_B().Show_Point(),
            "eje_mayor": self.EjeMayor(),
            "eje_menor": self.EjeMenor(),
            "lado_recto": self.LadoRecto(),
            "exentricidad": self.Exentrecidad()
        }


    def convert_to_json(self):
        return {
            "id_elipse": self.id_elipse,
            "centro": self.centro.convert_to_json(),
            "a": self.a,
            "b": self.b,
            "eje_focal": self.eje_focal
        }


#06
class Hiperbola:

    def __init__(self, id_hiperbola, centro, a, b, eje_focal) -> None:
        self.id_hiperbola = id_hiperbola
        self.centro = centro
        self.a = a
        self.b = b
        self.eje_focal = eje_focal

    def Vertice_A(self):
        if self.eje_focal == "x":
            vertice_a = Punto(self.centro.id_punto, self.centro.coord_x + self.a, self.centro.coord_y)
        elif self.eje_focal == "y":
            vertice_a = Punto(self.centro.id_punto, self.centro.coord_x, self.centro.coord_y + self.a)
        return vertice_a

    def Vertice_B(self):
        if self.eje_focal == "x":
            vertice_b = Punto(self.centro.id_punto, self.centro.coord_x - self.a, self.centro.coord_y)
        elif self.eje_focal == "y":
            vertice_b = Punto(self.centro.id_punto, self.centro.coord_x, self.centro.coord_y - self.a)
        return vertice_b

    def C(self):
        return round(math.sqrt(self.a * self.a + self.b * self.b), 2)

    def Foco_A(self):
        if self.eje_focal == "x":
            foco_a = Punto(self.centro.id_punto, self.centro.coord_x + self.C(), self.centro.coord_y)
        elif self.eje_focal == "y":
            foco_a = Punto(self.centro.id_punto, self.centro.coord_x, self.centro.coord_y + self.C())
        return foco_a

    def Foco_B(self):
        if self.eje_focal == "x":
            foco_b = Punto(self.centro.id_punto, self.centro.coord_x - self.C(), self.centro.coord_y)
        elif self.eje_focal == "y":
            foco_b = Punto(self.centro.id_punto, self.centro.coord_x, self.centro.coord_y - self.C())
        return foco_b

    def Conjugado_A(self):
        if self.eje_focal == "x":
            conjugado_a = Punto(self.centro.id_punto, self.centro.coord_x, self.centro.coord_y + self.b)
        elif self.eje_focal == "y":
            conjugado_a = Punto(self.centro.id_punto, self.centro.coord_x + self.b, self.centro.coord_y)
        return conjugado_a

    def Conjugado_B(self):
        if self.eje_focal == "x":
            conjugado_b = Punto(self.centro.id_punto, self.centro.coord_x, self.centro.coord_y - self.b)
        elif self.eje_focal == "y":
            conjugado_b = Punto(self.centro.id_punto, self.centro.coord_x - self.b, self.centro.coord_y)
        return conjugado_b

    def Sign(self, n):
        if n <= 0:
            return "+"
        else:
            return ""

    def Center_Validate(self):
        return self.centro.coord_x == 0 and self.centro.coord_y == 0

    def DivideBA_01(self):
        if self.eje_focal == "x":
            return str(Fraction(self.b/self.a).limit_denominator())
        elif self.eje_focal == "y":
            return str(Fraction(self.a/self.b).limit_denominator())

    def DivideBA_02(self):
        if self.eje_focal == "x":
            return str(Fraction((self.b/self.a)*(-1)).limit_denominator())
        elif self.eje_focal == "y":
            return str(Fraction((self.a/self.b)*(-1)).limit_denominator())

    def Asintota_A(self):
        if self.eje_focal == "x" and self.Center_Validate():
            return "y = {0}x".format(self.DivideBA_01())
        elif self.eje_focal == "x" and not self.Center_Validate():
            return "y{0}{1} = {2}(x{3}{4})".format(self.Sign(self.centro.coord_y),
                                                   self.centro.coord_y * (-1),
                                                   self.DivideBA_01(),
                                                   self.Sign(self.centro.coord_x),
                                                   self.centro.coord_x * (-1))
        elif self.eje_focal == "y" and self.Center_Validate():
            return "y = {0}x".format(self.DivideBA_01())
        elif self.eje_focal == "y" and not self.Center_Validate():
            return "y{0}{1} = {2}(x{3}{4})".format(self.Sign(self.centro.coord_y),
                                                   self.centro.coord_y * (-1),
                                                   self.DivideBA_01(),
                                                   self.Sign(self.centro.coord_x),
                                                   self.centro.coord_x * (-1))

    def Asintota_B(self):
        if self.eje_focal == "x" and self.Center_Validate():
            return "y = {0}x".format(self.DivideBA_02())
        elif self.eje_focal == "x" and not self.Center_Validate():
            return "y{0}{1} = {2}(x{3}{4})".format(self.Sign(self.centro.coord_y),
                                                   self.centro.coord_y * (-1),
                                                   self.DivideBA_02(),
                                                   self.Sign(self.centro.coord_x),
                                                   self.centro.coord_x * (-1))
        elif self.eje_focal == "y" and self.Center_Validate():
            return "y = {0}x".format(self.DivideBA_02())
        elif self.eje_focal == "y" and not self.Center_Validate():
            return "y{0}{1} = {2}(x{3}{4})".format(self.Sign(self.centro.coord_y),
                                                   self.centro.coord_y * (-1),
                                                   self.DivideBA_02(),
                                                   self.Sign(self.centro.coord_x),
                                                   self.centro.coord_x * (-1))

    def Ecuacion(self):
        if self.eje_focal == "x" and self.Center_Validate():
            return "x^2/{0} - y^2/{1} = 1".format(self.a * self.a,
                                                  self.b * self.b)
        elif self.eje_focal == "x" and not self.Center_Validate():
            return "(x{0}{1})^2/{2} - (y{3}{4})^2/{5} = 1".format(
                self.Sign(self.centro.coord_x), self.centro.coord_x * (-1),
                                                self.a * self.a, self.Sign(self.centro.coord_y),
                                                self.centro.coord_y * (-1), self.b * self.b)
        elif self.eje_focal == "y" and self.Center_Validate():
            return "y^2/{0} - x^2/{1} = 1".format(self.a * self.a,
                                                  self.b * self.b)
        elif self.eje_focal == "y" and not self.Center_Validate():
            return "(y{0}{1})^2/{2} - (x{3}{4})^2/{5} = 1".format(
                self.Sign(self.centro.coord_y), self.centro.coord_y * (-1),
                                                self.a * self.a, self.Sign(self.centro.coord_x),
                                                self.centro.coord_x * (-1), self.b * self.b)

    def EjeConjugado(self):
        if self.eje_focal == "x":
            return abs(self.Conjugado_B().coord_y - self.Conjugado_A().coord_y)
        elif self.eje_focal == "y":
            return abs(self.Conjugado_B().coord_x - self.Conjugado_A().coord_x)

    def EjeFocal(self):
        if self.eje_focal == "x":
            return "x = {0}".format(self.centro.coord_y)
        elif self.eje_focal == "y":
            return "y = {0}".format(self.centro.coord_x)

    def EjeNormal(self):
        if self.eje_focal == "x":
            return "y = {0}".format(self.centro.coord_x)
        elif self.eje_focal == "y":
            return "x = {0}".format(self.centro.coord_y)

    def Exentricidad(self):
        return round(self.C() / self.a, 2)

    def ShowHiperbola(self):
        return "Centro: {0}\nVertices: V-1 {1} V-2 {2}\nFocos: F-1 {3} F-2 {4}\nExt Eje Conjugado: E-1 {5} E-2 {6}" \
               "\nLongitud Eje Conjugado: {7}\nEje Focal: {8}\nEje Normal: {9}\nExcentricidad: {10}\n" \
               "Ecuaciones de la Asintotas: \nECA-1: {11}\nECA-2: {12}\nEcuacion Canonica: {13}".format(self.centro.Show_Point(),self.Vertice_A().Show_Point(), self.Vertice_B().Show_Point(),self.Foco_A().Show_Point(),
                                                                                                        self.Foco_B().Show_Point(), self.Conjugado_A().Show_Point(),self.Conjugado_B().Show_Point(),
                                                                                                        self.EjeConjugado(),self.EjeFocal(),self.EjeNormal(),self.Exentricidad(),self.Asintota_A(),
                                                                                                        self.Asintota_B(),self.Ecuacion())

    def convert_object_hiperbola_data(self, data):
        try:
            centro = Punto(0, 0, 0)
            centro = centro.convert_object_json_data(data)
            centro.id_punto = 0
            hiperbola = Hiperbola(0, centro, data['a'], data['b'], "{0}".format(data['eje_focal']))
            return hiperbola
        except Exception as ex:
            raise Exception(ex)

    def convert_object_hiperbola(self, list):
        try:
            data = json.loads(list)[0]
            centro = Punto(0, 0, 0)
            centro = centro.convert_object_json(data['centro'])
            hiperbola = Hiperbola(data['hiperbola'].get('id_hiperbola'), centro, data['hiperbola'].get('a'), data['hiperbola'].get('b'), "{0}".format(data['hiperbola'].get('eje_focal')))
            return hiperbola
        except Exception as ex:
            raise Exception(ex)

    def get_elements(self):
        return {
            "centro": self.centro.Show_Point(),
            "ecuacion": self.Ecuacion(),
            "foco_a: ": self.Foco_A().Show_Point(),
            "foco_b: ": self.Foco_B().Show_Point(),
            "vertice_a": self.Vertice_A().Show_Point(),
            "vertice_b": self.Vertice_B().Show_Point(),
            "intercepto_a": self.Conjugado_A().Show_Point(),
            "intercepto_b": self.Conjugado_B().Show_Point(),
            "eje_focal": self.EjeFocal(),
            "Longitud_eje_conjugado": self.EjeConjugado(),
            "eje_normal": self.EjeNormal(),
            "excentricidad": self.Exentricidad(),
            "asintota_a": self.Asintota_A(),
            "asintota_b": self.Asintota_B()
        }


    def convert_to_json(self):
        return {
            "id_hiperbola": self.id_hiperbola,
            "centro": self.centro.convert_to_json(),
            "a": self.a,
            "b": self.b,
            "eje_focal": self.eje_focal
        }


pointa = Punto(1, 0, 0)
eje_focal = "y"
h = Hiperbola(1, pointa, -1, 2, eje_focal)

print(h.ShowHiperbola())
print("\n")
pointb = Punto(2, 7, 5)

center = Punto(3, 2, -1)
c = Circunferencia(1, pointa, 2)
print(c.Show_Circunference())
print("\n")
l = Recta(1, pointa, pointb)
print(l.ShowLine())
print("\n")
ellipse = Elipse(1, center, 10, 6, "y")
print(ellipse.Show_Ellipse())
print("\n")
v = Punto(4, 1, 3)
p = Parabola(1, v, 9 / 4, "y")
print(p.Show_Parabola())


print(l.convert_to_json())

