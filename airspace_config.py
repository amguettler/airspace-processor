import re

airsport_areas = {
    'Oslo TMA' : ['STARMOEN', 'HOKKSUND', 'EGGEMOEN', 'EINA', 'SUNNVOLLEN', 'HVITTINGFOSS'],
    'Farris TMA' : ['HVITTINGFOSS', 'GVARV', 'LUNDE', 'DRANGEDAL', 'BOE', 'BØ', 
                    'TINNSJØ', 'TOKKE', 'NOTODDEN VEST'],
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
    'D125 Tinnsjø' : ('124.355', 'Farris Approach'),
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
    'D357 Oppdal' : ('125.700', 'Polaris Control'),
    'D358 Dovre' : ('125.700', 'Polaris Control'),
    'D359 Lesja' : ('125.700', 'Polaris Control'),
    'D360 Bjorli' : ('125.700', 'Polaris Control'),
    'Airwork A' : ('118.480', 'Oslo Approach'),
    'Airwork B' : ('118.480', 'Oslo Approach'),
    'Airwork C' : ('118.480', 'Oslo Approach'),
    'Airwork E' : ('118.480', 'Oslo Approach'),
    'Airwork F' : ('118.480', 'Oslo Approach'),
    'Alta TMA' : ('120.400', 'Alta Approach'),
    'Anda TIZ' : ('119.800', 'Anda Information'),
    'Andøya TMA' : ('118.200', 'Andøya Approach'),
    'Banak CTR' : ('118.900', 'Banak Tower'),
    'Bardufoss TMA' : ('118.800', 'Bardufoss Approach'),
#    'Bergen Lufthavn Flesland' : ('119.100', 'Flesland Tower'),
    'Berlevåg TIZ' : ('120.100', 'Berlevåg Information'),
    'Bodø CTR' : ('118.100', 'Bodø Tower'),
#    'Bodø Lufthavn' : ('118.100', 'Bodø Tower'),
    'Bodø TMA' : ('119.700', 'Bodø Approach'),
    'Bondalen N' : ('129.325', 'Møre Approach'),
    'Bondalen S' : ('129.325', 'Møre Approach'),
    'Bringeland TIZ' : ('118.450', 'Bringeland Information'),
    'Brønnøy TIZ' : ('119.600', 'Brønnøy Information'),
    'Båtsfjord TIZ' : ('123.400', 'Båtsfjord Information'),
    'Østre Æra' : ('121.350', 'Østre Æra Traffic'),
    'Etne' : ('124.780', 'Polaris Control'),
    'Evenes CTR' : ('119.900', 'Evenes Tower'),
    'Evenes TMA' : ('118.000', 'Evenes Approach'),
    'Fagerhaug' : ('123.500', 'Fagerhaug Traffic'),
    'Farris TMA' : ('124.355', 'Farris Approach'),
    'Finnmark TIA' : ('126.700', 'Finmark Information'),
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
    'Florø TIZ' : ('119.200', 'Florø Information'),
    'Gullfjellet Glider Area' : ('126.100', 'Flesland Approach'),
    'Gardermoen CTR' : ('120.105', 'Oslo Tower'),
#    'Hamar Flyplass' : ('130.275', 'Hamar Traffic'),
    'Hammerfest TIZ' : ('121.000', 'Hammerfest Information'),
    'Hammerfest TMA' : ('126.700', 'Hammerfest Approach'),
    'Hasvik TIZ' : ('119.900', 'Hasvik Information'),
    'Helgeland TMA' : ('127.900', 'Helgeland Approach'),
    'Helle TIZ' : ('120.200', 'Helle Information'),
    'Hoppfelt Bømoen' : ('123.500', 'Bømoen Traffic'),
    'Hovden TIZ' : ('118.900', 'Hovden Information'),
#    'Jarlsberg' : ('122.300', 'Jarlsberg Traffic'),
    'Kvam Transit Area' : ('126.100', 'Flesland Approach'),
    'Karmøy CTR' : ('120.505', 'Karmøy Tower'),
    'Kirkenes CTR' : ('120.350', 'Kirkenes Tower'),
    'Kirkenes Centre TMA' : ('120.350', 'Kirkenes Approach'),
    'Kirkenes TMA' : ('120.350', 'Kirkenes Approach'),
    'Kirkenes West TMA' : ('120.350', 'Kirkenes Approach'),
    'Kjevik CTR' : ('119.950', 'Kjevik Approach'),
    'Kjevik TMA' : ('119.950', 'Kjevik Approach'),
#    'Kristiansand Lufthavn Kjevik' : ('119.950', 'Kjevik Tower'),
    'Kvernberget CTR' : ('121.200', 'Kvernberget Tower'),
    'Leknes TIZ' : ('120.500', 'Leknes Information'),
    'Lesja/Bjorli Flyplass' : ('123.500', 'Bjorli Traffic'),
    'Lofoten TMA' : ('125.450', 'Lofoten Approach'),
    'Mehamn TIZ' : ('121.200', 'Mehamn Information'),
#    'Molde Lufthavn Årø' : ('119.950', 'Molde Information'),
    'Molde TIZ' : ('119.950', 'Molde Information'),
    'Mosjøen TIZ' : ('123.400', 'Mosjøen Information'),
    'Møre TMA' : ('119.350', 'Møre Approach'),
    'Namsos TIA' : ('118.550', 'Polaris Control'),
    'Namsos TIZ' : ('119.900', 'Namsos Information'),
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
    'Polaris S18' : ('125.700', 'Polaris Control'),
    'Polaris S19' : ('131.100', 'Polaris Control'),
    'Rena EAST' : ('135.300', 'Rena Traffic'),
    'Rena MID' : ('135.300', 'Rena Traffic'),
    'Rena WEST' : ('135.300', 'Rena Traffic'),
    'Rognan Flyplass' : ('123.500', 'Rognan Traffic'),
    'Rygge CTR' : ('119.505', 'Rygge Tower'),
#    'Rygge Flystasjon' : ('119.505', 'Rygge Tower'),
    'Røros TIA' : ('131.100', 'Polaris Control'),
    'Røros TIZ' : ('120.400', 'Røros Information'),
    'Rørvik TIZ' : ('119.800', 'Rørvik Information'),
    'Røssvoll TIZ' : ('119.950', 'Røssvoll Information'),
    'Røst TIZ' : ('119.250', 'Røst Information'),
    'Skagen TIZ' : ('120.455', 'Skagen Information'),
    'Sogn TIA' : ('124.705', 'Polaris Control'),
    'Sogndal TIZ' : ('119.300', 'Sogndal Information'),
    'Sola CTR' : ('118.355', 'Sola Tower'),
    'Sola TMA' : ('119.605', 'Sola Approach'),
    'Stokka TIZ' : ('120.300', 'Stokka Information'),
    'Sørkjosen TIA' : ('126.700', 'Polaris Control'),
    'Sørkjosen TIZ' : ('119.600', 'Sørkjosen Information'),
    'Sørstokken TIZ' : ('120.200', 'Sørstokken Information'),
    'Sälen TMA' : ('124.460', 'Sälen Tower (RMZ 118.825 when TWR closed)'),
    'Torp CTR' : ('118.655', 'Torp Tower'),
    'Tromsø CTR' : ('118.300', 'Tromsø Tower'),
#    'Tromsø Lufthavn' : ('118.300', 'Tromsø Tower'),
    'Tromsø TMA' : ('123.750', 'Tromsø Approach'),
    'Vadsø TIZ' : ('118.400', 'Vadsø Information'),
    'Valan TIZ' : ('119.800', 'Valan Information'),
    'Vardø TIZ' : ('122.150', 'Vardø Information'),
    'Vigra CTR' : ('119.850', 'Vigra Tower'),
    'Værnes CTR' : ('118.600', 'Værnes Tower'),
    'Værnes TMA' : ('118.600', 'Værnes Approach'),
#    'Ålesund Lufthavn Vigra' : ('119.850', 'Vigra Tower'),
    'Ørland CTR' : ('118.700', 'Ørland Tower'),
    'Ørland TMA' : ('118.250', 'Ørland Approach'),
    'Østre Æra Flyplass' : ('121.350', 'Østra Æra Traffic')
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
