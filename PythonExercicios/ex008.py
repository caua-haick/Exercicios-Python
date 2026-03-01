m = float(input('Uma distância em metros: '))
print('{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'
      .format(m/1000,m/100,m/10,m*10,m*100,m*1000))