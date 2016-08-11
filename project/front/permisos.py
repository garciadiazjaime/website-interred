# -*- coding: utf-8 -*-

class Permisos(object):

	def eu(self, lang=0):
		data = [
			[
				{
					'id': 'p_eu_mc_domestico',
					'title': 'MC/ICC Authority - Doméstico 48 estados',
					'desc': 'Este permiso, expedido a través del DOT (Departamento de Transporte, por sus siglas en inglés), otorga el libre tránsito en los 48 estados de Estados Unidos, es de tipo comercial para los domiciliados dentro de Estados Unidos cuyos propietarios son de procedencia norteamericana o ciudadanos residentes.',
				},
				{
					'id': 'p_eu_dot',
					'title': 'MC/ICC Authority - Enterprise 48 estados',
					'desc': 'Este permiso, expedido a través del DOT (Departamento de Transporte, por sus siglas en inglés), otorga el libre tránsito en los 48 estados de Estados Unidos, es de tipo comercial y es aplicado a compañías de transporte de carga cuya procedencia de mercancías es de México.',
				},
				{
					'id': 'p_eu_haz_mat',
					'title': 'MX/ICC Authority - Zona Comercial 50 millas',
					'desc': 'Tramitado a través del DOT (Departamento de Transporte, por sus siglas en inglés), permite transitar exclusivamente dentro de los límites de 50 millas de zona comercial. Es aplicado a unidades de carga comercial.',
				},
				{
					'id': 'p_eu_mc_enterprise',
					'title': 'DOT',
					'desc': 'El Departamento de Transporte, encargado de regular al sector transportista, otorga el número de identificación a cada compañía de negocio comercial, llámese transporte de carga público, privado, turismo y  pasaje, entre otros.',
				},
				{
					'id': 'p_eu_ca_chp',
					'title': 'CA -  CHP',
					'desc': 'La función de la California Higway Patrol (CHP) es regular e inspeccionar el mantenimiento y la seguridad de unidades de tipo comercial en carreteras y aduanas comerciales dentro del estado de California. Este organismo expide el número de identificación otorgado a vehículos de carga.',
				},
				{
					'id': 'p_eu_carga_ancha',
					'title': 'DIESEL',
					'desc': 'Reporte trimestral aplicado a transportistas de uso de combustible interestatal que no cuenten con el registro FUEL TAX AGREEMENT – IFTA.',
				},
				{
					'id': 'p_eu_mc_comercial',
					'title': 'HAZ MAT (Licencia de materiales peligrosos) - Federal y Estatal',
					'desc': 'Licencia y registro ante el USDOT para transporte de materiales peligrosos.',
				},
				{
					'id': 'p_eu_diesel',
					'title': 'PERMISOS CARGA ANCHA',
					'desc': 'Este permiso es aplicado a unidades de carga que transitan en carreteras en Estados Unidos y que sus dimensiones sean excesivas. Es necesario obtener permisos ante la autoridad competente antes de efectuar cualquier maniobra que exceda los límites permitidos de carga para la misma autoridad.',
				},
				{
					'id': 'p_eu_permiso_estado',
					'title': 'Permisos de Estado (Cruce) Arizona, Nevada, Oregón',
					'desc': 'Es requisito que un vehículo comercial de carga inicie el trámite correspondiente  de diesel y millas que recorrerá dentro de ese estado antes de cruzar a otro estado fuera de California. Nuestra oficina puede ofrecer el servicio de tramitación de dichos permisos. En este caso, la mayoría de nuestros clientes cuentan con unidades que tienen placas de California y no de los estados vecinos, Arizona, Nevada y Oregón; cuando cruzan estado se les requiere. Este permiso se debe tramitar por camión y por viaje.',
				},			
			],
			[
				{
					'id': 'p_eu_mc_domestico',
					'title': 'MC/ICC Authority - Domestic 48 States',
					'desc': 'This permit is issued by the Department of Transportation for the free travel throughout the 48 states of the U.S. It’s a commercial permit for residents in the U.S. whose owners are from the U.S. or resident citizens.',
				},
				{
					'id': 'p_eu_dot',
					'title': 'MC/ICC Authority - Enterprise 48 States',
					'desc': 'This permit is issued by the Department of Transportation to allow free travel throughout the 48 states of the U.S. It’s a commercial permit and applies to freight transportation companies whose goods originate from Mexico.',
				},
				{
					'id': 'p_eu_haz_mat',
					'title': 'MX/ICC Authority – Commercial Zone 50 miles',
					'desc': 'Processed through the Department of Transportation, it allows travel exclusively within the limits of 50 miles of commercial zone. It applies to commercial freight units.',
				},
				{
					'id': 'p_eu_mc_enterprise',
					'title': 'DOT',
					'desc': 'The Department of Transportation is responsible for regulating the transportation sector and issues the identification number to each commercially oriented company, public and private freight transportation, tourism, and travel amongst others.',
				},
				{
					'id': 'p_eu_ca_chp',
					'title': 'CA - CHP',
					'desc': 'The California Highway Patrol (CHP) is responsible for regulating and inspecting maintenance and safety in commercial units on highways and commercial customs in the state of California. This agency issues the ID number to freight vehicles.',
				},
				{
					'id': 'p_eu_carga_ancha',
					'title': 'DIESEL',
					'desc': 'Quarterly report applied to interstate fuel use carriers whom do not have the FUEL TAX AGREEMENT – IFTA registration.',
				},
				{
					'id': 'p_eu_mc_comercial',
					'title': 'HAZ MAT - Federal and State',
					'desc': 'License and registration issued through the USDOT for the transportation of hazardous materials.',
				},
				{
					'id': 'p_eu_diesel',
					'title': 'Oversize Permits',
					'desc': 'This permit applies to freight units that travel U.S. roads and whose freight is excessively wide. A permit must be acquired before initiating any transit that surpasses pre- determined limits.',
				},
				{
					'id': 'p_eu_permiso_estado',
					'title': 'State Trip Permits - Arizona, Nevada, Oregon',
					'desc': 'This permit is required for commercial vehicles to initiate the corresponding paperwork for the diesel gas and miles travelling within that state before crossing into another state outside California. Servicios Garita Otay can take care of processing such permits. The majority of our clients’ units have California plates and none from the neighboring states of Arizona, Nevada and Oregon. When the unit crosses a state, this permit will be required. A permit is required per truck and per trip.',
				},					
			]
			
		]		
		return data[lang]

