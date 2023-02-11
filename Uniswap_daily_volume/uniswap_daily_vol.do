clear
cd "folder with data"

import delimited uniswapvolume.csv

drop if timestamp<1656547200
drop if timestamp>1668729600
gen double date = timestamp*1000 + mdyhms(1,1,1970,0,0,0)
format date %tc

gen totalvolume=.
replace totalvolume=volume if timestamp==1656547200
replace totalvolume=totalvolume[_n-1]+volume if totalvolume==.

export delimited using uniswapdailyvolume.csv, replace
save uniswapdailyvolume.dta, replace
