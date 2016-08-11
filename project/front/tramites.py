# -*- coding: utf-8 -*-

class Tramites(object):

	def dmv(self, lang=0):
		data = [
			[
				{
					'id': 'dmv_default',					
					'desc': '<p>Nuestro servicio ante el Departamento de Vehículos Motorizados (DMV) es muy oportuno. Lo realizamos de manera profesional y le ayudamos a tramitar sus registros, cambios de nombres y otros trámites diversos.</p><p>Usted evitará largas filas, trámites complicados y sólo obtendrá la satisfacción de contar con su movimiento a tiempo.</p>',
					'class': '',
				},
				{
					'id': 'dmv_renovacion',
					'title': 'Renovaciones, Parciales, Auto y Comercial',
					'desc': 'Es importante contar con un registro vigente de auto en el estado de California. Usted evitará contratiempos, multas o el remolque de su unidad. Nosotros le ayudamos siempre de manera oportunidad. Usted evitará largas filas y pagos innecesarios en muchos casos.',
					'class': '',
				},
				{
					'id': 'dmv_verificacion',
					'title': 'Verificaciones de Tráilers ante DMV ',
					'desc': 'Evite largas filas para verificar su caja o tractor. Nosotros contamos con la Licencia de Verificador ante el Departamento de Vehículos Motorizados. Es requisito verificar ante el DMV cuando la serie es ilegible o no coincide con el chasis o la cabina.',
					'class': '',
				},
				{
					'id': 'dmv_duplicado',
					'title': 'Duplicado de Registro, Láminas, Calcomanías',
					'desc': 'Es frecuente el extravío de láminas y registros de auto, inclusive el robo de la calcomanía del mes o del año de la lámina. Usted, a través de nuestro Departamento de Trámites, podrá solicitar una reposición. ',
					'class': '',
				},
				{
					'id': 'dmv_registro',
					'title': 'Registro de Caja Mexicana en California',
					'desc': 'De acuerdo a la modalidad que existe entre los departamentos de transporte DMV y SCT, podemos hacer el registro de cualquier remolque, caja o plataforma que sea de registro mexicano. Usted podrá solicitar su lámina de California y gozar del periodo de 6 años de tránsito libre y sin ningún problema.',
					'class': '',
				},				
				{
					'id': 'dmv_cambios',
					'title': 'Cambios de Propietario, Bajas y Altas de Registro',
					'desc': 'Servicios Garita Otay le ayuda de manera acertada a tramitar su registro por primera vez cuando se trate de una alta de auto o auto comercial, cubriendo los pagos necesarios para obtener el registro y la lámina.  En el caso de Baja California, notificamos al DMV sobre la venta, regalo o pérdida de la unidad con lo que usted ampara su propiedad ante el DMV. ',
					'class': '',
				},
				{
					'id': 'dmv_duplicado_titulo',
					'title': 'Duplicados de Título',
					'desc': 'Podemos ayudarle a obtener su duplicado de título, ya sea de auto o auto comercial, ante el DMV. Con nuestros servicios usted evitará que su trámite de prolongue por meses y que se generen pagos innecesarios.',
					'class': '',
				},
			],	
			[
				{
					'id': 'dmv_default',					
					'desc': '<p>Eng Nuestro servicio ante el Departamento de Vehículos Motorizados (DMV) es muy oportuno. Lo realizamos de manera profesional y le ayudamos a tramitar sus registros, cambios de nombres y otros trámites diversos. Usted evitará largas filas, trámites complicados y sólo obtendrá la satisfacción de contar con su movimiento a tiempo.</p>',
					'class': '',
				},
				{
					'id': 'dmv_renovacion',
					'title': 'Eng Renovación, Parcial, Auto y Comercial',
					'desc': '<p>Eng Párrafo Renovacion, Parcial, Auto y Comercial</p>',
					'class': '',
				},
				{
					'id': 'dmv_verificacion',
					'title': 'Eng Verificación de Tráilers ante DMV',
					'desc': '<p>Eng Párrafo Verificación de Tráilers ante DMV</p>',
					'class': '',
				},
				{
					'id': 'dmv_dup_registro',
					'title': 'Eng Duplicado de Registro, Láminas, Calcomanías',
					'desc': '<p>Eng Párrafo Duplicado de Registro, Láminas, Calcomanías</p>',
					'class': '',
				},
				{
					'id': 'dmv_registro_caja',
					'title': 'Eng Registro de Caja Mexicana en California',
					'desc': '<p>Eng Párrafo Registro de Caja Mexicana en California</p>',
					'class': '',
				},
				{
					'id': 'dmv_cambios',
					'title': 'Eng Cambios de Propietario, Bajas y Altas de Registro',
					'desc': '<p>Eng Párrafo Cambios de Propietario, Bajas y Altas de Registro</p>',
					'class': '',
				},
				{
					'id': 'dmv_cambios',
					'title': 'Eng Duplicado de Título',
					'desc': '<p>Eng Párrafo Duplicado de Título</p>',
					'class': '',
				},
			]
		]		
		return data[lang]

	def eu(self, lang=0):
		data = [
			[
				{
					'id': 'eu_default',
					'desc': 'Es fundamental para el sector transportista cumplir con la normatividad de  requerimientos y permisos que son necesarios para transitar en forma comercial en carreteras de Estados Unidos y México.',
				},
				{
					'id': 'eu_placas',
					'title': 'Placas Apportioned, 48 Estados, Vehículos Comerciales (IRP)',
					'desc': 'Registro que permite transitar libremente sobre carreteras dentro de la Unión Americana, aplicado EXCLUSIVAMENTE a unidades comerciales, no habiendo límites de millas fuera de la zona comercial. El pago es anual y las placas son para diferentes estados.',
				},
				{
					'id': 'eu_arb',
					'title': 'ARB',
					'subtitle': '(Registration Air Resources Board)',
					'desc': 'Es un registro para vehículos comerciales de modelos antiguos. Se implementa un programa de filtros y un equipo de mejor calidad para combatir la contaminación de smog en el medio ambiente.',
				},
				{
					'id': 'eu_us_fee',
					'title': 'US FEE – Calcomania de Aduana',
					'desc': 'Este programa llamado US Customs Decal identifica el vehículo que cruza la frontera a Estados Unidos mediante un sensor colocado en el vidrio de la unidad. De acuerdo a la Ley Ómnibus Consolidada de Reconciliación Presupuestaria (COBRA), autoriza recibir cuotas por distintos servicios.',
				},
				{
					'id': 'eu_ifta',
					'title': 'IFTA',
					'subtitle': '(Permiso y Calcomanías) ',
					'desc': 'Es un formato diseñado para el transportista que opera dentro de los 48 estados y fuera de una jurisdicción. Simplifica un reporte de combustible por parte de la empresa. Es aplicado principalmente a vehículos de carga comercial.',
				},
				{
					'id': 'eu_mcp',
					'title': 'MCP',
					'subtitle': '(Permiso de Motor para Transportistas)',
					'desc': 'Es un registro para vehículos comerciales de modelos antiguos. Se implementa un programa de filtros y un equipo de mejor calidad para combatir la contaminación de smog en el medio ambiente.',
				},
				{
					'id': 'eu_gafete',
					'title': 'Gafete Norteamericano para Chofer',
					'desc': 'Le ayudamos en el llenado de la forma que requiere la aduana norteamericana para complementar la información y para aplicar para el Gafete de Manejo Comercial.',
				},
				{
					'id': 'eu_f2290',
					'title': 'F-2290',
					'subtitle': '(IRS Form 2290, Tax ID)',
					'desc': 'Heavy Higway Vehicle Use Tax Return es una forma para presentar el pago de impuestos por uso de carreteras en California, aplicado a vehículos de carga mayor a las 54,000  lb.',
				},
				{
					'id': 'eu_bit',
					'title': 'BIT- Program Enrollment ',
					'desc': 'La finalidad de este programa es verificar que cada terminal de vehículos de carga sea inspeccionada por la California Higway Patrol (CHP). Es importante que los vehículos cumplan con inspecciones y mantenimiento de manera periódica. Este programa es establecido por la Ley de California.',
				},
				{
					'id': 'eu_antidoping',
					'title': 'Programa de Concientización Antidoping ',
					'desc': 'La Parte 382 del acuerdo sobre regulaciones del Departamento de Transporte (DOT) establece que cada compañía transportista deberá inscribir a sus operadores a un programa concientizado de alcohol y drogas, donde se implementarán pruebas previas al empleo y aleatorias.',
				},	
				{
					'id': 'eu_scac',
					'title': 'SCAC – Alpha Code ',
					'desc': 'Es un código requerido que por sus siglas es llamado SCAC (Standard Carrier Alpha Code). Es utilizado para identificación de la compañía transportista. Es indispensable para tramitar documentación de exportación de mercancías ante las agencias de comercio.',
				},
				{				
					'id': 'eu_pull',
					'title': 'Pull Notice Program ',
					'desc': 'Es un programa de seguridad para conductores de compañías de transporte. Se cumple en términos de seguridad, determina si cada conductor tiene una licencia vigente e identifica cualquier problema de manejo o del conductor.',
				},
				{				
					'id': 'empty_eu_01',
					'title': '',
					'desc': '',
				},
				{
					'id': 'eu_ucr',
					'title': 'UCR',
					'subtitle': '<em>(Unifed Carrier Registration)</em>',
					'desc': 'Es un programa llamado Registro de Transportistas Unidos y fue creado en el 2007 con la finalidad de recabar fondos con base en el número de unidades a cargo de cada compañía o registro transportista. Los fondos son destinados a implementar programas para el sector.',
				},															
				{	
					'id': 'eu_fast',			
					'title': 'FAST',
					'desc': 'Es un programa de aduana norteamericano que se implementa  para compañías de trasportes. Permite el cruce rápido por la línea fronteriza comercial mediante distintas medidas de seguridad.',
				},														
				{				
					'id': 'empty_eu_02',
					'title': '',
					'desc': '',
				},
			],
			[
				{
					'id': 'eu_default',
					'desc': 'It is essential for the transport sector to comply with the regulations and permits required to travel commercially on U.S. and Mexican highways.',
				},	
				{			
					'id': 'eu_placas',
					'title': 'Apportioned Registration (IRP), 48 States, Commercial Vessels',
					'desc': 'Registration that allows free travel on U.S. roads and applies EXCLUSEVELY to commercial units with no limits on miles outside of the commercial zone. Payment is annual and plates are issued for different states.',
				},
				{
					'id': 'eu_arb',
					'title': 'ARB',
					'subtitle': '<em>(Air Resources Board)</em>',
					'desc': 'Registration for older models of commercial vessels. The program consists in the implementation of filters and a better quality of equipment to avoid smog pollution to the environment.',
				},
				{
					'id': 'eu_us_fee',
					'title': 'US FEE',
					'desc': 'The program known as the US Customs Decal identifies vehicles crossing the U.S. border through a sensor placed on the vehicles windshield. According to COBRA, it is authorized to collect fees for different services.',
				},			
				{
					'id': 'eu_ifta',
					'title': 'IFTA',
					'subtitle': '(License and Decal)',
					'desc': 'It is an agreement designed for the carrier that travels within the 48 U.S. states and outside one jurisdiction. It simplifies the use of fuel by motor carriers and it applies to freight commercial vessels.',
				},
				{
					'id': 'eu_mcp',
					'title': 'MCP',
					'subtitle': '(Motor Carrier Permit)',
					'desc': 'A document issued by the DMV to the motor carrier as evidence of their registration with the agency on their Carrier Identification Number (CA#). This permit also verifies that the carrier has met the statutory requirements to commercially operate motor vehicles on California’s highways.',
				},
				{
					'id': 'eu_gafete',
					'title': 'Commercial Driving Badge',
					'desc': 'We assist you in the completing and the filing of the application form required by U.S. customs for your commercial driving badge.',
				},		
				{		
					'id': 'eu_f2290',
					'title': 'F-2290',
					'subtitle': '(IRS Form 2290, Tax ID)',
					'desc': 'The Heavy Highway Vehicle Use Tax Return is a form used to pay taxes due to the use of roads in California. It applies to freight vessels over 54,000 pounds',
				},	
				{
					'id': 'eu_bit',
					'title': 'BIT- Program Enrollment ',
					'desc': 'The purpose of this is to verify that each freight vehicle’s terminal is inspected by the California Highway Patrol (CHP). It is important for vehicles to comply with periodic inspections and maintenance. This program was established by California Law.',
				},
				{
					'id': 'eu_antidoping',
					'title': 'Anti-doping Awareness Program',
					'desc': 'Part 382 of the Department of Transportation (DOT) agreement establishes that each transportation company shall enroll it operators in an alcohol and drug awareness program, where pre-employment and random screenings are held.',
				},		
				{
					'id': 'eu_scac',
					'title': 'SCAC (Standard Carrier Alpha Code)',
					'desc': 'A code used to identify transportation companies. It is essential to process documentation for goods exported before trade agencies.',
				},
				{
					'id': 'eu_pull',
					'title': 'Pull Notice Program ',
					'desc': 'A security program for drivers of transportation companies. It determines if each driver has a valid driver license or identifies any driving or driver problems.',
				},
				{
					'id': 'empty_eu_01',
					'title': '',
					'desc': '',
				},			
				{
					'id': 'eu_ucr',
					'title': 'UCR',
					'subtitle': '(Unifed Carrier Registration)',
					'desc': 'Es un programa llamado Registro de Transportistas Unidos y fue creado en el 2007 con la finalidad de recabar fondos con base en el número de unidades a cargo de cada compañía o registro transportista. Los fondos son destinados a implementar programas para el sector.',
				},																	
				{
					'id': 'eu_fast',
					'title': 'FAST',
					'desc': 'A North American customs program implemented for transportation companies. It allows a fast commercial border crossing going through different security measures.',
				},
				{
					'id': 'empty_eu_02',
					'title': '',
					'desc': '',
				},
			]
			
		]		
		return data[lang]

	def mx(self, lang=0):
		data = [
			[
				{
					'id': 'mx_default',					
					'desc': 'Es esencial para el transporte de carga en México contar con los permisos requeridos y cumplir con las disposiciones para su operación dentro del territorio mexicano. Existen trámites de acuerdo a modalidades emitidas por el mismo departamento. El propósito es cumplir con los parámetros de seguridad en carreteras federales.',
				},				
				{
					'id': 'mx_placas',
					'title': 'Secreataría de Comunicaciones y Transporte (SCT) Placas Transfer 20 Km',
					'desc': 'Es un permiso expedido por la Secretaría de Comunicaciones y Transportes (SCT) exclusivamente para vehículos comerciales de procedencia extranjera para su tránsito en la franja fronteriza, con límite de 20 km.',
				},
				{
					'id': 'mx_duplicados_cotejo',
					'title': 'Registro de Permisos por Primera Vez ante la SCT',
					'desc': 'Registro por primera vez para obtener las licencias y permisos para circular en carreteras en la franja fronteriza, límite 20 km.',
				},
				{	
					'id': 'mx_caat',			
					'title': 'CAAT',
					'subtitle': '(Código Armonizado Alfanumérico de Transportista)',
					'desc': 'Es el permiso que necesitan los transportistas para importar mercancía a México.',
				},
				{
					'id': 'mx_renovacion',
					'title': 'Renovaciones - Transfer ',
					'desc': 'El refrendo vigente y registro anual son necesarios para continuar con el permiso expedido por la SCT: libre para transitar en la franja fronteriza.',
				},				
				{
					'id': 'mx_baja_permisos',
					'title': 'Solicitud de Baja de Permisos',
					'desc': 'Solicitud de trámite para notificar al Departamento de Autotransporte Federal de la SCT la baja de una unidad, ya sea por venta o por estar fuera de servicio.',
				},
				{
					'id': 'empty_mx_01',
					'title': '',
					'desc': '',
				},								
				{
					'id': 'mx_duplicados_cotejo',
					'title': 'Duplicados y Cotejo de Tarjetón Mexicano',
					'desc': 'Ya que es frecuente el extravío de documentos de la propiedad, es recomendable solicitar ante el Departamento de Autotransporte Federal de la SCT una copia fiel y cotejada de los archivos correspondientes en cada movimiento con el fin de evitar demoras ante aduanas y dependencias gubernamentales.',
				},												
				{				
					'id': 'mx_placas_federales',
					'title': 'Solicitud para Placas Federales',
					'desc': 'Registro para vehículos de carga, exclusivamente vehículos nacionales, para su libre tránsito en carreteras de México.',
				},
				{
					'id': 'empty_mx_02',
					'title': '',
					'desc': '',
				},			
			],
			[
				{
					'id': 'eu_default',
					'desc': 'It is essential for the transport sector to comply with the regulations and permits required to travel commercially on U.S. and Mexican highways.',
				},	
				{			
					'id': 'mx_placas',
					'title': 'Transfer Plates, 20 Km',
					'desc': 'A permit issued by the Ministry of Communications and Transportation in Mexico (SCT, for its acronym in Spanish) exclusively for foreign commercial vehicles to travel along the border line, limit to 20km (12 miles).',
				},
				{
					'id': 'mx_duplicados_cotejo',
					'title': 'First Time Permit Registration with the Mexican Ministry of Communications, SCT',
					'desc': 'First time registration to obtain licenses and permits to drive in the borderline highways; limit of 20km (12 miles).',
				},
				{
					'id': 'mx_caat',
					'title': 'CAAT (Alphanumeric Harmonized Code Carrier)',
					'desc': 'This is the permit required for carriers to import goods into Mexico.',
				},		
				{
					'id': 'mx_renovacion',
					'title': 'Renewals - Transfer',
					'desc': 'A valid referendum and annual registration are required to continue validation of the permit issued by the Mexican Ministry of Communications and Transportation (SCT): free travel along the border line.',
				},
				{
					'id': 'mx_baja_permisos',
					'title': 'Non-Operating Permit Application',
					'desc': 'This is the application to notify the Federal Auto-Transport Department of the Mexican Ministry of Communications and Transportation of a non-operating unit in the case of a sale or out of service.',
				},
				{
					'id': 'empty_mx_01',
					'title': '',
					'desc': '',
				},		
				{		
					'id': 'mx_duplicados_cotejo',
					'title': 'Mexican Card Duplicate and Checking',
					'desc': 'As common as it is to lose unit documentation, it is recommended to request before the Federal Auto-Transportation Department from the SCT a true and accurate copy of each document in order to avoid delays at customs and governmental agencies.',
				},									
				{
					'id': 'mx_placas_federales',
					'title': 'Non-Operating Federal Application',
					'desc': 'Application for registration for freight vehicles. Exclusively for domestic vessel fees to travel on Mexico’s highways.',
				},
				{
					'id': 'empty_mx_02',
					'title': '',
					'desc': '',
				},										
			]
			
		]		
		return data[lang]
