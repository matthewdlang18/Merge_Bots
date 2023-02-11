clear
cd "folder with data"

use blocktimes_raw.dta 
rangestat (sd) blocktime, interval(blocknumber -10 0)
rename blocktime_sd sd_blocktime_10
rangestat (sd) blocktime, interval(blocknumber -100 0)
rename blocktime_sd sd_blocktime_100
rangestat (sd) blocktime, interval(blocknumber -1000 0)
rename blocktime_sd sd_blocktime_1000

*Run a regression discontinuity for blocktime and sd of blocktime
gen block0=blocknumber-15537393
replace block0=block0/1000
gen merge=(block0>0)
gen interaction=merge*block0
gen block0_2=block0^2
gen interaction_2=merge*block0_2

reg blocktime block0 block0_2 interaction interaction_2 merge, robust
outreg2 using blocktime_reg, replace

foreach i in sd_blocktime_10 sd_blocktime_100 sd_blocktime_1000 {
quietly reg `i' block0 block0_2 interaction interaction_2 merge, robust
outreg2 using blocktime_reg, excel
}

foreach i in blocktime sd_blocktime_10 sd_blocktime_100 sd_blocktime_1000 {
ttest `i', by(merge)
}