﻿# Interface to CitySim
# 
# Giuseppe Peronato <giuseppe.peronato@epfl.ch> 
# 

"""
Export CitySim XML
-

    
    Args:
        geometry: Tree of BReps (buildings;surfaces)
        path: Directory
        name: name of the project
    Returns:

"""

ghenv.Component.Name = "CitySim_RunSimulation"
ghenv.Component.NickName = 'RunSimulation'
ghenv.Component.Message = 'VER 0.0.1\nNOV_03_2016'
ghenv.Component.Category = "User"
ghenv.Component.SubCategory = "CitySim"
try: ghenv.Component.AdditionalHelpFromDocStrings = "1"
except: pass

import rhinoscriptsyntax as rs


def tree_to_list(input, retrieve_base = lambda x: x[0]):
    """Returns a list representation of a Grasshopper DataTree"""
    # written by Giulio Piacentino, giulio@mcneel.com
    def extend_at(path, index, simple_input, rest_list):
        target = path[index]
        if len(rest_list) <= target: rest_list.extend([None]*(target-len(rest_list)+1))
        if index == path.Length - 1:
            rest_list[target] = list(simple_input)
        else:
            if rest_list[target] is None: rest_list[target] = []
            extend_at(path, index+1, simple_input, rest_list[target])
    all = []
    for i in range(input.BranchCount):
        path = input.Path(i)
        extend_at(path, 0, input.Branch(path), all)
    return retrieve_base(all)
    
import rhinoscriptsyntax as rs
    
geometry = tree_to_list(geometry, retrieve_base = lambda P: P)
xml = '''<?xml version="1.0" encoding="ISO-8859-1"?>
<CitySim name="test">
	<Simulation beginMonth="1" endMonth="12" beginDay="1" endDay="31"/>
	<Climate location="sample.cli" city="Unknown"/>
	<District>
		<FarFieldObstructions>
			<Point phi="0"  theta="0"/>
			<Point phi="360"  theta="0"/>
		</FarFieldObstructions>
		<Composite id="12" name="Neuchatel_1981-1990_Double" category="Wall">
			<Layer Thickness="0.0100" Conductivity="0.5000" Cp="1000" Density="1300" nre="0" gwp="0" ubp="0"/>
			<Layer Thickness="0.1000" Conductivity="1.1300" Cp="1000" Density="1431" nre="0" gwp="0" ubp="0"/>
			<Layer Thickness="0.0800" Conductivity="0.7900" Cp="1000" Density="1329" nre="0" gwp="0" ubp="0"/>
			<Layer Thickness="0.1200" Conductivity="0.7900" Cp="1000" Density="1329" nre="0" gwp="0" ubp="0"/>
			<Layer Thickness="0.0200" Conductivity="0.8500" Cp="837" Density="1900" nre="0" gwp="0" ubp="0"/>
		</Composite>
		<Composite id="21" name="Simple wall" category="Wall">
			<Layer Thickness="0.1500" Conductivity="200.0000" Cp="418" Density="8900" nre="0" gwp="0" ubp="0"/>
			<Layer Thickness="0.1500" Conductivity="0.6200" Cp="840" Density="1800" nre="0" gwp="0" ubp="0"/>
		</Composite>
		<Composite id="15" name="Neuchatel_1991-2000_Double" category="Wall">
			<Layer Thickness="0.0100" Conductivity="0.5000" Cp="1000" Density="1700" nre="0" gwp="0" ubp="0"/>
			<Layer Thickness="0.1500" Conductivity="0.3600" Cp="1000" Density="1500" nre="0" gwp="0" ubp="0"/>
			<Layer Thickness="0.1200" Conductivity="0.3600" Cp="1050" Density="700" nre="0" gwp="0" ubp="0"/>
			<Layer Thickness="0.1200" Conductivity="0.1600" Cp="1050" Density="2500" nre="0" gwp="0" ubp="0"/>
			<Layer Thickness="0.0200" Conductivity="0.1600" Cp="840" Density="577" nre="0" gwp="0" ubp="0"/>
		</Composite>
		<Composite id="8" name="Neuchatel_1961-1970_isole" category="Wall">
			<Layer Thickness="0.0100" Conductivity="1.8300" Cp="712" Density="2200" nre="0" gwp="0" ubp="0"/>
			<Layer Thickness="0.0600" Conductivity="2.9000" Cp="900" Density="2650" nre="0" gwp="0" ubp="0"/>
			<Layer Thickness="0.0600" Conductivity="2.0000" Cp="880" Density="2500" nre="0" gwp="0" ubp="0"/>
			<Layer Thickness="0.1700" Conductivity="1.5000" Cp="720" Density="2180" nre="0" gwp="0" ubp="0"/>
			<Layer Thickness="0.0200" Conductivity="2.0000" Cp="753" Density="2700" nre="0" gwp="0" ubp="0"/>
		</Composite>

		<OccupancyDayProfile id="5" name="Day Profile5" p1="0.31" p2="0.35" p3="0.37" p4="0.4" p5="0.42" p6="0.44" p7="0.46" p8="0.49" p9="0.57" p10="0.62" p11="0.69" p12="0.75" p13="0.8" p14="0.77" p15="0.7" p16="0.62" p17="0.59" p18="0.53" p19="0.51" p20="0.51" p21="0.48" p22="0.43" p23="0.47" p24="0.43" />
		<OccupancyDayProfile id="2" name="Day Profile2" p1="0.11" p2="0.16" p3="0.18" p4="0.21" p5="0.24" p6="0.25" p7="0.26" p8="0.28" p9="0.28" p10="0.28" p11="0.28" p12="0.28" p13="0.28" p14="0.28" p15="0.28" p16="0.22" p17="0.21" p18="0.27" p19="0.21" p20="0.21" p21="0.22" p22="0.22" p23="0.24" p24="0.24" />
		<OccupancyDayProfile id="3" name="Day Profile3" p1="0.4" p2="0.4" p3="0.39" p4="0.39" p5="0.39" p6="0.39" p7="0.38" p8="0.38" p9="0.38" p10="0.28" p11="0.28" p12="0.28" p13="0.28" p14="0.28" p15="0.28" p16="0.22" p17="0.21" p18="0.08" p19="0.21" p20="0.21" p21="0.22" p22="0.24" p23="0.24" p24="0.24" />
		<OccupancyDayProfile id="4" name="Day Profile4" p1="0.4" p2="0.39" p3="0.39" p4="0.39" p5="0.39" p6="0.39" p7="0.38" p8="0.38" p9="0.38" p10="0.38" p11="0.37" p12="0.37" p13="0.37" p14="0.36" p15="0.35" p16="0.35" p17="0.35" p18="0.35" p19="0.35" p20="0.35" p21="0.36" p22="0.73" p23="0.42" p24="0.44" />
		<OccupancyDayProfile id="1" name="Day Profile1" p1="0.39" p2="0.39" p3="0.39" p4="0.39" p5="0.39" p6="0.39" p7="0.38" p8="0.38" p9="0.38" p10="0.38" p11="0.37" p12="0.37" p13="0.32" p14="0.37" p15="0.35" p16="0.35" p17="0.35" p18="0.35" p19="0.35" p20="0.35" p21="0.36" p22="0.39" p23="0.42" p24="0.44" />

		<OccupancyYearProfile id="2" name="Year Profile2" d1="1" d2="0" d3="0" d4="0" d5="0" d6="0" d7="0" d8="0" d9="0" d10="0" d11="0" d12="0" d13="5" d14="0" d15="0" d16="0" d17="0" d18="0" d19="0" d20="3" d21="3" d22="3" d23="3" d24="0" d25="0" d26="5" d27="5" d28="5" d29="0" d30="0" d31="0" d32="3" d33="0" d34="0" d35="5" d36="0" d37="0" d38="0" d39="0" d40="5" d41="0" d42="0" d43="0" d44="0" d45="0" d46="0" d47="0" d48="4" d49="0" d50="0" d51="3" d52="0" d53="0" d54="0" d55="0" d56="0" d57="2" d58="0" d59="0" d60="0" d61="0" d62="0" d63="0" d64="0" d65="0" d66="0" d67="0" d68="0" d69="0" d70="0" d71="0" d72="0" d73="0" d74="0" d75="0" d76="0" d77="0" d78="0" d79="0" d80="0" d81="0" d82="0" d83="0" d84="0" d85="0" d86="0" d87="0" d88="0" d89="0" d90="0" d91="0" d92="0" d93="0" d94="0" d95="0" d96="0" d97="0" d98="0" d99="0" d100="0" d101="0" d102="0" d103="0" d104="0" d105="0" d106="0" d107="0" d108="0" d109="0" d110="0" d111="0" d112="0" d113="0" d114="0" d115="0" d116="0" d117="0" d118="0" d119="0" d120="0" d121="0" d122="0" d123="0" d124="0" d125="0" d126="0" d127="0" d128="0" d129="0" d130="0" d131="0" d132="0" d133="0" d134="0" d135="0" d136="0" d137="0" d138="0" d139="0" d140="0" d141="0" d142="0" d143="0" d144="0" d145="0" d146="0" d147="0" d148="0" d149="0" d150="0" d151="0" d152="0" d153="0" d154="0" d155="0" d156="0" d157="0" d158="0" d159="0" d160="0" d161="0" d162="0" d163="0" d164="0" d165="0" d166="0" d167="0" d168="0" d169="0" d170="0" d171="0" d172="0" d173="0" d174="0" d175="0" d176="0" d177="0" d178="0" d179="0" d180="0" d181="0" d182="0" d183="0" d184="0" d185="0" d186="0" d187="0" d188="0" d189="0" d190="0" d191="0" d192="0" d193="0" d194="0" d195="0" d196="0" d197="0" d198="0" d199="0" d200="0" d201="0" d202="0" d203="0" d204="0" d205="0" d206="0" d207="0" d208="0" d209="0" d210="0" d211="0" d212="0" d213="0" d214="0" d215="0" d216="0" d217="0" d218="0" d219="0" d220="0" d221="0" d222="0" d223="0" d224="0" d225="0" d226="0" d227="0" d228="0" d229="0" d230="0" d231="0" d232="0" d233="0" d234="0" d235="0" d236="0" d237="0" d238="0" d239="0" d240="0" d241="0" d242="0" d243="0" d244="0" d245="0" d246="0" d247="0" d248="0" d249="0" d250="0" d251="2" d252="2" d253="2" d254="2" d255="2" d256="2" d257="0" d258="0" d259="0" d260="0" d261="0" d262="1" d263="1" d264="1" d265="1" d266="1" d267="1" d268="1" d269="1" d270="1" d271="1" d272="1" d273="1" d274="1" d275="1" d276="1" d277="1" d278="1" d279="1" d280="1" d281="1" d282="1" d283="1" d284="1" d285="1" d286="1" d287="1" d288="1" d289="1" d290="1" d291="1" d292="1" d293="1" d294="1" d295="1" d296="1" d297="1" d298="1" d299="1" d300="1" d301="1" d302="1" d303="1" d304="1" d305="1" d306="1" d307="1" d308="1" d309="1" d310="1" d311="1" d312="1" d313="1" d314="1" d315="1" d316="1" d317="1" d318="1" d319="1" d320="1" d321="1" d322="1" d323="1" d324="1" d325="1" d326="1" d327="1" d328="1" d329="1" d330="1" d331="1" d332="1" d333="1" d334="1" d335="1" d336="1" d337="1" d338="1" d339="1" d340="1" d341="1" d342="1" d343="1" d344="1" d345="1" d346="1" d347="1" d348="1" d349="1" d350="1" d351="1" d352="1" d353="1" d354="1" d355="1" d356="1" d357="1" d358="1" d359="1" d360="1" d361="1" d362="1" d363="1" d364="1" d365="1" />
		<OccupancyYearProfile id="3" name="SP Profile 1" d1="1" d2="0" d3="0" d4="0" d5="0" d6="0" d7="0" d8="0" d9="0" d10="0" d11="0" d12="0" d13="0" d14="0" d15="0" d16="0" d17="0" d18="0" d19="0" d20="4" d21="4" d22="4" d23="4" d24="4" d25="0" d26="0" d27="0" d28="0" d29="0" d30="0" d31="0" d32="0" d33="0" d34="0" d35="2" d36="0" d37="0" d38="0" d39="3" d40="0" d41="0" d42="2" d43="0" d44="0" d45="0" d46="0" d47="0" d48="0" d49="0" d50="0" d51="0" d52="0" d53="0" d54="1" d55="1" d56="1" d57="1" d58="1" d59="1" d60="1" d61="1" d62="1" d63="1" d64="1" d65="1" d66="1" d67="1" d68="1" d69="1" d70="1" d71="1" d72="1" d73="1" d74="1" d75="1" d76="1" d77="1" d78="1" d79="1" d80="1" d81="1" d82="1" d83="1" d84="1" d85="1" d86="1" d87="1" d88="1" d89="1" d90="1" d91="1" d92="1" d93="1" d94="1" d95="1" d96="1" d97="1" d98="1" d99="1" d100="1" d101="1" d102="1" d103="1" d104="1" d105="1" d106="1" d107="1" d108="1" d109="1" d110="1" d111="1" d112="1" d113="1" d114="1" d115="1" d116="1" d117="1" d118="1" d119="1" d120="1" d121="1" d122="1" d123="1" d124="1" d125="1" d126="1" d127="1" d128="1" d129="1" d130="1" d131="1" d132="1" d133="1" d134="1" d135="1" d136="1" d137="1" d138="1" d139="1" d140="1" d141="1" d142="1" d143="1" d144="1" d145="1" d146="1" d147="1" d148="1" d149="1" d150="1" d151="1" d152="1" d153="1" d154="1" d155="1" d156="1" d157="1" d158="1" d159="1" d160="1" d161="1" d162="1" d163="1" d164="1" d165="1" d166="1" d167="1" d168="1" d169="1" d170="1" d171="1" d172="1" d173="1" d174="1" d175="1" d176="1" d177="1" d178="1" d179="1" d180="1" d181="1" d182="1" d183="1" d184="1" d185="1" d186="1" d187="1" d188="0" d189="0" d190="0" d191="1" d192="1" d193="0" d194="1" d195="1" d196="1" d197="1" d198="1" d199="1" d200="1" d201="1" d202="1" d203="1" d204="1" d205="1" d206="1" d207="1" d208="1" d209="1" d210="1" d211="1" d212="1" d213="1" d214="1" d215="1" d216="1" d217="1" d218="1" d219="1" d220="1" d221="1" d222="1" d223="1" d224="1" d225="1" d226="1" d227="1" d228="1" d229="1" d230="1" d231="1" d232="1" d233="1" d234="1" d235="1" d236="1" d237="1" d238="1" d239="1" d240="1" d241="1" d242="1" d243="1" d244="1" d245="0" d246="0" d247="1" d248="1" d249="1" d250="1" d251="1" d252="1" d253="1" d254="1" d255="1" d256="1" d257="1" d258="1" d259="1" d260="1" d261="1" d262="2" d263="2" d264="2" d265="2" d266="2" d267="2" d268="2" d269="2" d270="2" d271="2" d272="2" d273="2" d274="2" d275="2" d276="2" d277="2" d278="2" d279="2" d280="2" d281="2" d282="2" d283="2" d284="2" d285="2" d286="2" d287="2" d288="2" d289="2" d290="2" d291="2" d292="2" d293="2" d294="2" d295="2" d296="2" d297="2" d298="2" d299="2" d300="2" d301="2" d302="2" d303="2" d304="2" d305="2" d306="2" d307="2" d308="2" d309="2" d310="2" d311="2" d312="2" d313="2" d314="2" d315="2" d316="2" d317="2" d318="2" d319="2" d320="2" d321="2" d322="2" d323="2" d324="2" d325="2" d326="2" d327="2" d328="2" d329="2" d330="2" d331="2" d332="2" d333="2" d334="2" d335="2" d336="2" d337="2" d338="2" d339="2" d340="2" d341="2" d342="2" d343="2" d344="2" d345="2" d346="2" d347="2" d348="2" d349="2" d350="2" d351="2" d352="2" d353="2" d354="2" d355="2" d356="2" d357="2" d358="2" d359="2" d360="2" d361="2" d362="2" d363="2" d364="2" d365="2" />
'''
for b in xrange(len(geometry)):
    xml += '''<Building Name="GROUP_1" id="'''+ str(b) + '''" key="1" Vi="1123.5" Ninf="0.15" BlindsLambda="0.2" BlindsIrradianceCutOff="100" Simulate="true">
            <HeatTank V="0.01" phi="20" rho="1000" Cp="4180" Tmin="20" Tmax="35"/>
			<CoolTank V="0.01" phi="20" rho="1000" Cp="4180" Tmin="5" Tmax="20"/>
			<HeatSource beginDay="1" endDay="365">
				<HeatPump Pmax="1000" eta_tech="0.3" Ttarget="55" Tsource="ground" depth="5" alpha="0.0700000003" position="vertical" z1="10" />
			</HeatSource>
			<CoolSource beginDay="1" endDay="365">
				<HeatPump Pmax="10000000" eta_tech="0.3" Ttarget="5" Tsource="ground" depth="5" alpha="0.0700000003" position="vertical" z1="10" />
			</CoolSource>
			<Zone id="1" volume="1123.5" psi="0.2" Tmin="21" Tmax="27" groundFloor="true" >
				<Occupants n="9" d="0.06" type="2"/>'''
    for s in xrange(len(geometry[b])):
        xml += '<Wall id="'+str(s)+'" type="21" ShortWaveReflectance="0.2" GlazingRatio="0.25" GlazingGValue="0.7" GlazingUValue="1.1" OpenableRatio="0">'
        srfpts = rs.SurfacePoints(geometry[b][s])
        for i in xrange(len(srfpts)):
            xml+= '<V' + str(i) + ' x="' + str(srfpts[i][0]) +'" y="' + str(srfpts[i][1]) +'" z="' + str(srfpts[i][2])+'"/> \n'
        xml+= '</Wall>'
    xml+= '''   </Zone>
            </Building>'''
xml+= ''' <ShadingSurface>
		</ShadingSurface>
		<Trees>
		</Trees>
		<GroundSurface>
			<Ground id="10000002" ShortWaveReflectance="0.2">
				<V0 x="15.00" y="10.00" z="0.00"/>
				<V1 x="0.00" y="20.00" z="0.00"/>
				<V2 x="0.00" y="10.00" z="0.00"/>
			</Ground>
			<Ground id="10000001" ShortWaveReflectance="0.2">
				<V0 x="15.00" y="10.00" z="0.00"/>
				<V1 x="7.49" y="20.00" z="0.00"/>
				<V2 x="0.00" y="20.00" z="0.00"/>
			</Ground>
			<Ground id="10000000" ShortWaveReflectance="0.2">
				<V0 x="15.00" y="10.00" z="0.00"/>
				<V1 x="7.49" y="30.00" z="0.00"/>
				<V2 x="7.49" y="20.00" z="0.00"/>
			</Ground>
		</GroundSurface>
	</District>
</CitySim> '''


out_file = open(path+name+".xml","w")
out_file.write(xml)
out_file.close()