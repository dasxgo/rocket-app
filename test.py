well_planned = 5000
LiquidsProd_BBL = 1000
LateralLength_FT = 500
ProducingDays = 30


data_oil = (LiquidsProd_BBL) * (well_planned / LateralLength_FT) * (30.4 / ProducingDays)
print(data_oil)


data_oil = lambda well_planned: LiquidsProd_BBL * ( well_planned / LateralLength_FT) * (30.4 / ProducingDays)
print(data_oil(5000))