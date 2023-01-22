well_planned = 8000
LateralLength_FT = 500
LiquidsProd_BBL = 1000
GasProd_MCF = 8000
WaterProd_BBL = 500
ProducingDays = 30


data_oil = (LiquidsProd_BBL) * (well_planned / LateralLength_FT) * (30.4 / ProducingDays)
print(data_oil)

data_gas = (GasProd_MCF) * (well_planned / LateralLength_FT) * (30.4 / ProducingDays)
print(data_gas)

data_water = (WaterProd_BBL) * (well_planned / LateralLength_FT) * (30.4 / ProducingDays)
print(data_water)

data_oilv2 = lambda well_planned: LiquidsProd_BBL * ( well_planned / LateralLength_FT) * (30.4 / ProducingDays)
print(data_oilv2(well_planned))

data_gasv2 = lambda well_planned: GasProd_MCF * ( well_planned / LateralLength_FT) * (30.4 / ProducingDays)
print(data_gasv2(well_planned))

data_waterv2 = lambda well_planned: WaterProd_BBL * ( well_planned / LateralLength_FT) * (30.4 / ProducingDays)
print(data_waterv2(well_planned))


# Se adiciona el siguiente codigo para probar ramas

a = 5 + 5
b = 20
x = a * b
print(x)
