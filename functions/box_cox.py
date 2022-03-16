def box_cox(data_set):
  #data_set: dataframe
  transformed, lam = scipystats.boxcox(data_set.squeeze())
  print(transformed)
  plt.plot(transformed)
  plt.show()
  qqplot(transformed, line = "r")
  plt.show()
  
