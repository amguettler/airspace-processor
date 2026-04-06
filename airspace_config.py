import re

airsport_areas = {
    'Oslo TMA' : ['STARMOEN', 'HOKKSUND', 'EGGEMOEN', 'EINA', 'SUNNVOLLEN', 'HVITTINGFOSS'],
    'Farris TMA' : ['HVITTINGFOSS', 'GVARV', 'LUNDE', 'DRANGEDAL', 'BOE', 'BØ', 
                    'TOKKE', 'NOTODDEN VEST'],
    'Flesland TMA' : ['GULLFJELLET GLIDER AREA', 'KVAM TRANSIT AREA'],
    'WestCoast TMA' : ['KVAM TRANSIT AREA', 'GULLFJELLET GLIDER AREA'],
    'Værnes TMA' : ['MERÅKER'],
    'Polaris CTA' : ['Bjorli', 'Lesja', 'Dovre', 'Oppdal',
                     'Vågå', 'Rondane', 'Ringebu', 'Jotunheimen'
                     ],
    }

airspace_frequencies = {
    'D117 Bø' : ('124.355', 'Farris Approach'),
    'D118 Drangedal' : ('124.355', 'Farris Approach'),
    'D119 Hvittingfoss A' : ('124.355', 'Farris Approach'),
    'D120 Hvittingfoss B' : ('124.355', 'Farris Approach'),
    'D123 Lunde' : ('124.355', 'Farris Approach'),
    'D133 Hvittingfoss C' : ('124.355', 'Farris Approach'),
    'D121 Hvittingfoss D' : ('124.355', 'Farris Approach'),
    'D122 Hvittingfoss E' : ('124.355', 'Farris Approach'),
    'D124 Notodden Vest' : ('124.355', 'Farris Approach'),
#    'D125 Tinnsjø' : ('124.355', 'Farris Approach'),
    'D126 Tokke' : ('124.355', 'Farris Approach'),
    'D127 Eggemoen A' : ('120.455', 'Oslo Approach'),
    'D128 Eggemoen B' : ('120.455', 'Oslo Approach'),
    'D129 Eina A' : ('120.455', 'Oslo Approach'),
    'D130 Eina B' : ('120.455', 'Oslo Approach'),
    'D131 Hokksund A' : ('120.455', 'Oslo Approach'),
    'D132 Hokksund B' : ('120.455', 'Oslo Approach'),
    'D134 Starmoen A' : ('118.480', 'Oslo Approach'),
    'D135 Starmoen B1' : ('118.480', 'Oslo Approach'),
    'D136 Starmoen B2' : ('118.480', 'Oslo Approach'),
    'D137 Starmoen C' : ('118.480', 'Oslo Approach'),
    'D138 Starmoen D' : ('118.480', 'Oslo Approach'),
    'D139 Starmoen F' : ('120.455', 'Oslo Approach'),
    'D140 Starmoen G1 Hamar' : ('118.480', 'Oslo Approach'),
    'D141 Starmoen G2 Elverum' : ('118.480', 'Oslo Approach'),
    'D142 Starmoen H' : ('118.480', 'Oslo Approach'),
    'D143 Sunnvollen' : ('120.455', 'Oslo Approach'),
    'D161 Ringebu' : ('124.780', 'Polaris Control'),
    'D162 Rondane' : ('124.780', 'Polaris Control'),
    'D163 Vågå' : ('124.780', 'Polaris Control'),
    'D166 Jotunheimen' : ('124.780', 'Polaris Control'),
    'D357 Oppdal' : ('125.705', 'Polaris Control'),
    'D358 Dovre' : ('125.705', 'Polaris Control'),
    'D359 Lesja' : ('125.705', 'Polaris Control'),
    'D360 Bjorli' : ('125.705', 'Polaris Control'),
    'Airwork A' : ('118.480', 'Oslo Approach'),
    'Airwork B' : ('118.480', 'Oslo Approach'),
    'Airwork C' : ('118.480', 'Oslo Approach'),
    'Airwork E' : ('118.480', 'Oslo Approach'),
    'Airwork F' : ('118.480', 'Oslo Approach'),
    'Alta TMA' : ('120.405', 'Alta Tower'),
    'Anda TIZ' : ('119.805', 'Anda Information'),
    'Andøya TMA' : ('118.205', 'Andøya Tower'),
    'Banak CTR' : ('118.905', 'Banak Tower'),   # Lakselv
    'Bardufoss TMA' : ('118.805', 'Bardufoss Approach'),
#    'Bergen Lufthavn Flesland' : ('119.100', 'Flesland Tower'),
    'Berlevåg TIZ' : ('120.105', 'Berlevåg Information'),
    'Bodø CTR' : ('118.100', 'Bodø Tower'),
#    'Bodø Lufthavn' : ('118.100', 'Bodø Tower'),
    'Bodø TMA' : ('119.707', 'Bodø Approach'),
    'Bondalen N' : ('119.355', 'Møre Approach'),
    'Bondalen S' : ('119.355', 'Møre Approach'),
    'Bringeland TIZ' : ('118.455', 'Bringeland Information'),  # Førde
    'Brønnøy TIZ' : ('119.605', 'Brønnøy Information'),
    'Båtsfjord TIZ' : ('123.405', 'Båtsfjord Information'),
    'Østre Æra' : ('120.905', 'Østre Æra Traffic'),
    'Etne' : ('124.780', 'Polaris Control'),
    'Evenes CTR' : ('118.005', 'Evenes Tower'),
    'Evenes TMA' : ('120.105', 'Evenes Approach'),
    'Fagerhaug' : ('119.210', 'Fagerhaug Traffic'),   # Oppdal
    'Farris TMA' : ('124.355', 'Farris Approach'),
    'Finnmark TIA' : ('126.705', 'Finmark Information'),
    'Flesland CTR' : ('119.100', 'Flesland Tower'),
    'Flesland TMA 2' : ('126.100', 'Flesland Approach'),
    'Flesland TMA 3' : ('126.100', 'Flesland Approach'),
    'Flesland TMA 4' : ('126.100', 'Flesland Approach'),
    'Flesland TMA 5' : ('126.100', 'Flesland Approach'),
    'Flesland TMA 6' : ('121.000', 'Flesland Approach'),
    'Flesland TMA 7' : ('121.000', 'Flesland Approach'),
    'Flesland TMA 8' : ('121.000', 'Flesland Approach'),
    'Flesland TMA 9' : ('121.000', 'Flesland Approach'),
    'Flesland TMA 10' : ('126.100', 'Flesland Approach'),
    'Flesland TMA 11' : ('126.100', 'Flesland Approach'),
    'Florø TIZ' : ('119.205', 'Florø Information'),
    'Gullfjellet Glider Area' : ('126.100', 'Flesland Approach'),
    'Gardermoen CTR' : ('120.105', 'Oslo Tower'),
#    'Hamar Flyplass' : ('130.280', 'Hamar Traffic'),
    'Hammerfest TIZ' : ('121.005', 'Hammerfest Information'),
    'Hammerfest TMA' : ('126.705', 'Polaris Control'),
    'Hasvik TIZ' : ('119.905', 'Hasvik Information'),
    'Helgeland TMA' : ('127.905', 'Polaris Control'),
    'Helle TIZ' : ('120.205', 'Helle Information'),     # Svolvær
    'Hoppfelt Bømoen' : ('123.065', 'Bømoen Traffic'),  # Voss
    'Hovden TIZ' : ('118.905', 'Hovden Information'),   # Ørsta/Volda
#    'Jarlsberg' : ('122.300', 'Jarlsberg Traffic'),
    'Kvam Transit Area' : ('126.100', 'Flesland Approach'),
    'Karmøy CTR' : ('120.505', 'Karmøy Tower'),   # Haugesund
    'Kirkenes CTR' : ('120.355', 'Kirkenes Tower'),
    'Kirkenes Centre TMA' : ('120.355', 'Kirkenes Approach'),
    'Kirkenes TMA' : ('120.355', 'Kirkenes Approach'),
    'Kirkenes West TMA' : ('120.355', 'Kirkenes Approach'),
    'Kjevik CTR' : ('119.950', 'Kjevik Approach'),
    'Kjevik TMA' : ('119.950', 'Kjevik Approach'),
#    'Kristiansand Lufthavn Kjevik' : ('119.950', 'Kjevik Tower'),
    'Kvernberget CTR' : ('118.305', 'Kvernberget Tower'),   # Kristiansund
    'Leknes TIZ' : ('120.505', 'Leknes Information'),
    'Lesja/Bjorli Flyplass' : ('123.065', 'Bjorli Traffic'),
    'Lofoten TMA' : ('126.455', 'Polaris Control'),
    'Mehamn TIZ' : ('121.205', 'Mehamn Information'),
#    'Molde Lufthavn Årø' : ('119.950', 'Molde Information'),
    'Molde TIZ' : ('119.955', 'Molde Information'),
    'Mosjøen TIZ' : ('123.405', 'Mosjøen Information'),
    'Møre TMA' : ('119.355', 'Møre Approach'),
    'Namsos TIA' : ('118.555', 'Polaris Control'),
    'Namsos TIZ' : ('119.905', 'Namsos Information'),
    'Notodden TIZ' : ('118.805', 'Notodden Information'),
    'Oslo TMA' : ('118.480', 'Oslo Approach'),
    'Oslo TMA 2' : ('120.455', 'Oslo Approach'),
    'Oslo TMA 3' : ('118.480', 'Oslo Approach'),
    'Oslo TMA 4' : ('120.455', 'Oslo Approach'),
    'Oslo TMA 5' : ('118.480', 'Oslo Approach'),
    'Oslo TMA 6' : ('118.480', 'Oslo Approach'),
    'Oslo TMA 7' : ('118.480', 'Oslo Approach'),
    'Polaris S1' : ('118.830', 'Polaris Control'),
    'Polaris S2' : ('126.630', 'Polaris Control'),
    'Polaris S3' : ('125.055', 'Polaris Control'),
    'Polaris S4' : ('118.880', 'Polaris Control'),
    'Polaris S5' : ('127.255', 'Polaris Control'),
    'Polaris S6' : ('120.380', 'Polaris Control'),
    'Polaris S7' : ('124.780', 'Polaris Control'),
    'Polaris S8' : ('134.355', 'Polaris Control'),
    'Polaris S9' : ('120.655', 'Polaris Control'),
    'Polaris S10' : ('136.280', 'Polaris Control'),
    'Polaris S11' : ('136.280', 'Polaris Control'),
    'Polaris S12' : ('120.655', 'Polaris Control'),
    'Polaris S13' : ('134.930', 'Polaris Control'),
    'Polaris S14' : ('124.580', 'Polaris Control'),
    'Polaris S15' : ('135.680', 'Polaris Control'),
    'Polaris S16' : ('135.680', 'Polaris Control'),
    'Polaris S17' : ('124.705', 'Polaris Control'),
    'Polaris S18' : ('125.705', 'Polaris Control'),
    'Polaris S19' : ('131.105', 'Polaris Control'),
    'Rena EAST' : ('134.810', 'Rena Traffic'),
    'Rena MID' : ('134.810', 'Rena Traffic'),
    'Rena WEST' : ('134.810', 'Rena Traffic'),
    'Rognan Flyplass' : ('123.065', 'Rognan Traffic'),   # Saltdal
    'Rygge CTR' : ('119.505', 'Rygge Tower'),
#    'Rygge Flystasjon' : ('119.505', 'Rygge Tower'),
    'Røros TIA' : ('131.105', 'Polaris Control'),
    'Røros TIZ' : ('120.405', 'Røros Information'),
    'Rørvik TIZ' : ('119.805', 'Rørvik Information'),
    'Røssvoll TIZ' : ('119.955', 'Røssvoll Information'),   # Mo i Rana
    'Røst TIZ' : ('119.255', 'Røst Information'),
    'Skagen TIZ' : ('120.455', 'Skagen Information'),  # Stokkmarknes
    'Sogn TIA' : ('124.705', 'Polaris Control'),
    'Sogndal TIZ' : ('119.305', 'Sogndal Information'),
    'Sola CTR' : ('118.355', 'Sola Tower'),
    'Sola TMA' : ('119.605', 'Sola Approach'),
    'Stokka TIZ' : ('120.305', 'Stokka Information'),   # Sandnessjøen
    'Sørkjosen TIA' : ('126.705', 'Polaris Control'),
    'Sørkjosen TIZ' : ('119.605', 'Sørkjosen Information'),
    'Sørstokken TIZ' : ('120.205', 'Sørstokken Information'),   # Stord
    'Sälen TMA' : ('124.460', 'Sälen Tower (RMZ 118.825 when TWR closed)'),
    'Torp CTR' : ('118.655', 'Torp Tower'),
    'Tromsø CTR' : ('118.305', 'Tromsø Tower'),
#    'Tromsø Lufthavn' : ('118.300', 'Tromsø Tower'),
    'Tromsø TMA' : ('123.755', 'Tromsø Approach'),
    'Vadsø TIZ' : ('118.405', 'Vadsø Information'),
    'Valan TIZ' : ('119.805', 'Valan Information'),  # Honningsvåg
    'Vardø TIZ' : ('122.155', 'Vardø Information'),
    'Vigra CTR' : ('118.105', 'Vigra Tower'),  # Ålesund
    'Værnes CTR' : ('119.405', 'Værnes Tower'),
    'Værnes TMA' : ('118.605', 'Værnes Approach'),
#    'Ålesund Lufthavn Vigra' : ('119.850', 'Vigra Tower'),
    'Ørland CTR' : ('118.705', 'Ørland Tower'),
    'Ørland TMA' : ('118.255', 'Ørland Approach'),
    'Østre Æra Flyplass' : ('120.905', 'Østra Æra Traffic')
}

REMOVE_AIRSPACES = [
    'EN D105 Rena',     # Replaced by our own Rena West, Mid and East
    'Bømoen Flyplass',  # Replaced by our own Hoppfelt Bømoen,
    'EN D201 Ulven'     # Already have a danger area for 'Ulven'
]

DANGER_PREFIX = re.compile(r'EN D\d\d\d ')
AIRSPACE_NAME = re.compile(r'((.*)(TMA|CTA|TIA|TIZ|CTR)\s+(\d*))')
def lookup_frequency(name):
    # Look up frequency in our table, from most specific to least
    if name in airspace_frequencies:   # We have frequency for exact airspace name
        return *airspace_frequencies[name],name
    
    if DANGER_PREFIX.match(name):
        # Try without the EN DXXX prefix
        name = name[8:]
        if name in airspace_frequencies:
            return *airspace_frequencies[name],name

    # For e.g. Farris TMA 3 West try in order: "Farris TMA 3", then "Farris TMA"
    if match := AIRSPACE_NAME.match(name):
        if match.group(1) in airspace_frequencies:
            return *airspace_frequencies[name],match.group(1)
        else:
            name = match.group(2) + match.group(3)
            return *airspace_frequencies.get(name, (None,None)),name

    return None,None,None
