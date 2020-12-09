import oseti

analyzer = oseti.Analyzer()
analyzer.analyze_detail('お金も希望もない！')
# => [1.0]
analyzer.analyze('今日も充実して満足でした')
# => [0.3333333333333333, 1.0]