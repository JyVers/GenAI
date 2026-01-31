from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo", json_response=True)

european_cities_data = {
    "Zurich": {
        "country": "Switzerland",
        "city_no": 1,
        "years": {
            2012: {"N": 2, "C": 3, "D": 1},
            2013: {"N": 1, "C": 4, "D": 3},
            2014: {"N": 2, "C": 3, "D": 1},
            2015: {"N": 1, "C": 3, "D": 2},
            2016: {"N": 2, "C": 4, "D": 2}
        },
        "sensitivity": 95.44
    },
    "Frankfurt": {
        "country": "Germany",
        "city_no": 2,
        "years": {
            2012: {"N": 1, "C": 1, "D": 0},
            2013: {"N": 2, "C": 2, "D": 0}
        },
        "sensitivity": 100.00
    },
    "Munich": {
        "country": "Germany",
        "city_no": 3,
        "years": {
            2012: {"N": 3, "C": 5, "D": 2},
            2013: {"N": 3, "C": 15, "D": 12},
            2014: {"N": 4, "C": 6, "D": 2}
        },
        "sensitivity": 85.34
    },
    "Edinburgh": {
        "country": "United Kingdom",
        "city_no": 4,
        "years": {
            2012: {"N": 4, "C": 1, "D": 3},
            2013: {"N": 1, "C": 1, "D": 0}
        },
        "sensitivity": 95.97
    },
    "Trondheim": {
        "country": "Norway",
        "city_no": 5,
        "years": {
            2012: {"N": 3, "C": 1, "D": 2},
            2013: {"N": 6, "C": 3, "D": 3},
            2014: {"N": 4, "C": 2, "D": 2},
            2015: {"N": 5, "C": 4, "D": 1}
        },
        "sensitivity": 94.87
    },
    "Geneva": {
        "country": "Switzerland",
        "city_no": 6,
        "years": {
            2012: {"N": 6, "C": 10, "D": 4},
            2013: {"N": 5, "C": 5, "D": 0}
        },
        "sensitivity": 94.63
    },
    "Vienna": {
        "country": "Austria",
        "city_no": 7,
        "years": {
            2012: {"N": 7, "C": 12, "D": 5},
            2013: {"N": 7, "C": 20, "D": 13},
            2014: {"N": 3, "C": 8, "D": 5}
        },
        "sensitivity": 82.31
    },
    "Copenhagen": {
        "country": "Denmark",
        "city_no": 8,
        "years": {
            2012: {"N": 5, "C": 4, "D": 1},
            2013: {"N": 9, "C": 7, "D": 2},
            2014: {"N": 5, "C": 5, "D": 0},
            2015: {"N": 8, "C": 7, "D": 1},
            2016: {"N": 6, "C": 5, "D": 1}
        },
        "sensitivity": 97.23
    },
    "Stockholm": {
        "country": "Sweden",
        "city_no": 9,
        "years": {
            2012: {"N": 4, "C": 6, "D": 2},
            2013: {"N": 8, "C": 9, "D": 1},
            2014: {"N": 8, "C": 10, "D": 2},
            2015: {"N": 9, "C": 17, "D": 8},
            2016: {"N": 13, "C": 24, "D": 11}
        },
        "sensitivity": 85.43
    },
    "Berlin": {
        "country": "Germany",
        "city_no": 10,
        "years": {
            2012: {"N": 1, "C": 2, "D": 1},
            2013: {"N": 2, "C": 2, "D": 0},
            2014: {"N": 6, "C": 6, "D": 0},
            2015: {"N": 10, "C": 11, "D": 1}
        },
        "sensitivity": 98.29
    },
    "Trieste": {
        "country": "Italy",
        "city_no": 11,
        "years": {
            2012: {"N": 11, "C": 5, "D": 6}
        },
        "sensitivity": 89.47
    },
    "Glasgow": {
        "country": "United Kingdom",
        "city_no": 12,
        "years": {
            2012: {"N": 12, "C": 6, "D": 6}
        },
        "sensitivity": 89.47
    },
    "Helsinki": {
        "country": "Finland",
        "city_no": 13,
        "years": {
            2012: {"N": 13, "C": 16, "D": 3},
            2013: {"N": 10, "C": 11, "D": 1}
        },
        "sensitivity": 95.76
    },
    "Amsterdam": {
        "country": "Netherlands",
        "city_no": 14,
        "years": {
            2012: {"N": 14, "C": 9, "D": 5},
            2013: {"N": 7, "C": 7, "D": 0}
        },
        "sensitivity": 93.29
    },
    "Bristol": {
        "country": "United Kingdom",
        "city_no": 15,
        "years": {
            2012: {"N": 15, "C": 24, "D": 9}
        },
        "sensitivity": 84.21
    },
    "Hamburg": {
        "country": "Germany",
        "city_no": 16,
        "years": {
            2012: {"N": 4, "C": 14, "D": 10},
            2013: {"N": 16, "C": 12, "D": 4},
            2014: {"N": 8, "C": 9, "D": 1}
        },
        "sensitivity": 87.14
    },
    "Oslo": {
        "country": "Norway",
        "city_no": 17,
        "years": {
            2012: {"N": 10, "C": 12, "D": 2},
            2013: {"N": 9, "C": 8, "D": 1},
            2014: {"N": 17, "C": 13, "D": 4},
            2015: {"N": 25, "C": 17, "D": 8}
        },
        "sensitivity": 90.01
    },
    "Valencia": {
        "country": "Spain",
        "city_no": 18,
        "years": {
            2012: {"N": 18, "C": 14, "D": 4}
        },
        "sensitivity": 92.98
    },
    "Gdansk": {
        "country": "Poland",
        "city_no": 19,
        "years": {
            2012: {"N": 19, "C": 18, "D": 1}
        },
        "sensitivity": 98.25
    },
    "Tallinn": {
        "country": "Estonia",
        "city_no": 20,
        "years": {
            2012: {"N": 11, "C": 10, "D": 1},
            2013: {"N": 10, "C": 14, "D": 4},
            2014: {"N": 20, "C": 22, "D": 2},
            2015: {"N": 17, "C": 12, "D": 5}
        },
        "sensitivity": 92.65
    },
    "Ljubljana": {
        "country": "Slovenia",
        "city_no": 21,
        "years": {
            2012: {"N": 7, "C": 12, "D": 5},
            2013: {"N": 15, "C": 18, "D": 3},
            2014: {"N": 15, "C": 16, "D": 1},
            2015: {"N": 21, "C": 21, "D": 0}
        },
        "sensitivity": 92.85
    },
    "Sevilla": {
        "country": "Spain",
        "city_no": 22,
        "years": {
            2012: {"N": 22, "C": 23, "D": 1}
        },
        "sensitivity": 98.25
    },
    "Prague": {
        "country": "Czech Republic",
        "city_no": 23,
        "years": {
            2012: {"N": 12, "C": 13, "D": 1},
            2013: {"N": 18, "C": 21, "D": 3},
            2014: {"N": 12, "C": 19, "D": 7},
            2015: {"N": 23, "C": 28, "D": 5},
            2016: {"N": 16, "C": 26, "D": 10}
        },
        "sensitivity": 85.81
    },
    "Dublin": {
        "country": "Ireland",
        "city_no": 24,
        "years": {
            2012: {"N": 6, "C": 5, "D": 1},
            2013: {"N": 13, "C": 8, "D": 5},
            2014: {"N": 13, "C": 7, "D": 6},
            2015: {"N": 24, "C": 8, "D": 16},
            2016: {"N": 24, "C": 19, "D": 5}
        },
        "sensitivity": 80.63
    },
    "Brno": {
        "country": "Czech Republic",
        "city_no": 25,
        "years": {
            2012: {"N": 11, "C": 11, "D": 0},
            2013: {"N": 19, "C": 15, "D": 4},
            2014: {"N": 16, "C": 15, "D": 1},
            2015: {"N": 25, "C": 29, "D": 4},
            2016: {"N": 12, "C": 13, "D": 1}
        },
        "sensitivity": 93.90
    },
    "Vilnius": {
        "country": "Lithuania",
        "city_no": 26,
        "years": {
            2012: {"N": 14, "C": 17, "D": 3},
            2013: {"N": 11, "C": 17, "D": 6},
            2014: {"N": 26, "C": 35, "D": 9},
            2015: {"N": 31, "C": 32, "D": 1}
        },
        "sensitivity": 87.79
    },
    "Thessaloniki": {
        "country": "Greece",
        "city_no": 27,
        "years": {
            2012: {"N": 20, "C": 18, "D": 2},
            2013: {"N": 32, "C": 29, "D": 3},
            2014: {"N": 23, "C": 21, "D": 2},
            2015: {"N": 27, "C": 26, "D": 1},
            2016: {"N": 20, "C": 14, "D": 6}
        },
        "sensitivity": 92.31
    },
    "Porto": {
        "country": "Portugal",
        "city_no": 28,
        "years": {
            2012: {"N": 9, "C": 7, "D": 2},
            2013: {"N": 17, "C": 13, "D": 4},
            2014: {"N": 14, "C": 9, "D": 5},
            2015: {"N": 28, "C": 19, "D": 9},
            2016: {"N": 14, "C": 10, "D": 4}
        },
        "sensitivity": 87.54
    },
    "Cluj-Napoca": {
        "country": "Romania",
        "city_no": 29,
        "years": {
            2012: {"N": 26, "C": 27, "D": 1},
            2013: {"N": 19, "C": 20, "D": 1},
            2014: {"N": 29, "C": 31, "D": 2},
            2015: {"N": 22, "C": 20, "D": 2}
        },
        "sensitivity": 96.57
    },
    "Lisbon": {
        "country": "Portugal",
        "city_no": 30,
        "years": {
            2012: {"N": 10, "C": 9, "D": 1},
            2013: {"N": 21, "C": 16, "D": 5},
            2014: {"N": 20, "C": 18, "D": 2},
            2015: {"N": 30, "C": 30, "D": 0},
            2016: {"N": 11, "C": 18, "D": 7}
        },
        "sensitivity": 90.70
    },
    "Zagreb": {
        "country": "Croatia",
        "city_no": 31,
        "years": {
            2012: {"N": 28, "C": 32, "D": 4},
            2013: {"N": 21, "C": 23, "D": 2},
            2014: {"N": 31, "C": 36, "D": 5},
            2015: {"N": 23, "C": 23, "D": 0}
        },
        "sensitivity": 92.73
    },
    "Madrid": {
        "country": "Spain",
        "city_no": 32,
        "years": {
            2012: {"N": 8, "C": 10, "D": 2},
            2013: {"N": 16, "C": 19, "D": 3},
            2014: {"N": 24, "C": 26, "D": 2},
            2015: {"N": 32, "C": 38, "D": 6},
            2016: {"N": 15, "C": 22, "D": 7}
        },
        "sensitivity": 89.44
    },
    "Brussels": {
        "country": "Belgium",
        "city_no": 33,
        "years": {
            2012: {"N": 13, "C": 8, "D": 5},
            2013: {"N": 12, "C": 11, "D": 1},
            2014: {"N": 17, "C": 13, "D": 4},
            2015: {"N": 33, "C": 25, "D": 8},
            2016: {"N": 27, "C": 25, "D": 2}
        },
        "sensitivity": 89.03
    },
    "Poznan": {
        "country": "Poland",
        "city_no": 34,
        "years": {
            2012: {"N": 34, "C": 33, "D": 1}
        },
        "sensitivity": 98.25
    },
    "Warsaw": {
        "country": "Poland",
        "city_no": 35,
        "years": {
            2012: {"N": 16, "C": 19, "D": 3},
            2013: {"N": 23, "C": 23, "D": 0},
            2014: {"N": 26, "C": 25, "D": 1},
            2015: {"N": 35, "C": 40, "D": 5},
            2016: {"N": 28, "C": 31, "D": 3}
        },
        "sensitivity": 93.06
    },
    "Bratislava": {
        "country": "Slovakia",
        "city_no": 36,
        "years": {
            2012: {"N": 20, "C": 20, "D": 0},
            2013: {"N": 36, "C": 34, "D": 2},
            2014: {"N": 21, "C": 21, "D": 0}
        },
        "sensitivity": 97.62
    },
    "Brasov": {
        "country": "Romania",
        "city_no": 37,
        "years": {
            2012: {"N": 37, "C": 27, "D": 10}
        },
        "sensitivity": 82.46
    },
    "Manchester": {
        "country": "United Kingdom",
        "city_no": 38,
        "years": {
            2012: {"N": 18, "C": 11, "D": 7},
            2013: {"N": 38, "C": 32, "D": 6},
            2014: {"N": 18, "C": 15, "D": 3}
        },
        "sensitivity": 88.41
    },
    "Wroclaw": {
        "country": "Poland",
        "city_no": 39,
        "years": {
            2012: {"N": 24, "C": 26, "D": 2},
            2013: {"N": 27, "C": 22, "D": 5},
            2014: {"N": 39, "C": 37, "D": 2},
            2015: {"N": 35, "C": 35, "D": 0}
        },
        "sensitivity": 93.78
    },
    "London": {
        "country": "United Kingdom",
        "city_no": 40,
        "years": {
            2012: {"N": 18, "C": 20, "D": 2},
            2013: {"N": 27, "C": 31, "D": 4},
            2014: {"N": 22, "C": 27, "D": 5},
            2015: {"N": 40, "C": 46, "D": 6},
            2016: {"N": 42, "C": 46, "D": 4}
        },
        "sensitivity": 89.70
    },
    "Barcelona": {
        "country": "Spain",
        "city_no": 41,
        "years": {
            2012: {"N": 30, "C": 28, "D": 2},
            2013: {"N": 28, "C": 28, "D": 0},
            2014: {"N": 41, "C": 41, "D": 0},
            2015: {"N": 26, "C": 28, "D": 2}
        },
        "sensitivity": 96.94
    },
    "Riga": {
        "country": "Latvia",
        "city_no": 42,
        "years": {
            2012: {"N": 42, "C": 42, "D": 0},
            2013: {"N": 32, "C": 29, "D": 3}
        },
        "sensitivity": 95.97
    },
    "Krakow": {
        "country": "Poland",
        "city_no": 43,
        "years": {
            2012: {"N": 43, "C": 43, "D": 0},
            2013: {"N": 33, "C": 37, "D": 4}
        },
        "sensitivity": 94.63
    },
    "Paris": {
        "country": "France",
        "city_no": 44,
        "years": {
            2012: {"N": 15, "C": 17, "D": 2},
            2013: {"N": 22, "C": 24, "D": 2},
            2014: {"N": 25, "C": 29, "D": 4},
            2015: {"N": 44, "C": 48, "D": 4},
            2016: {"N": 38, "C": 41, "D": 3}
        },
        "sensitivity": 92.68
    },
    "Budapest": {
        "country": "Hungary",
        "city_no": 45,
        "years": {
            2012: {"N": 17, "C": 14, "D": 3},
            2013: {"N": 31, "C": 22, "D": 9},
            2014: {"N": 29, "C": 24, "D": 5},
            2015: {"N": 45, "C": 39, "D": 6},
            2016: {"N": 37, "C": 33, "D": 4}
        },
        "sensitivity": 86.49
    },
    "Banja Luka": {
        "country": "Bosnia and Herzegovina",
        "city_no": 46,
        "years": {
            2012: {"N": 25, "C": 25, "D": 0},
            2013: {"N": 30, "C": 31, "D": 1},
            2014: {"N": 46, "C": 45, "D": 1}
        },
        "sensitivity": 98.21
    },
    "Minsk": {
        "country": "Belarus",
        "city_no": 47,
        "years": {
            2012: {"N": 47, "C": 50, "D": 3},
            2013: {"N": 45, "C": 45, "D": 0}
        },
        "sensitivity": 95.97
    },
    "Sofia": {
        "country": "Bulgaria",
        "city_no": 48,
        "years": {
            2012: {"N": 19, "C": 16, "D": 3},
            2013: {"N": 34, "C": 30, "D": 4},
            2014: {"N": 32, "C": 30, "D": 2},
            2015: {"N": 48, "C": 44, "D": 4},
            2016: {"N": 34, "C": 30, "D": 4}
        },
        "sensitivity": 91.83
    },
    "Turin": {
        "country": "Italy",
        "city_no": 49,
        "years": {
            2012: {"N": 49, "C": 47, "D": 2},
            2013: {"N": 30, "C": 34, "D": 4}
        },
        "sensitivity": 94.00
    },
    "Milan": {
        "country": "Italy",
        "city_no": 50,
        "years": {
            2012: {"N": 21, "C": 21, "D": 0},
            2013: {"N": 33, "C": 34, "D": 1},
            2014: {"N": 33, "C": 33, "D": 0},
            2015: {"N": 50, "C": 52, "D": 2},
            2016: {"N": 36, "C": 39, "D": 3}
        },
        "sensitivity": 96.09
    },
    "Belgrade": {
        "country": "Serbia",
        "city_no": 51,
        "years": {
            2012: {"N": 22, "C": 24, "D": 2},
            2013: {"N": 35, "C": 37, "D": 2},
            2014: {"N": 31, "C": 34, "D": 3},
            2015: {"N": 51, "C": 53, "D": 2},
            2016: {"N": 41, "C": 42, "D": 1}
        },
        "sensitivity": 95.09
    },
    "Athens": {
        "country": "Greece",
        "city_no": 52,
        "years": {
            2012: {"N": 25, "C": 22, "D": 3},
            2013: {"N": 35, "C": 35, "D": 1},
            2014: {"N": 34, "C": 32, "D": 2},
            2015: {"N": 52, "C": 49, "D": 3},
            2016: {"N": 39, "C": 36, "D": 3}
        },
        "sensitivity": 94.18
    },
    "Bucharest": {
        "country": "Romania",
        "city_no": 53,
        "years": {
            2012: {"N": 23, "C": 23, "D": 0},
            2013: {"N": 37, "C": 36, "D": 1},
            2014: {"N": 35, "C": 35, "D": 0},
            2015: {"N": 53, "C": 51, "D": 2},
            2016: {"N": 44, "C": 40, "D": 4}
        },
        "sensitivity": 95.21
    },
    "Chisinau": {
        "country": "Moldova",
        "city_no": 54,
        "years": {
            2012: {"N": 54, "C": 55, "D": 1}
        },
        "sensitivity": 98.25
    },
    "Saint Petersburg": {
        "country": "Russia",
        "city_no": 55,
        "years": {
            2012: {"N": 38, "C": 37, "D": 1},
            2013: {"N": 55, "C": 54, "D": 1},
            2014: {"N": 47, "C": 47, "D": 0}
        },
        "sensitivity": 98.31
    },
    "Rome": {
        "country": "Italy",
        "city_no": 56,
        "years": {
            2012: {"N": 24, "C": 25, "D": 1},
            2013: {"N": 38, "C": 39, "D": 1},
            2014: {"N": 36, "C": 38, "D": 2},
            2015: {"N": 56, "C": 57, "D": 1},
            2016: {"N": 43, "C": 44, "D": 1}
        },
        "sensitivity": 97.04
    },
    "Kiev": {
        "country": "Ukraine",
        "city_no": 57,
        "years": {
            2012: {"N": 39, "C": 38, "D": 1},
            2013: {"N": 37, "C": 36, "D": 1},
            2014: {"N": 57, "C": 56, "D": 1},
            2015: {"N": 49, "C": 49, "D": 0}
        },
        "sensitivity": 98.12
    },
    "Moscow": {
        "country": "Russia",
        "city_no": 58,
        "years": {
            2012: {"N": 26, "C": 26, "D": 0},
            2013: {"N": 40, "C": 40, "D": 0},
            2014: {"N": 39, "C": 39, "D": 0},
            2015: {"N": 58, "C": 58, "D": 0},
            2016: {"N": 48, "C": 48, "D": 0}
        },
        "sensitivity": 100.00
    },
    "Reykjavik": {
        "country": "Iceland",
        "city_no": 59,
        "years": {
            2012: {"N": 9, "C": 2, "D": 7}
        },
        "sensitivity": 85.42
    },
    "Timisoara": {
        "country": "Romania",
        "city_no": 60,
        "years": {
            2013: {"N": 19, "C": 16, "D": 3}
        },
        "sensitivity": 93.75
    },
    "Novi Sad": {
        "country": "Serbia",
        "city_no": 61,
        "years": {
            2013: {"N": 29, "C": 27, "D": 2}
        },
        "sensitivity": 95.83
    },
    "Sarajevo": {
        "country": "Bosnia and Herzegovina",
        "city_no": 62,
        "years": {
            2013: {"N": 40, "C": 38, "D": 2}
        },
        "sensitivity": 95.83
    },
    "Skopje": {
        "country": "Macedonia",
        "city_no": 63,
        "years": {
            2013: {"N": 46, "C": 43, "D": 3}
        },
        "sensitivity": 93.75
    },
    "Bergen": {
        "country": "Norway",
        "city_no": 64,
        "years": {
            2014: {"N": 5, "C": 6, "D": 1},
            2015: {"N": 3, "C": 4, "D": 1}
        },
        "sensitivity": 97.40
    },
    "Belfast": {
        "country": "United Kingdom",
        "city_no": 65,
        "years": {
            2014: {"N": 7, "C": 1, "D": 6}
        },
        "sensitivity": 84.62
    },
    "Constanta": {
        "country": "Romania",
        "city_no": 66,
        "years": {
            2015: {"N": 14, "C": 15, "D": 1},
            2016: {"N": 29, "C": 33, "D": 4}
        },
        "sensitivity": 91.10
    }
}

@mcp.tool()
def find_city_score(city: str) -> float:
    return european_cities_data[city.capitalize()]["sensitivity"]

@mcp.tool()
def list_cities():
    cities = {}
    for city in european_cities_data:
        cities = {
            **cities, 
            city: {
                "city": city,
                "sensitivity": european_cities_data[city]['sensitivity']
            }
        }
    return cities

if __name__ == "__main__":
    mcp.run()