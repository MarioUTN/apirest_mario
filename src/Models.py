# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 11:28:03 2022

@author: Mario
"""

import connectdb as conn
import Entities as entities
import json

connection = conn.get_connection()

class Model:


    @classmethod
    def get_points(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute("declare @points nvarchar(max) set @points = ( select p.id_punto, p.coord_x, p.coord_y from punto p for json auto ) select @points as points return")
            result = cursor.fetchone()
            connection.close()
            return result
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_lines(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute("declare @lines nvarchar(max) set @lines = (select r.id_recta as 'recta.id_recta', pa.id_punto as 'punto_a.id_punto', pa.coord_x as 'punto_a.coord_x', pa.coord_y as 'punto_a.coord_y', pb.id_punto 'punto_b.id_punto', pb.coord_x as 'punto_b.coord_x', pb.coord_y as 'punto_b.coord_y'from punto pa, recta r, punto pb where r.punto_a = pa.id_punto and r.punto_b = pb.id_punto for json path) select @lines as lines return")
            result = cursor.fetchone()
            connection.close()
            return result
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_circunferences(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute("declare @circunferences nvarchar(max) set @circunferences = (select c.id_circunferencia as 'circunferencia.id_circunferencia', p.id_punto as 'centro.id_punto', p.coord_x as 'centro.coord_x', p.coord_y as 'centro.coord_y' from circunferencia c inner join punto p on c.centro = p.id_punto for json path) select @circunferences as circunferences return")
            result = cursor.fetchone()
            connection.close()
            return result
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_elipses(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute("declare @elipses nvarchar(max) set @elipses = (select e.id_elipse as 'elipse.id_elipse', e.a as 'elipse.a', e.b as 'elipse.b', e.eje_focal as 'elipse.eje_focal', p.id_punto as 'centro.id_punto', p.coord_x as 'centro.coord_x', p.coord_y as 'centro.coord_y' from elipse e inner join punto p on e.centro = p.id_punto for json path) select @elipses as elipses return")
            result = cursor.fetchone()
            connection.close()
            return result
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_hiperbolas(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute("declare @hiperbolas nvarchar(max) set @hiperbolas = (select h.id_hiperbola as 'hiperbola.id_hiperbola', h.a as 'hiperbola.a', h.b as 'hiperbola.b', h.eje_focal as 'hiperbola.eje_focal', p.id_punto as 'centro.id_punto', p.coord_x as 'centro.coord_x', p.coord_y as 'centro.coord_y' from hiperbola h inner join punto p on h.centro = p.id_punto for json path) select @hiperbolas as hiperbolas return")
            result = cursor.fetchone()
            connection.close()
            return result
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_parabolas(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute("declare @parabolas nvarchar(max) set @parabolas = (select p.id_parabola as 'parabola.id_parabola', p.p as 'parabola.p', p.eje_focal as 'parabola.eje_focal', v.id_punto as 'vertice.id_punto', v.coord_x as 'vertice.coord_x', v.coord_y as 'vertice.coord_y' from parabola p inner join punto v on p.vertice = v.id_punto for json path) select @parabolas as parabolas return")
            result = cursor.fetchone()
            connection.close()
            return result
        except Exception as ex:
            raise Exception(ex)


# GET BY ID


    @classmethod
    def get_point_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute("select p.id_punto, p.coord_x, p.coord_y from punto p where p.id_punto= {0} for json path;".format(id))
            result = cursor.fetchone()
            connection.close()
            return result
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_line_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute("select r.id_recta as 'recta.id_recta', pa.id_punto as 'punto_a.id_punto', pa.coord_x as 'punto_a.coord_x', pa.coord_y as 'punto_a.coord_y', pb.id_punto 'punto_b.id_punto', pb.coord_x as 'punto_b.coord_x', pb.coord_y as 'punto_b.coord_y' from punto pa, recta r, punto pb where r.punto_a = pa.id_punto and r.punto_b = pb.id_punto and r.id_recta = {0} for json path;".format(id))
            result = cursor.fetchone()
            connection.close()
            return result
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_circunference_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute("select c.id_circunferencia as 'circunferencia.id_circunferencia', c.radio as 'circunferencia.radio', p.id_punto as 'centro.id_punto', p.coord_x as 'centro.coord_x', p.coord_y as 'centro.coord_y' from circunferencia c inner join punto p on c.centro = p.id_punto and c.id_circunferencia = {0} for json path;".format(id))
            result = cursor.fetchone()
            connection.close()
            return result
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_elipse_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute("select e.id_elipse as 'elipse.id_elipse', e.a as 'elipse.a', e.b as 'elipse.b', e.eje_focal as 'elipse.eje_focal', p.id_punto as 'centro.id_punto', p.coord_x as 'centro.coord_x', p.coord_y as 'centro.coord_y' from elipse e inner join punto p on e.centro = p.id_punto and e.id_elipse = {0} for json path;".format(id))
            result = cursor.fetchone()
            connection.close()
            return result
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_hiperbola_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute("select h.id_hiperbola as 'hiperbola.id_hiperbola', h.a as 'hiperbola.a', h.b as 'hiperbola.b', h.eje_focal as 'hiperbola.eje_focal', p.id_punto as 'centro.id_punto', p.coord_x as 'centro.coord_x', p.coord_y as 'centro.coord_y' from hiperbola h inner join punto p on h.centro = p.id_punto and h.id_hiperbola = {0} for json path;".format(id))
            result = cursor.fetchone()
            connection.close()
            return result
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_parabola_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute("select p.id_parabola as 'parabola.id_parabola', p.p as 'parabola.p', p.eje_focal as 'parabola.eje_focal', v.id_punto as 'vertice.id_punto', v.coord_x as 'vertice.coord_x', v.coord_y as 'vertice.coord_y' from parabola p inner join punto v on p.vertice = v.id_punto and p.id_parabola = {0} for json path;".format(id))
            result = cursor.fetchone()
            connection.close()
            return result
        except Exception as ex:
            raise Exception(ex)



    @classmethod
    def create_point(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO punto(coord_x, coord_y) values({0}, {1})".format(data['coord_x'], data['coord_y']))
                id_point = cursor.execute("SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    point = entities.Punto(id_point, data['coord_x'], data['coord_y'])
                    return point.convert_to_json()
                else:
                    return {'message': 'Error, Insert failed!'}
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def create_line(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO punto(coord_x, coord_y) values({0}, {1})".format(data['coord_xa'], data['coord_ya']))
                id_point_a = cursor.execute("SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                cursor.execute("INSERT INTO punto(coord_x, coord_y) values({0}, {1})".format(data['coord_xb'], data['coord_yb']))
                id_point_b = cursor.execute("SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                cursor.execute("INSERT INTO recta(punto_a, punto_b) values({0}, {1})".format(id_point_a, id_point_b))
                id_line = cursor.execute("SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    a = entities.Punto(id_point_a, data['coord_xa'], data['coord_ya'])
                    b = entities.Punto(id_point_b, data['coord_xb'], data['coord_yb'])
                    line = entities.Recta(id_line, a, b)
                    return line.convert_to_json()
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def create_circunference(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO punto(coord_x, coord_y) values({0}, {1})".format(data['coord_x'], data['coord_y']))
                id_point = cursor.execute("SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                cursor.execute("INSERT INTO circunferencia(centro, radio) values({0}, {1})".format(id_point, data['radio']))
                id_circunference = cursor.execute("SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    a = entities.Punto(id_point, data['coord_x'], data['coord_y'])
                    circunference = entities.Circunferencia(id_circunference, a, data['radio'])
                    return circunference.convert_to_json()
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)



    @classmethod
    def create_parabola(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO punto(coord_x, coord_y) values({0}, {1})".format(data['coord_x'], data['coord_y']))
                id_point = cursor.execute("SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                cursor.execute("INSERT INTO parabola(vertice, p, eje_focal) values({0}, {1}, '{2}')".format(id_point, data['p'], data['eje_focal']))
                id_parabola = cursor.execute("SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    a = entities.Punto(id_point, data['coord_x'], data['coord_y'])
                    parabola = entities.Parabola(id_parabola, a, "{0}".format(data['p']), "{0}".format(data['eje_focal']))
                    return parabola.convert_to_json()
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def create_elipse(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO punto(coord_x, coord_y) values({0}, {1})".format(data['coord_x'], data['coord_y']))
                id_point = cursor.execute("SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                cursor.execute("INSERT INTO elipse(centro, a,  b, eje_focal) values({0}, {1}, {2}, '{3}')".format(id_point, data['a'], data['b'], data['eje_focal']))
                id_elipse = cursor.execute("SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    a = entities.Punto(id_point, data['coord_x'], data['coord_y'])
                    elipse = entities.Elipse(id_elipse, a, data['a'], data['b'], "{0}".format(data['eje_focal']))
                    return elipse.convert_to_json()
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def create_hiperbola(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO punto(coord_x, coord_y) values({0}, {1})".format(data['coord_x'], data['coord_y']))
                id_point = cursor.execute("SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                cursor.execute("INSERT INTO hiperbola(centro, a,  b, eje_focal) values({0}, {1}, {2}, '{3}')".format(id_point, data['a'], data['b'], data['eje_focal']))
                id_hiperbola = cursor.execute("SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    a = entities.Punto(id_point, data['coord_x'], data['coord_y'])
                    hiperbola = entities.Hiperbola(id_hiperbola, a, data['a'], data['b'], "{0}".format(data['eje_focal']))
                    return hiperbola.convert_to_json()
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)


# UPDATE METHODS
    @classmethod
    def update_point(self,id_punto, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE punto SET coord_x = {0}, coord_y = {1} WHERE id_punto = {2}".format(data['coord_x'], data['coord_y'], id_punto))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    point = entities.Punto(id_punto, data['coord_x'], data['coord_y'])
                    return point
                else:
                    return {'message': 'Error, Update failed!'}
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def update_line(self,id_line, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO punto(coord_x, coord_y) values({0}, {1})".format(data['coord_xa'], data['coord_ya']))
                id_point_a = cursor.execute("SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                cursor.execute("INSERT INTO punto(coord_x, coord_y) values({0}, {1})".format(data['coord_xb'], data['coord_yb']))
                id_point_b = cursor.execute("SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                cursor.execute("UPDATE recta SET punto_a = {0}, punto_b = {1} WHERE id_recta = {2}".format(id_point_a, id_point_b, id_line))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    a = entities.Punto(id_point_a, data['coord_xa'], data['coord_ya'])
                    b = entities.Punto(id_point_a, data['coord_xb'], data['coord_yb'])
                    line = entities.Recta(id_line, a, b)
                    return line
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def update_circunference(self,id_circunferencia, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO punto(coord_x, coord_y) values({0}, {1})".format(data['coord_x'], data['coord_y']))
                id_point = cursor.execute("SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                cursor.execute("UPDATE circunferencia SET centro = {0}, radio = {1} WHERE id_circunferencia = {2}".format(id_point, data['radio'], id_circunferencia))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    a = entities.Punto(id_point, data['coord_x'], data['coord_y'])
                    circunference = entities.Circunferencia(id_circunferencia, a, data['radio'])
                    return circunference
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def update_parabola(self,id_parabola, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO punto(coord_x, coord_y) values({0}, {1})".format(data['coord_x'], data['coord_y']))
                id_point = cursor.execute("SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                cursor.execute("UPDATE parabola SET vertice = {0}, p = {1}, eje_focal = '{2}' WHERE id_parabola = {3}".format(id_point, data['p'], data['eje_focal'], id_parabola))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    a = entities.Punto(id_point, data['coord_x'], data['coord_y'])
                    parabola = entities.Parabola(id_parabola, a, data['p'],"{0}".format(data['eje_focal']))
                    return parabola
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def update_elipse(self,id_elipse, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO punto(coord_x, coord_y) values({0}, {1})".format(data['coord_x'], data['coord_y']))
                id_point = cursor.execute("SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                cursor.execute("UPDATE elipse SET centro = {0}, a = {1}, b = {2}, eje_focal = '{3}' WHERE id_elipse = {4}".format(id_point, data['a'], data['b'], data['eje_focal'], id_elipse))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    a = entities.Punto(id_point, data['coord_x'], data['coord_y'])
                    elipse = entities.Elipse(id_elipse, a, data['a'], data['b'], "{0}".format(data['eje_focal']))
                    return elipse
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def update_hiperbola(self,id_hiperbola, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO punto(coord_x, coord_y) values({0}, {1})".format(data['coord_x'], data['coord_y']))
                id_point = cursor.execute("SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                cursor.execute("UPDATE hiperbola SET centro = {0}, a = {1}, b = {2}, eje_focal = '{3}' WHERE id_hiperbola = {4}".format(id_point, data['a'], data['b'], data['eje_focal'], id_hiperbola))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    a = entities.Punto(id_point, data['coord_x'], data['coord_y'])
                    hiperbola = entities.Elipse(id_hiperbola, a, data['a'], data['b'], "{0}".format(data['eje_focal']))
                    return hiperbola
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def delete_point(self,id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM punto WHERE id_punto = {0}".format(id))
                row_affects = cursor.rowcount
                connection.commit()
                if row_affects > 0:
                    return {'message': 'Point deleted successfully!'}
                else:
                    return {'message': 'Error, Delete point failed, point not found!'}
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def delete_line(self,id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM recta WHERE id_recta = {0}".format(id))
                row_affects = cursor.rowcount
                print(row_affects)
                connection.commit()
                if row_affects > 0:
                    return {'message': 'Line deleted successfully!'}
                else:
                    return {'message': 'Error, Delete line failed, line not found!'}
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def delete_circunference(self,id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM circunferencia WHERE id_circunferencia = {0}".format(id))
                row_affects = cursor.rowcount
                print(row_affects)
                connection.commit()
                if row_affects > 0:
                    return {'message': 'Circunference deleted successfully!'}
                else:
                    return {'message': 'Error, Delete Circunference failed, Circunference not found!'}
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def delete_parabola(self,id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM parabola WHERE id_parabola = {0}".format(id))
                row_affects = cursor.rowcount
                print(row_affects)
                connection.commit()
                if row_affects > 0:
                    return {'message': 'Parabola deleted successfully!'}
                else:
                    return {'message': 'Error, Delete parabola failed, parabola not found!'}
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def delete_elipse(self,id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM elipse WHERE id_elipse = {0}".format(id))
                row_affects = cursor.rowcount
                print(row_affects)
                connection.commit()
                if row_affects > 0:
                    return {'message': 'Elipse deleted successfully!'}
                else:
                    return {'message': 'Error, Delete elipse failed, elipse not found!'}
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def delete_hiperbola(self,id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM hiperbola WHERE id_hiperbola = {0}".format(id))
                row_affects = cursor.rowcount
                print(row_affects)
                connection.commit()
                if row_affects > 0:
                    return {'message': 'Hiperbola deleted successfully!'}
                else:
                    return {'message': 'Error, Delete hiperbola failed, hiperbola not found!'}
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_elements_line_byid(self, id):
        try:
            data = self.get_line_byid(id)
            if data is not None:  
                line = entities.Recta(0, 0, 0)
                line = line.convert_line(data[0])
                return line
            else:
                return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_elements_circunference_byid(self, id):
        try:
            data = self.get_circunference_byid(id)
            if data is not None:  
                circunference = entities.Circunferencia(0, 0, 0)
                circunference = circunference.convert_object_circunference(data[0])
                return circunference
            else:
                return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_elements_parabola_byid(self, id):
        try:
            data = self.get_parabola_byid(id)
            if data is not None:  
                parabola = entities.Parabola(0, 0, 0, "y")
                parabola = parabola.convert_object_parabola(data[0])
                return parabola
            else:
                return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_elements_elipse_byid(self, id):
        try:
            data = self.get_elipse_byid(id)
            if data is not None:  
                elipse = entities.Elipse(0, 0, 0, 0, "y")
                elipse = elipse.convert_object_elipse(data[0])
                return elipse
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_elements_hiperbola_byid(self, id):
        try:
            data = self.get_hiperbola_byid(id)
            print(data)
            if data is not None:  
                hiperbola = entities.Hiperbola(0, 0, 0, 0, "y")
                hiperbola = hiperbola.convert_object_hiperbola(data[0])
                return hiperbola
            else:
                return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_elements_line(self, data):
        try:
            if data is not None:  
                line = entities.Recta(0, 0, 0)
                line = line.convert_line_data(data)
                return line
            else:
                return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_elements_circunference(self, data):
        try:
            if data is not None:  
                circunference = entities.Circunferencia(0, 0, 0)
                circunference = circunference.convert_object_circunference_data(data)
                return circunference
            else:
                return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_elements_parabola(self, data):
        try:
            if data is not None:  
                parabola = entities.Parabola(0, 0, 0, "y")
                parabola = parabola.convert_object_parabola_data(data)
                return parabola
            else:
                return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_elements_elipse(self, data):
        try:
            if data is not None:  
                elipse = entities.Elipse(0, 0, 0, 0, "y")
                elipse = elipse.convert_object_elipse_data(data)
                return elipse
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_elements_hiperbola(self, data):
        try:
            if data is not None:  
                hiperbola = entities.Hiperbola(0, 0, 0, 0, "y")
                hiperbola = hiperbola.convert_object_hiperbola_data(data)
                return hiperbola
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
