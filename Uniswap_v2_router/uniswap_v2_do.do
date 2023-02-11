clear

import delimited "uniswapv2.csv", clear

gen txn=1
*merge with block times for blocks 15000000 to 16000000
merge m:m blocknumber using "folder path\blocktimes_simple.dta"

gen blockgroup=floor(blocknumber/1000)

collapse (sum) iserror txn, by(blockgroup)
drop if blockgroup<15050

gen error_rate=iserror/txn

save "uniswapv2.dta", replace
export delimited using "uniswapv2txn.csv", replace 

*Run regression discontinuity

gen block0=blockgroup-15537
gen merge=(block0>0)
gen interaction=merge*block0
gen block0_2=block0^2
gen interaction_2=merge*block0_2

reg txn block0 block0_2 interaction interaction_2 merge , robust
outreg2 using uniswap_v2_reg, replace

reg error_rate block0 block0_2 interaction interaction_2 merge, robust
outreg2 using uniswap_v2_reg, excel
