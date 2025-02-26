import csv

dati = [
    ["Stagione", "Squadra", "Valore rosa"],
    ["2013-14", "Juventus", "391.45"],
    ["2013-14", "FC Internazionale Milano", "292.65"],
    ["2013-14", "SSC Napoli", "276.60"],
    ["2013-14", "AC Milan", "263.95"],
    ["2013-14", "ACF Fiorentina", "249.13"],
    ["2013-14", "AS Roma", "246.40"],
    ["2013-14", "SS Lazio", "162.95"],
    ["2013-14", "Udinese Calcio", "123.95"],
    ["2013-14", "Genoa CFC", "102.10"],
    ["2013-14", "Parma", "89.78"],
    ["2013-14", "US Sassuolo Calcio", "87.85"],
    ["2013-14", "Cagliari Calcio", "86.20"],
    ["2013-14", "UC Sampdoria", "83.48"],
    ["2013-14", "Torino FC", "80.25"],
    ["2013-14", "Calcio Catania", "78.98"],
    ["2013-14", "Atalanta", "73.93"],
    ["2013-14", "AS Livorno Calcio", "71.18"],
    ["2013-14", "Bologna FC", "69.83"],
    ["2013-14", "AC Chievo Verona", "69.08"],
    ["2013-14", "Hellas Verona", "67.13"],
    ["2014-15", "Juventus", "329.00"],
    ["2014-15", "AS Roma", "276.78"],
    ["2014-15", "SSC Napoli", "262.18"],
    ["2014-15", "FC Internazionale Milano", "260.70"],
    ["2014-15", "AC Milan", "236.13"],
    ["2014-15", "ACF Fiorentina", "216.13"],
    ["2014-15", "SS Lazio", "167.55"],
    ["2014-15", "UC Sampdoria", "132.23"],
    ["2014-15", "Genoa CFC", "117.33"],
    ["2014-15", "Udinese Calcio", "107.18"],
    ["2014-15", "Palermo", "92.60"],
    ["2014-15", "US Sassuolo Calcio", "91.03"],
    ["2014-15", "Atalanta", "83.48"],
    ["2014-15", "Torino FC", "82.58"],
    ["2014-15", "Cagliari Calcio", "74.20"],
    ["2014-15", "Parma", "65.95"],
    ["2014-15", "AC Chievo Verona", "61.85"],
    ["2014-15", "Empoli FC", "54.03"],
    ["2014-15", "Hellas Verona", "41.80"],
    ["2014-15", "AC Cesena", "34.15"],
    ["2015-16", "Juventus", "440.00"],
    ["2015-16", "AS Roma", "332.90"],
    ["2015-16", "SSC Napoli", "321.93"],
    ["2015-16", "FC Internazionale Milano", "294.28"],
    ["2015-16", "AC Milan", "213.83"],
    ["2015-16", "ACF Fiorentina", "190.53"],
    ["2015-16", "SS Lazio", "175.30"],
    ["2015-16", "UC Sampdoria", "126.53"],
    ["2015-16", "Genoa CFC", "117.55"],
    ["2015-16", "US Sassuolo Calcio", "97.00"],
    ["2015-16", "Udinese Calcio", "93.00"],
    ["2015-16", "Torino FC", "89.83"],
    ["2015-16", "Atalanta", "78.45"],
    ["2015-16", "Bologna FC", "75.23"],
    ["2015-16", "Empoli FC", "74.60"],
    ["2015-16", "Palermo", "68.68"],
    ["2015-16", "Carpi", "52.05"],
    ["2015-16", "AC Chievo Verona", "49.78"],
    ["2015-16", "Hellas Verona", "47.73"],
    ["2015-16", "Frosinone Calcio", "38.30"],
    ["Stagione", "Squadra", "Valore rosa"],
    ["2016-17", "Juventus", "497.18"],
    ["2016-17", "SSC Napoli", "387.30"],
    ["2016-17", "AS Roma", "354.68"],
    ["2016-17", "FC Internazionale Milano", "328.30"],
    ["2016-17", "AC Milan", "254.33"],
    ["2016-17", "SS Lazio", "226.45"],
    ["2016-17", "ACF Fiorentina", "217.08"],
    ["2016-17", "Torino FC", "162.35"],
    ["2016-17", "Atalanta", "161.70"],
    ["2016-17", "US Sassuolo Calcio", "145.25"],
    ["2016-17", "UC Sampdoria", "117.58"],
    ["2016-17", "Genoa CFC", "108.18"],
    ["2016-17", "Udinese Calcio", "101.95"],
    ["2016-17", "Bologna FC", "95.00"],
    ["2016-17", "Cagliari Calcio", "61.08"],
    ["2016-17", "Empoli FC", "55.45"],
    ["2016-17", "Pescara", "48.10"],
    ["2016-17", "AC Chievo Verona", "45.88"],
    ["2016-17", "Palermo", "41.10"],
    ["2016-17", "FC Crotone", "36.70"],
    ["2017-18", "Juventus", "653.15"],
    ["2017-18", "SSC Napoli", "504.25"],
    ["2017-18", "FC Internazionale Milano", "487.28"],
    ["2017-18", "AS Roma", "469.10"],
    ["2017-18", "SS Lazio", "408.78"],
    ["2017-18", "AC Milan", "407.05"],
    ["2017-18", "ACF Fiorentina", "237.33"],
    ["2017-18", "Atalanta", "207.95"],
    ["2017-18", "UC Sampdoria", "190.45"],
    ["2017-18", "Torino FC", "175.53"],
    ["2017-18", "Genoa CFC", "135.13"],
    ["2017-18", "US Sassuolo Calcio", "126.78"],
    ["2017-18", "Udinese Calcio", "108.03"],
    ["2017-18", "Bologna FC", "103.55"],
    ["2017-18", "Cagliari Calcio", "98.58"],
    ["2017-18", "SPAL", "63.55"],
    ["2017-18", "Benevento", "57.83"],
    ["2017-18", "Hellas Verona", "56.50"],
    ["2017-18", "AC Chievo Verona", "55.23"],
    ["2017-18", "FC Crotone", "47.88"],
    ["2018-19", "Juventus", "871.05"],
    ["2018-19", "SSC Napoli", "646.80"],
    ["2018-19", "FC Internazionale Milano", "617.93"],
    ["2018-19", "AC Milan", "578.48"],
    ["2018-19", "AS Roma", "459.05"],
    ["2018-19", "Atalanta", "367.68"],
    ["2018-19", "ACF Fiorentina", "315.33"],
    ["2018-19", "SS Lazio", "291.15"],
    ["2018-19", "US Sassuolo Calcio", "242.05"],
    ["2018-19", "Torino FC", "239.23"],
    ["2018-19", "UC Sampdoria", "216.75"],
    ["2018-19", "Udinese Calcio", "201.20"],
    ["2018-19", "Genoa CFC", "191.73"],
    ["2018-19", "Cagliari Calcio", "155.38"],
    ["2018-19", "Bologna FC", "119.68"],
    ["2018-19", "Empoli FC", "105.60"],
    ["2018-19", "SPAL", "97.40"],
    ["2018-19", "Parma", "95.75"],
    ["2018-19", "AC Chievo Verona", "54.70"],
    ["2018-19", "Frosinone Calcio", "54.53"],
    ["2019-20", "Juventus", "661.88"],
    ["2019-20", "FC Internazionale Milano", "606.05"],
    ["2019-20", "SSC Napoli", "548.28"],
    ["2019-20", "AC Milan", "404.33"],
    ["2019-20", "AS Roma", "392.73"],
    ["2019-20", "SS Lazio", "303.88"],
    ["2019-20", "ACF Fiorentina", "302.23"],
    ["2019-20", "Atalanta", "291.43"],
    ["2019-20", "US Sassuolo Calcio", "167.98"],
    ["2019-20", "Cagliari Calcio", "167.83"],
    ["2019-20", "Torino FC", "163.55"],
    ["2019-20", "Genoa CFC", "142.38"],
    ["2019-20", "UC Sampdoria", "135.28"],
    ["2019-20", "Bologna FC", "129.65"],
    ["2019-20", "Parma", "128.75"],
    ["2019-20", "Udinese Calcio", "121.08"],
    ["2019-20", "Hellas Verona", "112.53"],
    ["2019-20", "Brescia Calcio", "83.23"],
    ["2019-20", "SPAL", "73.63"],
    ["2019-20", "US Lecce", "52.33"],
    ["2020-21", "FC Internazionale Milano", "663.90"],
    ["2020-21", "Juventus", "633.30"],
    ["2020-21", "AC Milan", "547.78"],
    ["2020-21", "SSC Napoli", "530.20"],
    ["2020-21", "Atalanta", "430.00"],
    ["2020-21", "AS Roma", "395.65"],
    ["2020-21", "SS Lazio", "326.33"],
    ["2020-21", "ACF Fiorentina", "286.80"],
    ["2020-21", "US Sassuolo Calcio", "241.74"],
    ["2020-21", "Cagliari Calcio", "187.83"],
    ["2020-21", "Torino FC", "175.28"],
    ["2020-21", "Udinese Calcio", "173.00"],
    ["2020-21", "Hellas Verona", "157.21"],
    ["2020-21", "Bologna FC", "153.60"],
    ["2020-21", "Parma", "128.70"],
    ["2020-21", "UC Sampdoria", "127.18"],
    ["2020-21", "Genoa CFC", "111.93"],
    ["2020-21", "Spezia Calcio", "71.68"],
    ["2020-21", "FC Crotone", "52.75"],
    ["2020-21", "Benevento", "50.13"],
    ["2021-22", "Juventus", "642.50"],
    ["2021-22", "FC Internazionale Milano", "558.55"],
    ["2021-22", "AC Milan", "546.95"],
    ["2021-22", "SSC Napoli", "477.23"],
    ["2021-22", "Atalanta", "398.75"],
    ["2021-22", "AS Roma", "381.25"],
    ["2021-22", "ACF Fiorentina", "325.80"],
    ["2021-22", "SS Lazio", "264.53"],
    ["2021-22", "US Sassuolo Calcio", "251.00"],
    ["2021-22", "Torino FC", "223.40"],
    ["2021-22", "Bologna FC", "186.20"],
    ["2021-22", "Hellas Verona", "162.98"],
    ["2021-22", "Udinese Calcio", "142.30"],
    ["2021-22", "Cagliari Calcio", "134.53"],
    ["2021-22", "UC Sampdoria", "128.55"],
    ["2021-22", "Empoli FC", "126.50"],
    ["2021-22", "Genoa CFC", "121.28"],
    ["2021-22", "Venezia FC", "80.98"],
    ["2021-22", "Spezia Calcio", "78.50"],
    ["2021-22", "Salernitana", "70.56"],
    ["2022-23", "SSC Napoli", "654.08"],
    ["2022-23", "FC Internazionale Milano", "567.55"],
    ["2022-23", "AC Milan", "545.10"],
    ["2022-23", "Juventus", "483.13"],
    ["2022-23", "AS Roma", "361.38"],
    ["2022-23", "Atalanta", "338.38"],
    ["2022-23", "SS Lazio", "266.43"],
    ["2022-23", "ACF Fiorentina", "258.80"],
    ["2022-23", "US Sassuolo Calcio", "232.20"],
    ["2022-23", "Torino FC", "197.19"],
    ["2022-23", "Udinese Calcio", "188.86"],
    ["2022-23", "Bologna FC", "153.63"],
    ["2022-23", "AC Monza", "135.70"],
    ["2022-23", "Empoli FC", "125.53"],
    ["2022-23", "Hellas Verona", "123.89"],
    ["2022-23", "Salernitana", "118.35"],
    ["2022-23", "Spezia Calcio", "115.81"],
    ["2022-23", "US Lecce", "105.20"],
    ["2022-23", "US Cremonese", "83.78"],
    ["2022-23", "UC Sampdoria", "82.96"],
    ["2023-24", "FC Internazionale Milano", "654.85"],
    ["2023-24", "AC Milan", "571.41"],
    ["2023-24", "SSC Napoli", "515.00"],
    ["2023-24", "Juventus", "504.50"],
    ["2023-24", "Atalanta", "436.05"],
    ["2023-24", "Bologna FC", "349.30"],
    ["2023-24", "AS Roma", "339.90"],
    ["2023-24", "ACF Fiorentina", "283.60"],
    ["2023-24", "Torino FC", "232.70"],
    ["2023-24", "SS Lazio", "225.40"],
    ["2023-24", "Genoa CFC", "195.40"],
    ["2023-24", "Udinese Calcio", "169.06"],
    ["2023-24", "AC Monza", "143.43"],
    ["2023-24", "Hellas Verona", "140.70"],
    ["2023-24", "US Sassuolo Calcio", "139.54"],
    ["2023-24", "Frosinone Calcio", "108.13"],
    ["2023-24", "US Lecce", "107.73"],
    ["2023-24", "Empoli FC", "102.33"],
    ["2023-24", "Salernitana", "94.60"],
    ["2023-24", "Cagliari Calcio", "92.23"],
    ["2023-24", "FC Internazionale Milano", "684.55"],
    ["2023-24", "AC Milan", "585.65"],
    ["2023-24", "Juventus", "531.90"],
    ["2023-24", "SSC Napoli", "463.08"],
    ["2023-24", "Atalanta", "418.60"],
    ["2023-24", "AS Roma", "336.00"],
    ["2023-24", "Bologna FC", "254.00"],
    ["2023-24", "ACF Fiorentina", "252.70"],
    ["2023-24", "SS Lazio", "229.83"],
    ["2023-24", "Torino FC", "173.10"],
    ["2023-24", "Genoa CFC", "153.50"],
    ["2023-24", "Udinese Calcio", "149.83"],
    ["2023-24", "US Lecce", "90.70"],
    ["2023-24", "Parma", "85.40"],
    ["2023-24", "Como 1907", "84.78"],
    ["2023-24", "AC Monza", "81.98"],
    ["2023-24", "Cagliari Calcio", "69.45"],
    ["2023-24", "Hellas Verona", "59.15"],
    ["2023-24", "Venezia FC", "53.10"],
    ["2023-24", "Empoli FC", "51.83"],
]

def get_market_value(year, team):
    for row in dati:
        if row[0] == f'{year}-{(year+1)%2000}' and row[1] == team:
            return row[2]
    return None

def get_max_market_value(year):
    max_value = 0
    for row in dati:
        if row[0] == f'{year}-{(year+1)%2000}' and float(row[2]) > max_value:
            max_value = float(row[2])
    return max_value