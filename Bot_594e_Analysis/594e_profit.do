clear

cd "folder with data"

import delimited 594etoken.csv, clear 

*Consider "clean" sandwiches with one transfer on the front end (two txns) and one at the end (two txns)
gen ones=1
bys blocknumber: egen txn=sum(ones)
drop if txn!=4

*Check for any odd gaps in the transaction index
bys blocknumber: gen order=_n
bys blocknumber: egen maxtxn=max(transactionindex)
bys blocknumber: egen mintxn=min(transactionindex)
gen txndif=maxtxn-mintxn
tab txndif

*Get the additional value in ETH
sort blocknumber tokenname transactionindex order
bys blocknumber tokenname: gen revenue=value[_n]-value[_n-1]

*Drop swaps that only involve WETH
gen eth=(tokensymbol=="WETH")
bys blocknumber: egen ethonly=mean(eth)
drop if ethonly==1


*Gen gas cost
gen gascost=gasused*gasprice/(10^18)
bys blocknumber: egen maxgas=max(gascost)
bys blocknumber: egen mingas=min(gascost)
gen totalgas=maxgas+mingas

*Replace revenue = 0 in relevant observations before collapse
replace rev=0 if rev==.
replace rev=0 if rev==-1
replace rev=0 if tokensymbol!="WETH"
replace rev = rev/(10^18)
collapse (sum) rev (mean) ones totalgas, by(blocknumber)

*Fill in blocknumbers and replace
tsset blocknumber
tsfill
foreach i in revenue ones totalgas {
	replace `i' = 0 if `i' == .
}

*Generate profit and collapse by 1000 block increments
gen profit = revenue - totalgas

gen blockgroup=floor(blocknumber/1000)
collapse (sum) profit ones, by(blockgroup)
drop if blockgroup<=15049
rename ones txn
gen merge=(blockgroup>15537)
gen avgprofit=profit/txn

*Test txn, profit per 1000 and avg profit per txn by merge
foreach i in txn profit avgprofit {
	ttest `i', by(merge)
}

drop if avgprofit==.

save 594eprofit.dta, replace
export delimited using 594eprofit.csv, replace 

clear

*Run regression discontinuity

import delimited 594etxn.csv, clear 
gen txn=1
gen blockgroup=floor(blocknumber/1000)
collapse (sum) txn iserror, by(blockgroup)
gen error_rate=iserror/txn
gen merge=(blockgroup>15537)
ttest error_rate, by(merge)

merge m:m blockgroup using 594eprofit.dta

drop if blockgroup<15050

replace profit=0 if profit==.
replace avgprofit=0 if avgprofit==.
gen negprofit=(profit<0)
ttest negprofit, by(merge)

gen block0=blockgroup-15537
gen interaction=merge*block0
gen block0_2=block0^2
gen interaction_2=merge*block0_2

reg txn block0 block0_2 interaction interaction_2 merge, robust
outreg2 using 594e_reg, replace

reg error_rate block0 block0_2 interaction interaction_2 merge, robust
outreg2 using 594e_reg, excel

drop _merge

save 594etransactions.dta, replace
export delimited using 594etransactions.csv, replace 
