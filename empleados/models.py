from django.db import models
from login.models import Municipio, Departamento, User
from django.core.validators import MaxValueValidator, MinValueValidator
# create your models here.

class Persona(models.Model):

    tipoId = [
        ("CC", 'Cédula de ciudadanía'),
        ("TI", 'Tarjeta de identidad'),
        ("CE", 'Cédula de extranjería'),
        ("PA", 'Pasaporte'),
        ("RC", 'Registro Civil'),
        ("TE", 'Tarjeta de Extranjería'),
        ("DIE", 'Documento de identificación extranjero'),
        ("PEP", 'PEP'),
        ("NUIP", 'NUIP'),
        ("NIT", 'NIT'),
    ]


    Per_codigo = models.AutoField(primary_key = True)
    Per_tipoId = models.CharField(max_length = 38, choices = tipoId, verbose_name='Tipo de identificacion')
    Per_id = models.CharField(max_length = 50, verbose_name='Identificacion')
    Per_nombre = models.CharField(max_length = 50, verbose_name='Nombre')
    Per_apellido = models.CharField(max_length = 50, verbose_name='Apellido')
    Per_correo = models.EmailField(max_length = 50, verbose_name='Correo', unique=True)
    Per_telefono = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)], verbose_name='Telefono')
    # Mun_nombre = models.ForeignKey(Municipio, verbose_name="Municipio", on_delete=models.CASCADE)

    class Meta:
        db_table = "Persona"
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self) -> str:
        return self.Per_nombre
    
class Empleado(models.Model):

    tipoContrato = [
        (1, 'Término Fijo'),
        (2, 'Término Indefinido'),
        (3, 'Obra o Labor'),
        (4, 'Aprendizaje'),
        (5, 'Prácticas o Pasantías'),
    ]

    tipoTrabajador = [
        (1, 'Dependiente'),
        (2, 'Servicio doméstico'),
        (3, 'Madre comunitaria'),
        (4, 'Aprendices del Sena en etapa lectiva'),
        (5, 'Funcionarios públicos sin tope máximo de IBC'),
        (6, 'Aprendices del SENA en etapa productiva'),
        (7, 'Estudiantes de postgrado en salud'),
        (8, 'Profesor de establecimiento particular'),
        (9, 'Estudiantes aportes solo riesgos laborales'),
        (10, 'Dependiente entidades o universidades públicas con régimen especial en salud'),
        (11, 'Cooperados o pre cooperativas de trabajo asociado'),
        (12, 'Trabajador dependiente de entidad beneficiaria del sistema general de participaciones - aportes patronales'),
        (13, 'Trabajador de tiempo parcial'),
        (14, 'Pre pensionado con aporte voluntario a salud'),
        (15, 'Pre pensionado de entidad en liquidación'),
        (16, 'Estudiantes de prácticas laborales en el sector público'),
    ]

    frecuenciaPago = [
        (1, 'Quincenal'),
        (2, 'Mensual'),
    ]

    subtipoTrabajador = [
        (1, 'Dependiente pensionado por vejez activo'),
    ]

    nivelDeRiesgo = [
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
        (5, 'V'),
    ]

    area = [
        (1, 'Administrativa'),
        (2, 'Operativa'),
        (3, 'Comercial'),
    ]

    metodoPago = [
    (1, 'Efectivo'),
    (2, 'Transferencia débito'),
    (3, 'Cheque'),
    (4, 'Consignación bancaria'),
    (5, 'Bonos'),
    (6, 'Instrumento no definido'),
    (7, 'Crédito ACH'),
    (8, 'Débito ACH'),
    (9, 'Reversión débito de demanda ACH'),
    (10, 'Reversión crédito de demanda ACH'),
    (11, 'Crédito de demanda ACH'),
    (12, 'Débito de demanda ACH'),
    (13, 'Mantener'),
    (14, 'Clearing nacional o regional'),
    (15, 'Reversión crédito ahorro'),
    (16, 'Reversión débito ahorro'),
    (17, 'Crédito ahorro'),
    (18, 'Débito ahorro'),
    (19, 'Bookentry crédito'),
    (20, 'Bookentry débito'),
    (21, 'Concentración de la demanda en efectivo/Desembolso crédito (CCD)'),
    (22, 'Concentración de la demanda en efectivo /Desembolso (CCD) débito'),
    (23, 'Crédito pago negocio corporativo (CTP)'),
    (24, 'Poyecto bancario'),
    (25, 'Proyecto bancario certificado'),
    (26, 'Cheque bancario'),
    (27, 'Nota cambiaria esperando aceptación'),
    (28, 'Cheque certificado'),
    (29, 'Cheque local'),
    (30, 'Débito Pago Negocio Corporativo (CTP)'),
    (31, 'Crédito Negocio Intercambio Corporativo (CTX)'),
    (32, 'Débito Negocio Intercambio Corporativo (CTX)'),
    (33, 'Transferencia crédito'),
    (34, 'Concentración efectivo / Desembolso crédito plus (CCD+)'),
    (35, 'Concentración efectivo / Desembolso débito plus (CCD+)'),
    (36, 'Pago y depósito pre acordado (PPD)'),
    (37, 'Concentración efectivo ahorros / Desembolso crédito (CCD)'),
    (38, 'Concentración efectivo ahorros / Desembolso crédito (CCD)'),
    (39, 'Pago negocio corporativo ahorros crédito (CTP)'),
    (40, 'Pago negocio corporativo ahorros débito (CTP)'),
    (41, 'Crédito negocio intercambio corporativo (CTX)'),
    (42, 'Débito negocio intercambio corporativo (CTX)'),
    (43, 'Concentración efectivo/Desembolso crédito plus (CCD+)'),
    (44, 'Concentración efectivo / Desembolso débito plus (CCD+)'),
    (45, 'Nota cambiaria'),
    (46, 'Transferencia crédito bancario'),
    (47, 'Transferencia débito interbancario'),
    (48, 'Transferencia débito bancaria'),
    (49, 'Tarjeta crédito'),
    (50, 'Tarjeta débito'),
    (51, 'Postgiro'),
    (52, 'Telex estándar bancario francés'),
    (53, 'Pago comercial urgente'),
    (54, 'Pago tesorería urgente'),
    (55, 'Nota promisoria'),
    (56, 'Nota promisoria firmada por el acreedor'),
    (57, 'Nota promisoria firmada por el acreedor, avalada por el banco'),
    (58, 'Nota promisoria firmada por el acreedor, avalada por un tercero'),
    (59, 'Nota promisoria firmada por el banco'),
    (60, 'Nota promisoria firmada por un banco avalada por otro banco'),
    (61, 'Nota promisoria firmada'),
    (62, 'Nota promisoria firmada por un tercero avalada por un banco'),
    (63, 'Retiro de nota por el acreedor'),
    (64, 'Vales'),
    (65, 'Retiro de nota por el acreedor sobre un banco'),
    (66, 'Retiro de nota por el acreedor, avalada por otro banco'),
    (67, 'Retiro de nota por el acreedor, sobre un banco avalada por un tercero'),
    (68, 'Retiro de una nota por el acreedor sobre un tercero'),
    (69, 'Retiro de una nota por el acreedor sobre un tercero avalada por un banco'),
    (70, 'Nota bancaria transferible'),
    (71, 'Cheque local transferible'),
    (72, 'Giro referenciado'),
    (73, 'Giro urgente'),
    (74, 'Giro formato abierto'),
    (75, 'Método de pago solicitado no usado'),
    (76, 'Clearing entre partners'),
    (77, 'Acuerdo mutuo'),
    (78, 'Cuentas de Ahorro de Trámite Simplificado (CATS) (Nequi, Daviplata, etc)')
    ]

    eps = [
    (1, 'ESSC24-COOSALUD ESS EPS-S'),
    (2, 'EPS037-NUEVA EPS S.A - NUEVA EMPRESA PROMOTORA DE SALUD NUEVA EPS S.A'),
    (3, 'ESSC07-EPS-S MUTUAL SER'),
    (4, 'EPS001-COLMÉDICA EPS - ALIANSALUD DESDE EL 01/01/2011'),
    (5, 'EPS002-SALUD TOTAL S.A. ENTIDAD PROMOTORA DE SALUD'),
    (6, 'EPS005-ENTIDAD PROMOTORA DE SALUD SANITAS S.A.'),
    (7, 'EPS010-EPS-SURA'),
    (8, 'EPS017-ENTIDAD PROMOTORA DE SALUD FAMISANAR LIMITADA CAFAM-COLSUBSIDIO'),
    (9, 'EPS018-ENTIDAD PROMOTORA DE SALUD SERVICIO OCCIDENTAL DE SALUD S.A. S.O.S.'),
    (10, 'EPS046-SALUD MIA EPS'),
    (11, 'EPS012-COMFENALCO VALLE E.P.S.'),
    (12, 'EPS008-COMPENSAR ENTIDAD PROMOTORA DE SALUD'),
    (13, 'EPM - Empresas públicas de Medellín'),
    (14, 'Fondo de pasivo social de ferrocarriles nacionales de Colombia'),
    (15, 'CCFC55-EPS-S CAJACOPI'),
    (16, 'EPSC25-CAPRESOCA EPS'),
    (17, 'Comfachoco'),
    (18, 'CCFC23-EPS-CCFC COM GUAJIRA'),
    (19, 'CCFC50-EPS-S COMFAORIENTE'),
    (20, 'EPS Familiar de Colombia (Antes ComfaSucre)'),
    (21, 'ESSC62-ASMET SALUD EPS SAS'),
    (22, 'ESSC91-ENTIDAD COOPERATIVA SOLIDARIA "ECOOPSOS"'),
    (23, 'ESSC18-CMRC RECAUDO FOSYGA-EMSSANAR E.S.S'),
    (24, 'EPSC34-RECAUDO FOSYGA CAPITAL SALUD'),
    (25, 'EPS040-ALIANZA MEDELLIN ANTIOQUIA EPS SAS (SAVIA SALUD)'),
    (26, 'EPSIC1-DUSAKAWI EPS'),
    (27, 'EPSIC3-ASOCIACION INDIGENA DEL CAUDA "A.I.C"'),
    (28, 'EPSIC4-ANAS WAYUU E P S I FOSYGA'),
    (29, 'EPSIC5-ENTIDAD PROMOTORA DE SALUD MALLAMAS'),
    (30, 'EPSIC6-ENTIDAD PROMOTORA DE SALUD PIJAOSALUD E'),
    (31, 'ESSC02-EMP MUTUAL PARA EL DESAR ENDISALUD ESS'),
    (32, 'EPS042-COOSALUD EPS S.A.'),
    (33, 'EPS041-NUEVA EPS S.A.'),
    (34, 'FMS001-FUERZAS MILITARES'),
    (35, 'POL001-POLICIA NACIONAL'),
    (36, 'RES002-ECOPETROL'),
    (37, 'RES004-MAGISTERIO'),
    (38, 'RES005-UNIVERSIDAD DEL ATLANTICO'),
    (39, 'RES006-UNIVERSIDAD INDUSTRIAL DE SANTANDER'),
    (40, 'RES007-UNIVERSIDAD DEL VALLE'),
    (41, 'RES008-UNIVERSIDAD NACIONAL DE COLOMBIA'),
    (42, 'RES009-UNIVERSIDAD DEL CAUCA'),
    (43, 'RES010-UNIVERSIDAD DE CARTAGENA'),
    (44, 'RES011-UNIVERSIDAD DE ANTIOQUIA'),
    (45, 'RES012-UNIVERSIDAD DE CORDOBA'),
    (46, 'RES013-UNIVERSIDAD DE NARIÑO'),
    (47, 'RES014-UNIVERSIDAD PEDAGOGICA Y TECNOLOGICA DE COLOMBIA - UPT')
    ]

    cajas_compensacion = [
    (1, 'CCF02-CAJA DE COMPENSACIÓN FAMILIAR CAMACOL COMFAMILIAR CAMACOL'),
    (2, 'CCF03-CAJA DE COMPENSACIÓN FAMILIAR COMFENALCO ANTIOQUIA'),
    (3, 'CCF04-CAJA DE COMPENSACIÓN FAMILIAR DE ANTIOQUIA COMFAMA'),
    (4, 'CCF05-CAJA DE COMPENSACIÓN FAMILIAR CAJACOPI ATLANTICO'),
    (5, 'CCF06-CAJA DE COMPENSACIÓN FAMILIAR DE BARRANQUILLA COMBARRANQUILLA'),
    (6, 'CCF07-CAJA DE COMPENSACIÓN FAMILIAR COMFAMILIAR DEL ATLANTICO'),
    (7, 'CCF08-CAJA DE COMPENSACIÓN FAMILIAR DE FENALCO - ANDI COMFENALCO CARTAGENA'),
    (8, 'CCF09-CAJA DE COMPENSACIÓN FAMILIAR DE CARTAGENA'),
    (9, 'CCF10-CAJA DE COMPENSACIÓN FAMILIAR DE BOYACA - COMFABOY'),
    (10, 'CCF11-CAJA DE COMPENSACIÓN FAMILIAR DE CALDAS'),
    (11, 'CCF13-CAJA DE COMPENSACIÓN FAMILIAR DEL CAQUETÁ - COMFACA'),
    (12, 'CCF14-CAJA DE COMPENSACIÓN FAMILIAR DEL CAUCA - COMFACAUCA'),
    (13, 'CCF15-COMFACESAR'),
    (14, 'CCF16-CAJA DE COMPENSACIÓN FAMILIAR DE CORDOBA COMFACOR'),
    (15, 'CCF21-CAJA DE COMPENSACIÓN FAMILIAR CAFAM'),
    (16, 'CCF22-CAJA COLOMBIANA DE SUBSIDIO FAMILIAR COLSUBSIDIO'),
    (17, 'CCF24-CAJA DE COMPENSACIÓN FAMILIAR COMPENSAR'),
    (18, 'CCF26-CAJA DE COMPENSACIÓN FAMILIAR DE CUNDINAMARCA - COMFACUNDI'),
    (19, 'CCF29-CAJA DE COMPENSACIÓN FAMILIAR DEL CHOCÓ'),
    (20, 'CCF30-CAJA DE COMPENSACIÓN FAMILIAR DE LA GUAJIRA'),
    (21, 'CCF32-CAJA DE COMPENSACIÓN FAMILIAR DEL HUILA - COMFAMILIAR'),
    (22, 'CCF33-CAJA DE COMPENSACIÓN FAMILIAR DEL MAGDALENA'),
    (23, 'CCF34-CAJA DE COMPENSACIÓN FAMILIAR REGIONAL DEL META COFREM'),
    (24, 'CCF35-CAJA DE COMPENSACIÓN FAMILIAR DE NARIÑO'),
    (25, 'CCF36-CAJA DE COMPENSACIÓN FAMILIAR DEL ORIENTE COLOMBIANO COMFAORIENTE'),
    (26, 'CCF37-CAJA DE COMPENSACIÓN FAMILIAR DEL NORTE DE SANTANDER COMFANORTE'),
    (27, 'CCF38-CAJA DE COMPENSACIÓN FAMILIAR DE BARRANCABERMEJA CAFABA'),
    (28, 'CCF39-CAJA SANTANDEREANA DE SUBSIDIO FAMILIAR CAJASAN'),
    (29, 'CCF40-CAJA DE COMPENSACIÓN FAMILIAR COMFENALCO SANTANDER'),
    (30, 'CCF41-CAJA DE COMPENSACIÓN FAMILIAR DE SUCRE'),
    (31, 'CCF43-CAJA DE COMPENSACIÓN FAMILIAR DE FENALCO COMFENALCO QUINDIO'),
    (32, 'CCF44-CAJA DE COMPENSACIÓN FAMILIAR DE RISARALDA - COMFAMILIAR RISARALDA'),
    (33, 'CCF46-CAJA DE COMPENSACIÓN FAMILIAR DEL SUR DEL TOLIMA CAFASUR'),
    (34, 'Caja de compensación familiar del norte del Tolima comfaminorte'),
    (35, 'CCF48-CAJA DE COMPENSACIÓN FAMILIAR DEL TOLIMA COMFATOLIMA'),
    (36, 'CCF50-CAJA DE COMPENSACIÓN FAMILIAR DE FENALCO DEL TOLIMA - COMFENALCO'),
    (37, 'CCF56-CAJA DE COMPENSACIÓN FAMILIAR COMFENALCO DEL VALLE DEL CAUCA - COMFENALCO VALLE'),
    (38, 'CCF57-CAJA DE COMPENSACIÓN FAMILIAR DEL VALLE DEL CAUCA COMFAMILIAR ANDI - COMFANDI'),
    (39, 'CCF63-CAJA DE COMPENSACIÓN FAMILIAR DEL PUTUMAYO - COMFAMILIAR PUTUMAYO'),
    (40, 'CCF64-CAJA DE COMPENSACIÓN FAMILIAR DE SAN ANDRES Y PROVIDENCIA, ISLAS CAJASAI'),
    (41, 'CCF65-CAJA DE COMPENSACIÓN FAMILIAR DEL AMAZONAS CAFAMAZ'),
    (42, 'CCF67-CAJA DE COMPENSACIÓN FAMILIAR DE ARAUCA COMFIAR'),
    (43, 'CCF68-CAJA DE COMPENSACIÓN FAMILIAR CAMPESINA COMCAJA'),
    (44, 'CCF69-CAJA DE COMPENSACIÓN FAMILIAR DEL CASANARE - COMFACASANARE')
   ]

    fondos_pensiones = [
    (1, '25-14-COLPENSIONES'),
    (2, '231001-COLFONDOS'),
    (3, '230201-PROTECCIÓN'),
    (4, '230901-OLD MUTUAL (ANTES SKANDIA)'),
    (5, '230301-PORVENIR')
    ]

    fondos_cesantias = [
    (1, '230201-PROTECCIÓN'),
    (2, '230301-PORVENIR'),
    (3, '230901-OLD MUTUAL (ANTES SKANDIA)'),
    (4, '231001-COLFONDOS'),
    (5, 'Fondo nacional del ahorro'),
    (6, 'Fondo de prestaciones sociales del magisterio')
    ]


    Emp_codigo = models.AutoField(primary_key=True)
    Emp_tipoContrato = models.IntegerField(max_length = 30, choices = tipoContrato, verbose_name='Tipo de contrato')
    Emp_tipoTrabajador = models.IntegerField(max_length = 106, choices = tipoTrabajador, verbose_name='Tipo de trabajador')
    Emp_subtipoTrabajador = models.IntegerField(max_length = 106, choices=subtipoTrabajador, verbose_name='Subtipo de trabajador')
    Emp_cargo = models.CharField(max_length = 60, verbose_name='cargo')
    Emp_area = models.IntegerField(max_length = 30, choices=area, verbose_name='Area')
    Emp_diasVacacionesAcumulados = models.IntegerField(verbose_name="dias de vacaciones acumulados")
    Emp_salario = models.IntegerField(verbose_name="salario")
    Emp_auxilioTransporte = models.BooleanField(verbose_name="auxilio de transporte")
    Emp_salarioIntegral = models.BooleanField(verbose_name="salario integral")
    Emp_frecuenciaPago = models.IntegerField(max_length = 30, choices=frecuenciaPago, verbose_name='Frecuencia de pago')
    Emp_metodoDePago = models.IntegerField(max_length = 30, choices=metodoPago, verbose_name='Metodo de pago')
    Emp_nivelDeRiesgo = models.IntegerField(max_length = 30, choices=nivelDeRiesgo, verbose_name='Nivel de riesgo')
    Emp_sabadoLaboral = models.BooleanField(verbose_name="sabado laboral")
    Emp_fechaingreso = models.DateField(verbose_name="fecha de ingreso", auto_now_add=True)
    Emp_fechaFinContrato = models.DateField(verbose_name="fecha fin de contrato")
    Emp_eps = models.IntegerField(max_length = 60, choices=eps, verbose_name='EPS')
    Emp_cajaCompensacion = models.IntegerField(max_length = 60, choices=cajas_compensacion, verbose_name='Caja de compensacion')
    Emp_fondoPensiones = models.IntegerField(max_length = 60, choices=fondos_pensiones, verbose_name='Fondo de pensiones')
    Emp_fondoCesantias = models.IntegerField(max_length = 60, choices=fondos_cesantias, verbose_name='Fondo de cesantias')
    Mun_nombre = models.ForeignKey(Municipio, verbose_name="Municipio", on_delete=models.CASCADE)
    Emp_direccion = models.CharField(max_length = 60, verbose_name='Direccion')
    Persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    Usr_codigo = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")

    class meta:
        db_table = "Empleado"
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def __str__(self) -> str:
        return self.Persona.Per_nombre
