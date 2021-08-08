cols = df.columns.tolist()
print(cols)
#print("cols[-1] =", cols[-1])
#print("cols[:-1] = ", cols[:-1])
#print("cols[-1:] = ", cols[-1:])
#print("cols[1:2] = ", cols[1:2])

#1:3 will give cols[1] and cols[2]
cols = cols[1:3]  + cols[0:1]
print(cols)
df.columns = cols
print(df)
