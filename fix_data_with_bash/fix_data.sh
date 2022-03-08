#! /bin/bash

rm -rf test1.csv
rm -rf test2.csv
rm -rf test3.csv
rm -rf test4.csv
rm -rf test5.csv

awk {'print $1'} robberies.csv >> test1.csv
awk {'print $2'} robberies.csv >> test2.csv
awk -F, '{sub($1, "\"&\""); print}' test1.csv >> test3.csv
awk {'print $1","'} test3.csv >> test4.csv
paste test4.csv test2.csv >> test5.csv
mv test5.csv robberies_modified.csv
cat robberies_modified.csv

rm -rf test1.csv
rm -rf test2.csv
rm -rf test3.csv
rm -rf test4.csv
rm -rf test5.csv

